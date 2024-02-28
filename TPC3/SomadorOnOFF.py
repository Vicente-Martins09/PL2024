import re


def main():
    
    texto = """
1 4 6  5 off 2 4 6 8 on
-5 -5 7 7 = OFF 1  3 = 5 6 ON 23
1 2 Off 34 5 45 On 8 =
"""

    somando = True
    contador = 0
    
    regexON= r'(?i)on'
    regexOFF= r'(?i)off'
    regexInt= r'[+-]?\d+'


    for linha in texto.splitlines():
        for palavra in linha.split():
            if (re.fullmatch(regexOFF,palavra)):
                somando = False
            if (re.fullmatch(regexON,palavra)):
                somando = True
            if (re.fullmatch(regexInt,palavra)):
                if somando is True:
                    contador += int(palavra)
            if (palavra=='='):
                print(contador)

    
    
if __name__ == "__main__":
    main()