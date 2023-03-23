listas = input('crie sua lista: ') 

listas = list(map(int, listas.split()))

menor = [num for num in listas if num < 5]

print('Os números menores que 5 são: ',menor)