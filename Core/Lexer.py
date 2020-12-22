from rply import LexerGenerator
class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('add', r'\+')
        self.lexer.add('sub', r'\-')
        self.lexer.add('mul', r'\*')
        self.lexer.add('div', r'\/')
        self.lexer.add('OPEN_PAR', r'\(')
        self.lexer.add('CLOSE_PAR', r'\)')
        self.lexer.add('OPEN_BRACKET', r'\{')
        self.lexer.add('CLOSE_BRACKET', r'\}')
        self.lexer.add('NUM', r'\d+')
        self.lexer.add('VAR_DECL', r'\bvar\b')
        self.lexer.add('FUNC_DECL', r'\bfunc\b')
        self.lexer.add('ID', r'\w+')
        self.lexer.add('ASSIGNMENT', r'\=')
        self.lexer.add('SEMICOLON', r'\;')

        self.lexer.add('GREATER',r'\>')
        self.lexer.add('EQUAL',r'\b==\b')
        self.lexer.add('LESSER', r'\<')
        self.lexer.add('IF', r'\bif\b')

        self.lexer.add('FOREACH',r'\bforeach\b')
        self.lexer.add('PRINT',r'\bprint\b')
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()


