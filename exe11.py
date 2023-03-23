listas = input('crie sua lista: ') #pedindo para o usuario criar a lista

listas = list(map(int, listas.split()))

soma = 0 #declarando variavel e que tem valor nulo no comeco

for num in listas: #loop
    if num % 2 != 0: 
        soma += num
        
print('A soma dos números ímpares são: ', soma)