listas = input('crie sua lista: ') #pedindo para o usuario criar a lista

listas = list(map(str, listas.split()))

mais_longo = max(listas, key=len)
mais_curto = min(listas, key=len)

print('O nome mais longo é: ' ,mais_longo, 'e o nome mais curto é: ' ,mais_curto)