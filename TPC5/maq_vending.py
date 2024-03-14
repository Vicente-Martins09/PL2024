import json
import ply.lex as lex
import sys
from datetime import datetime as time
import re
    
tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR',
)

t_LISTAR = r'(?i)LISTAR'
t_SAIR = r'(?i)SAIR'

def t_MOEDA(t):
    r'MOEDA (\s*\d+e,?\s*|\s*\d+c,?\s*)+.*'
    return t

def t_SELECIONAR (t):
    r'SELECIONAR\s+A\d+'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)



def printaSaldo(saldo_euros, saldo_centimos):
    
    if (saldo_euros ==0 and saldo_centimos==0):
        print("maq: Saldo 0")
    elif (saldo_euros ==0 and saldo_centimos!=0):
        print(f"maq: Saldo {saldo_centimos}c")
    elif (saldo_euros !=0 and saldo_centimos==0):
        print(f"maq: Saldo {saldo_euros}e")
    else:
        print(f"maq: Saldo {saldo_euros}e{saldo_centimos}c") 
    
    
       
def adicionarMoeda(token, saldo_euros, saldo_centimos):
    valor_moeda = {'e': 100, 'c': 1}
    saldo = saldo_euros * 100 + saldo_centimos
    match_moedas = re.findall(r'\d+[ec]', token.value)
    for moeda in match_moedas:
        quantidade = int(moeda[:-1])
        unidade = moeda[-1]
        if unidade not in valor_moeda:
            print(f"Unidade de moeda inválida: {unidade}")
            continue
        saldo += quantidade * valor_moeda[unidade]
    saldo_euros = saldo // 100
    saldo_centimos = saldo % 100
    return saldo_euros, saldo_centimos

def imprimir_Lista(stock):
    print("cod | nome | quantidade | preço")
    print("---------------------------------")
    for produto in stock:
        print(f"{produto['cod']}  {produto['nome']}     {produto['quant']}     {produto['preco']}")
        
def selecionar_produto(stock, saldo_euros, saldo_centimos, token):
    codigo_match = re.search(r'A\d+', token.value)
    if codigo_match:
        codigo = codigo_match.group()  # Extrai o código do produto
        for produto in stock:
            if produto['cod'] == codigo:
                if produto['quant'] > 0 and saldo_euros * 100 + saldo_centimos >= int(produto['preco']*100):
                    produto['quant'] -= 1
                    saldo = saldo_euros * 100 + saldo_centimos - int(produto['preco']*100)
                    saldo_euros = saldo // 100
                    saldo_centimos = saldo % 100
                    print(f"maq: Pode retirar o produto dispensado: {produto['nome']}")
                    printaSaldo(saldo_euros, saldo_centimos)
                    return saldo_euros, saldo_centimos
                elif produto['quant'] == 0:
                    print("maq: Produto esgotado.")
                else:
                    print("maq: Saldo insuficiente para satisfazer o seu pedido.")
                break
        else:
            print("maq: Produto não encontrado.")
    else:
        print("maq: Código do produto inválido.")
    return saldo_euros, saldo_centimos





with open("stock.json", "r") as file:
    stockData = json.load(file)['stock']

for produto in stockData:
    produto['quant'] = int(produto['quant'])
    produto['preco'] = float(produto['preco'])


print(f"maq: {time.now().date()}, Stock carregado, Estado atualizado.")
print("maq: Bom dia. Estou disponível para atender o seu pedido.")

saldo=0
saldo_euros = 0
saldo_centimos = 0

lexer= lex.lex()

for line in sys.stdin:    
    
    lexer.input(line)
    
    for token in lexer:
        print(token)
        if token.type == 'MOEDA':
            saldo_euros, saldo_centimos = adicionarMoeda(token, saldo_euros, saldo_centimos)
            printaSaldo(saldo_euros, saldo_centimos)
        
        
        elif token.type == 'SAIR':
            if saldo_euros > 0 or saldo_centimos > 0:
                print(f"maq: Pode retirar o troco = {saldo_euros}e{saldo_centimos}c")
            print("maq: Até à próxima.")
                
            with open('stock.json', 'w') as file:
                json.dump({"stock": stockData}, file, indent=4)
            sys.exit()
        
        
        elif token.type == 'LISTAR':
            imprimir_Lista(stockData)
        
        
        elif token.type == 'SELECIONAR':
            saldo_euros, saldo_centimos = selecionar_produto(stockData, saldo_euros, saldo_centimos, token)
        else:
            print("maq: Comando inválido.")