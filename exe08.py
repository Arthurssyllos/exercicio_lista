# Tentativa 01:

#listas = input('crie sua lista: ') #pedindo para o usuario criar a lista

#listas = list(map(int, listas.split()))

#for numero in range(listas):
    #if numero > 10:
       # print('Seu número é maior que 10!', numero)
   # elif numero <= 10:
       # print('NÃO VOU EXIBIR ANDERSON!!!!')
    

#ou pode ser assim

listas = input('crie sua lista: ') #pedindo para o usuario criar a lista

listas = list(map(int, listas.split()))

maior = [num for num in listas if num > 10]

print('Os números maiores que 10 são: ',maior)