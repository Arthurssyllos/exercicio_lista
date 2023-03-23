listas = input('crie sua lista: ') #pedindo para o usuario criar a lista

listas = list(map(int, listas.split())) #definindo a lista em inteira e para dar espaço

soma = sum(listas)

quantidade = len(listas)

total = soma / quantidade

print(total)