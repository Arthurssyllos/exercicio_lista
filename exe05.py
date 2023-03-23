listas = input('crie sua lista: ') #pedindo para o usuario criar a lista

listas = list(map(int, listas.split()))

listas.sort()

print(listas)