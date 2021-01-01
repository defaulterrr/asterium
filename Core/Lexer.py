import ply.lex as lex

reserved = {
    'var'   : 'VAR',
    'func'  : 'FUNC',
    '=='    :'EQUAL',
    '='     :'ASSIGN',
    '>'     :'GREATER',
    '<'     :'LESSER',
    'if'    :'IF',
    'else'  :'ELSE'
}

tokens = [
    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'LPAR',
    'RPAR',
    'LBR',
    'RBR',

    'NUM',
    'ID',
    'SMCLN'
] + list(reserved.values())

t_PLUS  = r'\+'
t_MINUS = r'\-'
t_MUL   = r'\*'
t_DIV   = r'\/'
t_LPAR  = r'\('
t_RPAR  = r'\)'
t_LBR   = r'\{'
t_RBR   = r'\}'
t_SMCLN = r'\;'
t_NUM   = r'\d+'
t_GREATER = r'\>'
t_LESSER = r'\<'

def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_EQUAL(t):
    r'=='
    return t

def t_ASSIGN(t):
    r'='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    raise ValueError("Unknown token {0}".format(t.value))

lexer = lex.lex()

# data = '''
# func space() {3 < == > if 4}
# '''

# lexer.input(data)
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)


