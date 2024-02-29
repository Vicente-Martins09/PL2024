import re


def main():
    
    texto = """
1iMRE7r=HtzkAon8o2sdXVtM0oLoffzNxZi4t5eqOpZNEqCJaLonK1mMTy3d22W
offaJ8uH6sgDxy2xMJoNRQZ7aAmkmhF4N91eTqqzequb4eYpA34DIojequZtnvw
6LyrPxme0eqZbYZPon82fFbYKoffQXTonOnjjAAzS4=eq1tKe0VQuS89yuoffL
oNCs8rV24P3Eeq1GeAtonjvTK0A5KmKAEaOon1=deqQcZrZ5MBu58HzkequWQ5
XC9Fon83ctoffFHaEQFtN9aIonfjAq9eqW0L6F9W4=eq=2pOQRUgAM56DKoffZ
6BYeq7sYononKZV=eq0K9KdW=VononAid6Uon6GeoffW=onD=OffonEQ=offG=3
9MoNyOn=EQOff7offOn5DSOffOn9OnW=43Uk=OffOnON 7=
"""

    somando = True
    contador = 0
    
    regex= r'(?i)(?P<soma>([+-]?\d+))|(?P<on>on)|(?P<off>off)|(?P<igual>=)'


    for linha in texto.splitlines():
        lista = re.finditer(regex, linha)
        
        for objeto in lista:
            if objeto.lastgroup == 'soma':
                if somando==True:
                    contador += int(objeto.group('soma'))
            
            elif objeto.lastgroup=='on':
                somando=True
            
            elif objeto.lastgroup=='off':
                somando=False
                
            elif objeto.lastgroup=='igual':
                print(contador)
            
    
    
if __name__ == "__main__":
    main()