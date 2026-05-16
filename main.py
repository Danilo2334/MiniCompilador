from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.ErrorStrategy import BailErrorStrategy

ROOT = Path(__file__).resolve().parent

INPUT_PATH = ROOT / "input.txt"
OUTPUT_LOG = ROOT / "output.txt"
OUTPUT_PY = ROOT / "output_program.py"

GRAMMAR_PATH = ROOT / "gramatica.g4"
GENERATED_DIR = ROOT / "generated"


class CompilationError(Exception):
    pass


@dataclass
class CollectedError:
    kind: str
    line: int
    column: int
    msg: str

    def format(self) -> str:
        return (
            f"Error {self.kind}: "
            f"línea {self.line}:{self.column} {self.msg}"
        )


class CollectingErrorListener(ErrorListener):

    def __init__(self, kind: str, errors: List[CollectedError]):
        super().__init__()
        self.kind = kind
        self.errors = errors

    def syntaxError(
        self,
        recognizer,
        offendingSymbol,
        line,
        column,
        msg,
        e
    ):
        self.errors.append(
            CollectedError(
                kind=self.kind,
                line=line,
                column=column,
                msg=msg
            )
        )


def ensure_generated():

    required = [
        GENERATED_DIR / "gramaticaLexer.py",
        GENERATED_DIR / "gramaticaParser.py",
        GENERATED_DIR / "gramaticaVisitor.py",
    ]

    if all(p.exists() for p in required):
        return

    try:
        subprocess.run(
            [
                "antlr4",
                "-Dlanguage=Python3",
                "-visitor",
                str(GRAMMAR_PATH),
                "-o",
                str(GENERATED_DIR),
            ],
            cwd=str(ROOT),
            check=True,
            capture_output=True,
            text=True,
        )

    except Exception as e:

        missing = [
            str(p.relative_to(ROOT))
            for p in required
            if not p.exists()
        ]

        raise CompilationError(
            "No se encontraron archivos generados por ANTLR.\n"
            f"Faltan: {', '.join(missing)}\n\n"
            "Ejecuta:\n"
            "antlr4 -Dlanguage=Python3 "
            "-visitor gramatica.g4 -o generated"
        ) from e


def load_antlr():

    sys.path.insert(0, str(ROOT))
    sys.path.insert(0, str(GENERATED_DIR))

    try:

        from generated.gramaticaLexer import gramaticaLexer
        from generated.gramaticaParser import gramaticaParser

    except ModuleNotFoundError as e:

        raise CompilationError(
            "No se pudo importar lexer/parser.\n"
            "Verifica generated/"
        ) from e

    return gramaticaLexer, gramaticaParser


def compile_source(source_path: Path):

    ensure_generated()

    gramaticaLexer, gramaticaParser = load_antlr()

    errors: List[CollectedError] = []

    input_stream = FileStream(
        str(source_path),
        encoding="utf-8"
    )

    lexer = gramaticaLexer(input_stream)

    lexer.removeErrorListeners()

    lexer.addErrorListener(
        CollectingErrorListener("LÉXICO", errors)
    )

    token_stream = CommonTokenStream(lexer)

    # fuerza análisis completo
    token_stream.fill()

    error_type = getattr(
        gramaticaLexer,
        "ERROR_CHAR",
        None
    )

    if error_type is not None:

        bad_tokens = [
            t for t in token_stream.tokens
            if t.type == error_type
        ]

        for t in bad_tokens:

            errors.append(
                CollectedError(
                    kind="LÉXICO",
                    line=t.line,
                    column=t.column,
                    msg=f"símbolo inválido '{t.text}'",
                )
            )

    parser = gramaticaParser(token_stream)

    # MODO ESTRICTO
    parser._errHandler = BailErrorStrategy()

    parser.removeErrorListeners()

    parser.addErrorListener(
        CollectingErrorListener(
            "SINTÁCTICO",
            errors
        )
    )

    try:

        tree = parser.program()

    except Exception as e:

        if not errors:

            errors.append(
                CollectedError(
                    kind="SINTÁCTICO",
                    line=0,
                    column=0,
                    msg="estructura inválida del programa",
                )
            )

        msgs = "\n".join(
            err.format()
            for err in errors
        )

        raise CompilationError(msgs) from e

    if errors or parser.getNumberOfSyntaxErrors() > 0:

        msgs = (
            "\n".join(e.format() for e in errors)
            or "Error sintáctico."
        )

        raise CompilationError(msgs)

    return tree


def run_semantic(tree):

    from semantic_analyzer.semantic_errors import SemanticError
    from semantic_analyzer.semantic_visitor import SemanticVisitor
    from semantic_analyzer.symbol_table import SymbolTable

    symtab = SymbolTable()

    visitor = SemanticVisitor(symtab)

    try:

        visitor.visit(tree)

    except SemanticError as e:

        raise CompilationError(str(e)) from e

    return symtab


def generate_tac(tree):

    from codegen.tac_generator import TACGenerator

    gen = TACGenerator()

    instrs = gen.generate(tree)

    return [i.to_line() for i in instrs]


def generate_python(tree):

    from codegen.python_generator import PythonGenerator

    gen = PythonGenerator()

    return gen.generate(tree)


def main():

    logs: List[str] = []

    try:

        if not INPUT_PATH.exists():

            raise CompilationError(
                f"No existe {INPUT_PATH.name}"
            )

        tree = compile_source(INPUT_PATH)

        logs.append(
            "ANÁLISIS SINTÁCTICO EXITOSO"
        )

        run_semantic(tree)

        logs.append(
            "ANÁLISIS SEMÁNTICO EXITOSO"
        )

        tac_lines = generate_tac(tree)

        logs.append("")
        logs.append(
            "=== TAC (Three Address Code) ==="
        )

        logs.extend(tac_lines)

        py_code = generate_python(tree)

        OUTPUT_PY.write_text(
            py_code,
            encoding="utf-8"
        )

        logs.append("")
        logs.append(
            "CÓDIGO PYTHON GENERADO"
        )

        OUTPUT_LOG.write_text(
            "\n".join(logs) + "\n",
            encoding="utf-8"
        )

        print("ANÁLISIS SINTÁCTICO EXITOSO")
        print("ANÁLISIS SEMÁNTICO EXITOSO")
        print("CÓDIGO PYTHON GENERADO")

        return 0

    except CompilationError as e:

        msg = str(e).strip()

        OUTPUT_LOG.write_text(
            msg + "\n",
            encoding="utf-8"
        )

        print(msg)

        return 1


if __name__ == "__main__":
    raise SystemExit(main())
