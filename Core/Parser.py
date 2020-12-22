from Library.Number import Number
from Library.Add import Add
from Library.Sub import Sub
from Library.Mul import Mul
from Library.Div import Div
from Library.Assignment import Assignment
from Library.ID import ID
from Library.Declaration import Declaration
from Library.Function import Function
import string
import random
from Library.AddressTable import AddressTable
from Library.Node import Node

from rply import ParserGenerator


class Parser():
    def __init__(self, debug=False):
        self.pg = ParserGenerator(
            ['add', 'sub', 'mul', 'div', 'OPEN_PAR', 'CLOSE_PAR', 'OPEN_BRACKET',
                'CLOSE_BRACKET', 'NUM', 'ID', 'ASSIGNMENT', 'SEMICOLON', 'VAR_DECL',
                    'FUNC_DECL', 'GREATER', 'EQUAL', 'LESSER', 'IF'],
            precedence=[
                ('left', ['ASSIGNMENT']),
                ('left', ['FUNC_DECL']),
                ('left', ['add', 'sub']),
                ('left', ['expression_list','expression']),
                ('left', ['GREATER','EQUAL','LESSER']),
                ('right', ['mul', 'div']),
            ]
        )
        self.debug = debug

    def parse(self):

        
        @self.pg.production('expression : expression SEMICOLON')
        def expr_list(p):
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got an expression")
                print(p)
            return p[0]

        @self.pg.production('expression : function')
        def func_expr(p):
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got function expression")
                print(p)
            return p[0]

        @self.pg.production('expression : function expression')
        def func_node(p):
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got function node")
                print(p)
            return Node(p[0],p[1])

        @self.pg.production('expression : expression_list')
        def expr_list(p):
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got expression from list")
                print(p)
            return p[0]

        @self.pg.production('expression_list : expression_list expression')
        def expr_list_long(p):
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got prolonged expression list")
                print(p)
            return Node(p[1],p[0])

        @self.pg.production('expression_list : expression expression')
        def expr_list_basic(p):
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got init expression list")
            return Node(p[0],p[1])

        @self.pg.production('expression : FUNC_DECL ID OPEN_PAR CLOSE_PAR OPEN_BRACKET expression CLOSE_BRACKET')
        def function(p):
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got a function")
                print(p[0])
            print(p[3])
            return Function(p[1].getstr(),p[5])

        @self.pg.production('function : FUNC_DECL ID OPEN_PAR expression CLOSE_PAR compound_expression')
        def function(p):
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got a function")
                print(p[0])
            print(p[3])
            return Function(p[1].getstr(),p[6])

        @self.pg.production('expression : NUM')
        def expression_num(p):
            # print(p[0])
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got numeric expression")
                print(p)
            return Number(int(p[0].getstr()))

        @self.pg.production('expression : OPEN_PAR expression CLOSE_PAR')
        def expression_parentheses(p):
            # print(p[1])
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got parentheses expression")
                print(p)
            return p[1]

        @self.pg.production('expression : OPEN_BRACKET expression CLOSE_BRACKET')
        def expression_bracket(p):
            # print(p[1])

            return p[1]


        # __________________
        #   ARITHMETICS
        # ------------------

        @self.pg.production('expression : expression add expression')
        @self.pg.production('expression : expression sub expression')
        @self.pg.production('expression : expression mul expression')
        @self.pg.production('expression : expression div expression')
        def expression_basic_arithmetics(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got elementary arithmetic expression")
                print(p)

            tokentype = operator.gettokentype()
            if tokentype == "add":
                return Add(left, right)
            elif tokentype == "sub":
                return Sub(left, right)
            elif tokentype == "mul":
                return Mul(left, right)
            elif tokentype == "div":
                return Div(left, right)
            else:
                raise AssertionError("Undefined token")

        # __________________
        #   LOGICAL
        # ------------------
        @self.pg.production('conditional : IF logical ')
        def logic_conditional(p):
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got logical expression: conditional block")
                print(p)
            pass

        # GREATER THAN
        @self.pg.production('logical : expression GREATER expression')
        def logic_greater_num(p):
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got logical expression: greater than")
                print(p)
            pass

        # EQUAL TO
        @self.pg.production('expression : NUM EQUAL NUM')
        def logic_equal_num(p):
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got logical expression: equal to")
                print(p)
            pass

        # LESSER THAN
        @self.pg.production('expression : NUM LESSER NUM')
        def logic_lesser_num(p):
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got logical expression: lesser than")
                print(p)
            pass

        

        @self.pg.production('expression : ID ASSIGNMENT expression ')
        def assignment(p):
            left = ID(p[0])
            right = p[2]

            if self.debug:
                print("PARSER_DEBUG ----->>>> Got assignment expression")
                print(p)

            return Assignment(left, right)

        @self.pg.production('expression : VAR_DECL ID')
        def declaration(p):
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got declaration expression")
                print(p)
            name = p[1].getstr()
            return Declaration(name)


        @self.pg.production('compound_expression : OPEN_BRACKET expression_list CLOSE_BRACKET')
        def comp_expr(p):
            if self.debug:
                print("PARSER_DEBUG ----->>>> Got compound expression")
                print(p)
            return p[1]

        @self.pg.error
        def error_handler(token):
            raise ValueError(
                "Ran into a %s:%s where it wasn't expected" % (token.gettokentype(),token.getstr()))

    def getParser(self):
        return self.pg.build()
