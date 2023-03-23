listas = input('crie sua lista: ') #pedindo para o usuario criar a lista

listas = list(map(int, listas.split()))


sort = sorted(listas, reverse = True)

print(sort)