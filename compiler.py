from lexer import Lexer
from parser import Parser

input = '3+(3/6)*9'

lexer = Lexer().get_lexer()
tokens = lexer.lex(input)
pg = Parser()
pg.parse()
parser = pg.getParser()

result = parser.parse(tokens)
print(result.eval())