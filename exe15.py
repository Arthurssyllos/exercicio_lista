listas = input('crie sua lista: ') #pedindo para o usuario criar a lista

listas = list(map(int, listas.split()))

# Criando uma lista com elementos duplicados
lista_com_duplicatas = listas

# Inicializando uma lista vazia para armazenar os elementos únicos
lista_sem_duplicatas = []

# Usando um loop While para percorrer a lista e remover os elementos duplicados
while lista_com_duplicatas:
    elemento = lista_com_duplicatas.pop(0) # pop é usado para remover o elemento
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento) # append é usado para adicionar na lista
        
# Imprimindo o resultado
print('A lista sem duplicatas é:', lista_sem_duplicatas)