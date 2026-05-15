# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#program.
    def enterProgram(self, ctx:gramaticaParser.ProgramContext):
        pass

    # Exit a parse tree produced by gramaticaParser#program.
    def exitProgram(self, ctx:gramaticaParser.ProgramContext):
        pass


    # Enter a parse tree produced by gramaticaParser#statement.
    def enterStatement(self, ctx:gramaticaParser.StatementContext):
        pass

    # Exit a parse tree produced by gramaticaParser#statement.
    def exitStatement(self, ctx:gramaticaParser.StatementContext):
        pass


    # Enter a parse tree produced by gramaticaParser#assignment.
    def enterAssignment(self, ctx:gramaticaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by gramaticaParser#assignment.
    def exitAssignment(self, ctx:gramaticaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by gramaticaParser#rule_.
    def enterRule_(self, ctx:gramaticaParser.Rule_Context):
        pass

    # Exit a parse tree produced by gramaticaParser#rule_.
    def exitRule_(self, ctx:gramaticaParser.Rule_Context):
        pass


    # Enter a parse tree produced by gramaticaParser#action.
    def enterAction(self, ctx:gramaticaParser.ActionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#action.
    def exitAction(self, ctx:gramaticaParser.ActionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#printStmt.
    def enterPrintStmt(self, ctx:gramaticaParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#printStmt.
    def exitPrintStmt(self, ctx:gramaticaParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#condition.
    def enterCondition(self, ctx:gramaticaParser.ConditionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#condition.
    def exitCondition(self, ctx:gramaticaParser.ConditionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#expression.
    def enterExpression(self, ctx:gramaticaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#expression.
    def exitExpression(self, ctx:gramaticaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#comparator.
    def enterComparator(self, ctx:gramaticaParser.ComparatorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#comparator.
    def exitComparator(self, ctx:gramaticaParser.ComparatorContext):
        pass



del gramaticaParser