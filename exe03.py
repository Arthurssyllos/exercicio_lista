listas = input('insira uma lista de numeros: ')

listas = list(map(int, listas.split()))

maximo = max(listas)
minimo = min(listas)

print('O número máximo da sua lista é: ', maximo,  'E o número mínimo da sua lista é: ', minimo)
