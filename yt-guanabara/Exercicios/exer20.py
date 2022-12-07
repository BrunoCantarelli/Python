import random

pessoa1 = str(input('Digite o nome da primeira pessoa: '))
pessoa2 = str(input('Digite o nome da segunda pessoa: '))
pessoa3 = str(input('Digite o nome da terceira pessoa: '))
pessoa4 = str(input('Digite o nome da quarta pessoa: '))

lista = [pessoa1, pessoa2, pessoa3, pessoa4]
ordem = random.shuffle(lista)

print('A ordem ficou {}'.format(ordem))
