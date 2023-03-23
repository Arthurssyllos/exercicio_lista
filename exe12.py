listas = input('crie sua lista de nomes: ') #pedindo para o usuario criar a lista

listas = list(map(str, listas.split()))

pesquisanome = input('Consulte seu nome: ') #pedindo para o usuario colocar apenas um nome

len(listas)

if pesquisanome in listas:
    print('O nome está na lista!', pesquisanome.capitalize())
else:
    print('O nome não está na lista :( ')
