import ply.lex as lex


tokens=(
    "INTERROGACAO",
    "EXCLAMACAO",
    "IGUAL",
    "MULTIPLICACAO",
    "DIVISAO",
    "SOMA",
    "SUBTRACAO",
    "PARE",
    "PARD",
    "NUMBER"
    "ID"
)

t_INTERROGACAO = r'\?'
t_EXCLAMACAO= r'!'
t_IGUAL=r'='
t_MULTIPLICACAO = r'\*'
t_DIVISAO= r'/'
t_SOMA=r'\+'
t_SUBTRACAO=r'-'
t_PARE=r'\('
t_PARD=r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z]\w*'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()