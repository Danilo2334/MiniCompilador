# Generated from gramatica.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,78,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,3,7,63,8,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,71,8,7,10,7,12,
        7,74,9,7,1,8,1,8,1,8,0,1,14,9,0,2,4,6,8,10,12,14,16,0,3,1,0,6,7,
        1,0,8,9,1,0,10,14,75,0,19,1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,6,35,
        1,0,0,0,8,40,1,0,0,0,10,45,1,0,0,0,12,51,1,0,0,0,14,62,1,0,0,0,16,
        75,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,
        0,21,22,1,0,0,0,22,23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,29,3,
        4,2,0,26,29,3,6,3,0,27,29,3,10,5,0,28,25,1,0,0,0,28,26,1,0,0,0,28,
        27,1,0,0,0,29,3,1,0,0,0,30,31,5,17,0,0,31,32,5,1,0,0,32,33,3,14,
        7,0,33,34,5,2,0,0,34,5,1,0,0,0,35,36,5,15,0,0,36,37,3,12,6,0,37,
        38,5,3,0,0,38,39,3,8,4,0,39,7,1,0,0,0,40,41,5,17,0,0,41,42,5,1,0,
        0,42,43,3,14,7,0,43,44,5,2,0,0,44,9,1,0,0,0,45,46,5,16,0,0,46,47,
        5,4,0,0,47,48,5,17,0,0,48,49,5,5,0,0,49,50,5,2,0,0,50,11,1,0,0,0,
        51,52,3,14,7,0,52,53,3,16,8,0,53,54,3,14,7,0,54,13,1,0,0,0,55,56,
        6,7,-1,0,56,57,5,4,0,0,57,58,3,14,7,0,58,59,5,5,0,0,59,63,1,0,0,
        0,60,63,5,18,0,0,61,63,5,17,0,0,62,55,1,0,0,0,62,60,1,0,0,0,62,61,
        1,0,0,0,63,72,1,0,0,0,64,65,10,5,0,0,65,66,7,0,0,0,66,71,3,14,7,
        6,67,68,10,4,0,0,68,69,7,1,0,0,69,71,3,14,7,5,70,64,1,0,0,0,70,67,
        1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,15,1,0,0,0,
        74,72,1,0,0,0,75,76,7,2,0,0,76,17,1,0,0,0,5,21,28,62,70,72
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "':'", "'('", "')'", "'*'", 
                     "'/'", "'+'", "'-'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'si'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SI", "PRINT", 
                      "ID", "NUMBER", "COMMENT", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_rule_ = 3
    RULE_action = 4
    RULE_printStmt = 5
    RULE_condition = 6
    RULE_expression = 7
    RULE_comparator = 8

    ruleNames =  [ "program", "statement", "assignment", "rule_", "action", 
                   "printStmt", "condition", "expression", "comparator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    SI=15
    PRINT=16
    ID=17
    NUMBER=18
    COMMENT=19
    WS=20
    ERROR_CHAR=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gramaticaParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = gramaticaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0)):
                    break

            self.state = 23
            self.match(gramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(gramaticaParser.AssignmentContext,0)


        def rule_(self):
            return self.getTypedRuleContext(gramaticaParser.Rule_Context,0)


        def printStmt(self):
            return self.getTypedRuleContext(gramaticaParser.PrintStmtContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = gramaticaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.assignment()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.rule_()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.printStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = gramaticaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(gramaticaParser.ID)
            self.state = 31
            self.match(gramaticaParser.T__0)
            self.state = 32
            self.expression(0)
            self.state = 33
            self.match(gramaticaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(gramaticaParser.SI, 0)

        def condition(self):
            return self.getTypedRuleContext(gramaticaParser.ConditionContext,0)


        def action(self):
            return self.getTypedRuleContext(gramaticaParser.ActionContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_rule_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_" ):
                listener.enterRule_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_" ):
                listener.exitRule_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_" ):
                return visitor.visitRule_(self)
            else:
                return visitor.visitChildren(self)




    def rule_(self):

        localctx = gramaticaParser.Rule_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rule_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(gramaticaParser.SI)
            self.state = 36
            self.condition()
            self.state = 37
            self.match(gramaticaParser.T__2)
            self.state = 38
            self.action()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = gramaticaParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(gramaticaParser.ID)
            self.state = 41
            self.match(gramaticaParser.T__0)
            self.state = 42
            self.expression(0)
            self.state = 43
            self.match(gramaticaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(gramaticaParser.PRINT, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = gramaticaParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(gramaticaParser.PRINT)
            self.state = 46
            self.match(gramaticaParser.T__3)
            self.state = 47
            self.match(gramaticaParser.ID)
            self.state = 48
            self.match(gramaticaParser.T__4)
            self.state = 49
            self.match(gramaticaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressionContext,i)


        def comparator(self):
            return self.getTypedRuleContext(gramaticaParser.ComparatorContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = gramaticaParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.expression(0)
            self.state = 52
            self.comparator()
            self.state = 53
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressionContext,i)


        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 56
                self.match(gramaticaParser.T__3)
                self.state = 57
                self.expression(0)
                self.state = 58
                self.match(gramaticaParser.T__4)
                pass
            elif token in [18]:
                self.state = 60
                self.match(gramaticaParser.NUMBER)
                pass
            elif token in [17]:
                self.state = 61
                self.match(gramaticaParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 70
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 64
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 65
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 66
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 67
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 68
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 69
                        self.expression(5)
                        pass

             
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = gramaticaParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




