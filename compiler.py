from lexer import Lexer
from parser import Parser

input = """
4+4*9/10
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(input)
pg = Parser()
pg.parse()
parser = pg.getParser()

for token  in tokens:
    print(token)

parser.parse(tokens).eval()