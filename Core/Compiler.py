from Lexer import Lexer
from Parser import Parser
from Library import AddressTable

input = '1/0*999-521456*83/7'

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