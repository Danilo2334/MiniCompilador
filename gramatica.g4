grammar gramatica;

program : statement+ EOF ;

statement
    : assignment
    | rule_
    | printStmt
    ;

assignment
    : ID '=' expression ';'
    ;

rule_
    : 'si' condition ':' action
    ;

action
    : ID '=' expression ';'
    ;

printStmt
    : 'print' '(' ID ')' ';'
    ;

condition
    : expression comparator expression
    ;

expression
    : expression ('*' | '/') expression
    | expression ('+' | '-') expression
    | '(' expression ')'
    | NUMBER
    | ID
    ;

comparator
    : '>'
    | '<'
    | '>='
    | '<='
    | '=='
    ;

SI      : 'si' ;
PRINT   : 'print' ;

ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER  : [0-9]+ ('.' [0-9]+)? ;

COMMENT : '#' ~[\r\n]* -> skip ;
WS      : [ \t\r\n]+ -> skip ;

ERROR_CHAR : . ;