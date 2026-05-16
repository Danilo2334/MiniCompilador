from generated.gramaticaVisitor import gramaticaVisitor
from semantic_analyzer.semantic_errors import SemanticError
from semantic_analyzer.symbol_table import SymbolTable


class SemanticVisitor(gramaticaVisitor):

    def __init__(self, symbol_table=None):
        self.symbol_table = symbol_table or SymbolTable()

    def visitProgram(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)
        return self.symbol_table

    def visitAssignment(self, ctx):
        variable_name = ctx.ID().getText()
        self.visit(ctx.expression())
        self.symbol_table.declare(variable_name, "number")

    def visitAction(self, ctx):
        variable_name = ctx.ID().getText()
        self.visit(ctx.expression())
        self.symbol_table.declare(variable_name, "number")

    def visitPrintStmt(self, ctx):
        variable_name = ctx.ID().getText()

        if not self.symbol_table.exists(variable_name):
            raise SemanticError(
                f"Error semántico: Variable '{variable_name}' no declarada."
            )

    def visitRule_(self, ctx):
        self.visit(ctx.condition())
        self.visit(ctx.action())

    def visitExpression(self, ctx):
        ids = ctx.ID()

        if not isinstance(ids, list):
            ids = [ids] if ids else []

        for token in ids:
            variable_name = token.getText()

            if not self.symbol_table.exists(variable_name):
                raise SemanticError(
                    f"Error semántico: Variable '{variable_name}' no declarada."
                )

        return "number"