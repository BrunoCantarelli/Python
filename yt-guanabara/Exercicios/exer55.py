cont = 0
maior = 0
menor = 0

for n in range(1, 6):
    peso = float(input('Qual é o peso da {}ª pesssoa? '.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    
print('Maior peso: {}'.format(maior))
print('Menor peso: {}'.format(menor))
    