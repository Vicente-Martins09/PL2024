
atletasAptos=0
atletasInaptos=0
modalidades= []
escaloes={}

with open('emd.csv', 'r') as  ficheiro:
    linhas= ficheiro.readlines()[1:]
    
for linha in linhas:
    campo=linha.split(',')
    
    
    if campo[12]=='true\n': atletasAptos +=1
    else: atletasInaptos +=1
    

    if campo[8] not in modalidades:
        modalidades.append(campo[8])
    
    
    idade = int(campo[5])
    intrevalo = idade // 5
    
    if intrevalo in escaloes:
        escaloes[intrevalo] +=1
    else: 
        escaloes[intrevalo]=1
    
    

escaloes = dict(sorted(escaloes.items()))
modalidades=sorted(modalidades)

print('\nResultados:\n')
print(f'Número total de atletas: {atletasAptos+atletasInaptos}')
print(f'Número de atletas Aptos: {atletasAptos} ({round(100*(atletasAptos /(atletasAptos+atletasInaptos)),2)}%)')
print(f'Número de atletas Inaptos: {atletasInaptos} ({round(100*(atletasInaptos /(atletasAptos+atletasInaptos)),2)}%)')

print(f'\nIntrevalo de idades:')
for key in escaloes:
    print(f'[{key*5}...{key*5 + 4}] = {escaloes[key]}')

print('\nLista de Modalidades:')
print(modalidades)