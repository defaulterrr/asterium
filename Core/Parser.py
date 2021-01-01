import ply.yacc as yacc

from Lexer import tokens

from Library.Add import Add
from Library.Sub import Sub
from Library.Mul import Mul
from Library.Div import Div
from Library.Number import Number
from Library.Assignment import Assignment
from Library.Declaration import Declaration
from Library.Function import Function
from Library.FunctionCall import FunctionCall
from Library.Node import Node
from Library.ID import ID
from Library.Condition import Condition
from Library.Conditional import Conditional

# arithmetics - DONE
# function declaration - DONE
# function calls - DONE

# conditional statements - WIP 

precedence = (
    ('left','ASSIGN'),
    ('left','PLUS','MINUS'),
    ('left','MUL','DIV')
)

def p_expression(p):
    '''expression : expression SMCLN
                | decl_function
                | number
    '''
    p[0] = p[1]

def p_expression_list_from_list(p):
    ''' expression : expression_list
    '''
    p[0] = p[1]

def p_function_call(p):
    ''' expression : ID LPAR RPAR
    '''
    p[0] = FunctionCall(p[1])

def p_expression_list(p):
    '''expression_list : expression expression 
    '''
    p[0] = Node(p[1],p[2])

def p_function_declaration(p):
    '''decl_function : FUNC ID LPAR RPAR compound
    '''
    p[0] = Function(p[2],p[5])

def p_compound_expression(p):
    '''compound : LBR expression RBR
    '''
    p[0] = p[2]

def p_empty_compound_expression(p):
    ''' compound : LBR RBR
    '''
    pass

def p_basic_arithmetics(p):
    '''expression : expression PLUS expression
                | expression MINUS expression
                | expression MUL expression
                | expression DIV expression
    '''
    left = p[1]
    right = p[3]
    operator = p[2]
    if operator == "+":
        p[0] = Add(left,right)
    elif operator == "-":
        p[0] = Sub(left,right)
    elif operator == "*":
        p[0] = Mul(left,right)
    elif operator == "/":
        p[0] = Div(left,right)
    else:
        raise AssertionError("Tokenization failure")

def p_assignment(p):
    ''' expression : ID ASSIGN expression
    '''
    left = ID(p[1])
    right = p[3]

    p[0] = Assignment(left,right)

def p_declaration(p):
    ''' expression : VAR ID '''
    p[0] = Declaration(p[2])

def p_number(p):
    'number : NUM'
    p[0] = Number(p[1])

def p_condition(p):
    ''' condition : number EQUAL number 
                    | number GREATER number
                    | number LESSER number
                    | ID EQUAL ID 
                    | ID GREATER ID
                    | ID LESSER ID
    '''
    p[0] = Condition(p[2],p[1],p[3])

def p_conditional(p):
    ''' expression : IF LPAR condition RPAR compound
    '''
    p[0] = Conditional(p[3],p[5])

def p_conditional_expanded(p):
    ''' expression : IF LPAR condition RPAR compound ELSE compound
    '''
    p[0] = Conditional(p[3],p[5],p[7])

def p_error(p):
    if p:
        raise SyntaxError("Syntax error: {0}".format(p))
    else: 
        raise SyntaxError("Unknown syntax at the end of input")

Parser = yacc.yacc(debug=1)
