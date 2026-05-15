# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#program.
    def visitProgram(self, ctx:gramaticaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#statement.
    def visitStatement(self, ctx:gramaticaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#assignment.
    def visitAssignment(self, ctx:gramaticaParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#rule_.
    def visitRule_(self, ctx:gramaticaParser.Rule_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#action.
    def visitAction(self, ctx:gramaticaParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#printStmt.
    def visitPrintStmt(self, ctx:gramaticaParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#condition.
    def visitCondition(self, ctx:gramaticaParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#expression.
    def visitExpression(self, ctx:gramaticaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#comparator.
    def visitComparator(self, ctx:gramaticaParser.ComparatorContext):
        return self.visitChildren(ctx)



del gramaticaParser