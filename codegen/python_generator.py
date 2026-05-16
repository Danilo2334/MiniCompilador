from __future__ import annotations

from typing import List

try:
    from generated.gramaticaVisitor import gramaticaVisitor
    from generated.gramaticaParser import gramaticaParser
except ModuleNotFoundError as e:  # pragma: no cover
    raise ModuleNotFoundError(
        "No se encontraron los archivos generados por ANTLR. "
        "Ejecuta: antlr4 -Dlanguage=Python3 -visitor gramatica.g4 -o generated"
    ) from e


class PythonGenerator(gramaticaVisitor):
    def __init__(self) -> None:
        super().__init__()
        self._lines: List[str] = []
        self._indent = 0

    def generate(self, tree: "gramaticaParser.ProgramContext") -> str:
        self.visit(tree)
        return "\n".join(self._lines) + ("\n" if self._lines else "")

    def _emit(self, line: str) -> None:
        self._lines.append(("    " * self._indent) + line)

    # program / statement
    def visitProgram(self, ctx: "gramaticaParser.ProgramContext"):
        for st in ctx.statement():
            self.visit(st)
        return None

    def visitAssignment(self, ctx: "gramaticaParser.AssignmentContext"):
        name = ctx.ID().getText()
        expr = self.visit(ctx.expression())
        self._emit(f"{name} = {expr}")
        return None

    def visitAction(self, ctx: "gramaticaParser.ActionContext"):
        name = ctx.ID().getText()
        expr = self.visit(ctx.expression())
        self._emit(f"{name} = {expr}")
        return None

    def visitPrintStmt(self, ctx: "gramaticaParser.PrintStmtContext"):
        expr = ctx.ID().getText()
        self._emit(f"print({expr})")
        return None

    def visitRule_(self, ctx: "gramaticaParser.Rule_Context"):
        cond = self.visit(ctx.condition())
        self._emit(f"if {cond}:")
        self._indent += 1
        self.visit(ctx.action())
        self._indent -= 1
        return None

    # condition / expressions return str
    def visitCondition(self, ctx: "gramaticaParser.ConditionContext"):
        left = self.visit(ctx.expression(0))
        op = ctx.comparator().getText()
        if op == "=":
            op = "=="
        right = self.visit(ctx.expression(1))
        return f"{left} {op} {right}"

    def visitExpression(self, ctx: "gramaticaParser.ExpressionContext"):
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        if ctx.ID():
            return ctx.ID().getText()
        if ctx.getChildCount() == 3:
            first = ctx.getChild(0).getText()
            if first == "(":
                return self.visit(ctx.expression(0))
            left = self.visit(ctx.expression(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expression(1))
            return f"({left} {op} {right})"
        return self.visitChildren(ctx)

