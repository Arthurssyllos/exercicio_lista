listas = input('crie sua lista de nomes: ') #pedindo para o usuario criar a lista

listas = list(map(int, listas.split()))

menor = segundo_menor = float('inf')

for numero in listas:
    if numero < menor:
        segundo_menor = menor
        menor = numero
    elif numero < segundo_menor and numero != menor:
            segundo_menor = numero
print('O segundo maior número da lista é: ', segundo_menor)