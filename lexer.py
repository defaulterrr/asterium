from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('add',r'\+')
        self.lexer.add('sub',r'\-')
        self.lexer.add('mul',r'\*')
        self.lexer.add('div',r'\/')
        self.lexer.add('OPEN_PAR',r'\(')
        self.lexer.add('CLOSE_PAR',r'\)')
        self.lexer.add('OPEN_BRACKET',r'\{')
        self.lexer.add('CLOSE_BRACKET',r'\}')
        self.lexer.add('NUM', r'\d+')
        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()