from Lexer import Lexer
from Parser import Parser
from Library.AddressTable import AddressTable

input = '1/0*999-521456*83/7'

table = AddressTable()

lexer = Lexer().get_lexer()
tokens = lexer.lex(input)
pg = Parser()
pg.parse()
parser = pg.getParser()

tree = parser.parse(tokens)
tree.eval(table)
print("main: start 0")

print(tree.generate(table))
print(table.generate())