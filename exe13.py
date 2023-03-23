listas = input('crie sua lista de nomes: ') #pedindo para o usuario criar a lista

listas = list(map(int, listas.split()))

maior = segundo_maior = float('-inf')

for numero in listas:
    if numero > maior:
        segundo_maior = maior
        maior = numero
    elif numero > segundo_maior and numero != maior:
            segundo_maior = numero
print('O segundo maior número da lista é: ', segundo_maior)