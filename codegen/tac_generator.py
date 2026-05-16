from __future__ import annotations

from typing import List, Tuple

from codegen.ir_nodes import (
    TACAssign,
    TACBinary,
    TACGoto,
    TACIfFalse,
    TACInstr,
    TACLabel,
    TACPrint,
)

try:
    from generated.gramaticaVisitor import gramaticaVisitor
    from generated.gramaticaParser import gramaticaParser
except ModuleNotFoundError as e:  # pragma: no cover
    raise ModuleNotFoundError(
        "No se encontraron los archivos generados por ANTLR. "
        "Ejecuta: antlr4 -Dlanguage=Python3 -visitor gramatica.g4 -o generated"
    ) from e


class TACGenerator(gramaticaVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.instructions: List[TACInstr] = []
        self._temp_counter = 0
        self._label_counter = 0

    def new_temp(self) -> str:
        self._temp_counter += 1
        return f"t{self._temp_counter}"

    def new_label(self) -> str:
        self._label_counter += 1
        return f"L{self._label_counter}"

    def generate(self, tree: "gramaticaParser.ProgramContext") -> List[TACInstr]:
        self.visit(tree)
        return self.instructions

    # program / statements
    def visitProgram(self, ctx: "gramaticaParser.ProgramContext"):
        for st in ctx.statement():
            self.visit(st)
        return None

    def visitAssignment(self, ctx: "gramaticaParser.AssignmentContext"):
        target = ctx.ID().getText()
        value_place = self.visit(ctx.expression())
        self.instructions.append(TACAssign(target=target, value=value_place))
        return None

    def visitAction(self, ctx: "gramaticaParser.ActionContext"):
        target = ctx.ID().getText()
        value_place = self.visit(ctx.expression())
        self.instructions.append(TACAssign(target=target, value=value_place))
        return None

    def visitPrintStmt(self, ctx: "gramaticaParser.PrintStmtContext"):
        value_place = ctx.ID().getText()
        self.instructions.append(TACPrint(value=value_place))
        return None

    def visitRule_(self, ctx: "gramaticaParser.Rule_Context"):
        left, op, right = self._visit_condition(ctx.condition())
        end_label = self.new_label()
        self.instructions.append(TACIfFalse(left=left, op=op, right=right, goto_label=end_label))
        self.visit(ctx.action())
        self.instructions.append(TACLabel(name=end_label))
        return None

    # condition helpers
    def _visit_condition(self, ctx: "gramaticaParser.ConditionContext") -> Tuple[str, str, str]:
        left = self.visit(ctx.expression(0))
        op = ctx.comparator().getText()
        if op == "=":
            op = "=="
        right = self.visit(ctx.expression(1))
        return left, op, right

    # expressions return "place" (var/const/temp)
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
            tmp = self.new_temp()
            self.instructions.append(TACBinary(target=tmp, left=left, op=op, right=right))
            return tmp
        return self.visitChildren(ctx)
