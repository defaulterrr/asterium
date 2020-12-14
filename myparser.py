from rply.token import BaseBox
import string, random
from addresstable import AddressTable

class Number(BaseBox):
    def __init__(self,value):
        self.value = value
        self.address = ""

    def reserve(self):
        """
        Reserve a word
        """
        # <name>: word <word>
        # get unique name
        # self.address = get_random_string()
        # set its value
        # push to name table
        # set self.address = unique name

    def eval(self, addresstable):
        #return self.value
        # self.address = addresstable.push(self.value)
        # print(self.address + " " + "word" + " " + str(self.value) + "\n")
        if self.address != "":
            return self.address
        else:
            self.address = addresstable.push(self.value)
            return self.address

    def generate(self, addresstable):
        return "\n"

class BinaryOperation(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.address = ''


    def eval(self, addresstable):
        # address 1
        # address 2
        # ld A, address1;
        # add A, address2;  // -> a
        # st A, address3;
        # self.resultAddress = get_random_string()
        if self.address != "":
            return self.address
        else:
            self.address = addresstable.push(0)
            return self.address

    def generate(self, addresstable):
        self.cmds = []
        self.left.eval(addresstable)
        self.right.eval(addresstable)
        self.cmds.append(self.left.generate(addresstable))
        self.cmds.append(self.right.generate(addresstable))
        self.cmds.append("ld A," + str(self.left.eval(addresstable)) + ";\n")
        self.cmds.append("add A," + str(self.right.eval(addresstable)) + ";\n")
        self.cmds.append("st A," + str(self.address) + ";\n")
        cmds = "".join(self.cmds)
        return cmds

class Sub(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.address = ''

    def eval(self, addresstable):
        if self.address != "":
            return self.address
        else:
            self.address = addresstable.push(0)
            return self.address
    def generate(self, addresstable):
        self.cmds = []
        self.left.eval(addresstable)
        self.right.eval(addresstable)
        self.cmds.append(self.left.generate(addresstable))
        self.cmds.append(self.right.generate(addresstable))
        self.cmds.append("ld A," + str(self.left.eval(addresstable)) + ";\n")
        self.cmds.append("sub A," + str(self.right.eval(addresstable)) + ";\n")
        self.cmds.append("st A," + str(self.address) + ";\n")
        cmds = "".join(self.cmds)
        return cmds

class Mul(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.address = ''

    def eval(self, addresstable):
        if self.address != "":
            return self.address
        else:
            self.address = addresstable.push(0)
            return self.address

    def generate(self, addresstable):
        self.cmds = []
        self.left.eval(addresstable)
        self.right.eval(addresstable)
        self.cmds.append(self.left.generate(addresstable))
        self.cmds.append(self.right.generate(addresstable))
        self.cmds.append("ld A," + str(self.left.eval(addresstable)) + ";\n")
        self.cmds.append("mul A," + str(self.right.eval(addresstable)) + ";\n")
        self.cmds.append("st A," + str(self.address) + ";\n")
        cmds = "".join(self.cmds)
        return cmds

class Div(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.address = ''

    def eval(self, addresstable):
        if self.address != "":
            return self.address
        else:
            self.address = addresstable.push(0)
            return self.address

    def generate(self, addresstable):
        self.cmds = []
        self.left.eval(addresstable)
        self.right.eval(addresstable)
        self.cmds.append(self.left.generate(addresstable))
        self.cmds.append(self.right.generate(addresstable))
        self.cmds.append("ld A," + str(self.left.eval(addresstable)) + ";\n")
        self.cmds.append("div A," + str(self.right.eval(addresstable)) + ";\n")
        self.cmds.append("st A," + str(self.address) + ";\n")
        print(self.cmds)
        cmds = "".join(self.cmds)
        return cmds


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
