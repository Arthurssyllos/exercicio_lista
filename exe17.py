listas = input('crie sua lista: ') #pedindo para o usuario criar a lista

listas = list(map(str, listas.split()))

nomes_com_e = []

for nome in listas:
    if "e" in nome:
        nomes_com_e.append(nome)
print('Os nomes que contêm a letra "e" são: ', nomes_com_e )