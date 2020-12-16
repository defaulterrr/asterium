from Core.Library import Number,Add,Sub,Mul,Div
import string, random
from Core.Library import AddressTable

from rply import ParserGenerator


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
        ['add','sub','mul','div','OPEN_PAR','CLOSE_PAR','OPEN_BRACKET','CLOSE_BRACKET','NUM'],
        precedence=[
            ('left',['add','sub']),
            ('right',['mul','div'])
        ]
        )

    def parse(self):
        @self.pg.production('expression : NUM')
        def expression_num(p):
            #print(p[0])
            return Number(int(p[0].getstr()))

        @self.pg.production('expression : OPEN_PAR expression CLOSE_PAR')
        def expression_parentheses(p):
            #print(p[1])

            return p[1]

        @self.pg.production('expression : OPEN_BRACKET expression CLOSE_BRACKET')
        def expression_bracket(p):
            #print(p[1])

            return p[1]

        @self.pg.production('expression : expression add expression')
        @self.pg.production('expression : expression sub expression')
        @self.pg.production('expression : expression mul expression')
        @self.pg.production('expression : expression div expression')
        def expression_basic_arithmetics(p):
            left = p[0]
            right =  p[2]
            operator = p[1]
           #print(p[1])

            tokentype = operator.gettokentype()
            if tokentype == "add":
                return Add(left,right)
            elif tokentype == "sub":
                return Sub(left,right)
            elif tokentype == "mul":
                return Mul(left,right)
            elif tokentype  == "div":
                return Div(left,right)
            else:
                raise AssertionError("Undefined token")

        @self.pg.error
        def error_handler(token):
            raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

    def getParser(self):
        return self.pg.build()
