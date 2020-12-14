from lexer import Lexer
from myparser import Parser
from addresstable import AddressTable

input = '666*15/3-13000'

table = AddressTable()

lexer = Lexer().get_lexer()
tokens = lexer.lex(input)
pg = Parser()
pg.parse()
parser = pg.getParser()

result = parser.parse(tokens)
result.eval(table)
print(result.generate(table))
print(table.generate())