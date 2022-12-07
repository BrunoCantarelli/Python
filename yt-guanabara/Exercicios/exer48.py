soma = 0
cont = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        cont += 1 # vai ser o número de valores multiplos de 3
        soma += n

print('A soma de todos os {} valores múltiplos de 3 entre 1 e 500 é {}'.format(cont, soma))