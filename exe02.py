q = int(input('Quantos letras haverá na lista ? ')) #variavel para dizer quantas letras vai ter na lista
letra = [] #lista vazia

for c in range(q): #entrar no loop
    letra = input('Insira as letras: ')
for letras in letra:
    if letra.startswith('a') or letra.startswith('A'):
        print('As palavras que iniciam com a letra "a", respectivamente: ', letra)