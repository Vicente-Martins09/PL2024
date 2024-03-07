import ply.lex as lex

tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'IDENTIFIER',
    'NUMBER',
    'OPERATOR',
    'COMMA', 
)

t_SELECT = r'(?i)Select'
t_FROM = r'(?i)From'
t_WHERE = r'(?i)Where'
t_OPERATOR = r'>=|<=|>|<|='
t_COMMA = r','
t_IDENTIFIER = r'\b\w+\b'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
    
    
def  main():
    
    lexer=  lex.lex()
    query = "Select id, nome, salario From empregados Where salario >= 820"
    lexer.input(query)
    
    for tok in iter(lexer.token, None):
        print(tok)



if __name__=='__main__':
    main()