def contaPares(lista): #funcao lista
    pares = 0
    impares = 0 #comeca com 0
    for num in lista:
        if (num % 2) == 0: #numeros pares
            pares = pares + 1
        else:
            impares = impares + 1 #numeros impares
    return pares, impares

lista = list() 

q = int(input('Quantos valores haverá na lista ? '))
while q < 0:
    print('Erro')
    q = int(input('Quantos valores haverá na lista ? '))

for c in range(q):
    num = int(input('Valor:'))
    lista.append(num)

print('A quantidade de valores pares e impares são, respectivamente:',contaPares(lista))