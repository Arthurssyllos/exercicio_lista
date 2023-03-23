listas = input('crie sua lista: ') #pedindo para o usuario criar a lista

listas = list(map(str, listas.split()))

palavras_impares = []

for palavra in listas:
    if len(palavra) % 2 != 0:
        palavras_impares.append(palavra)
        
print(f'As palavras com número ímpar de letras são:', palavras_impares)