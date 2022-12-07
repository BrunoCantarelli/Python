num = int(input('Digite um número para saber a sua tabuada: '))

for i in range(1, 11):
    print('{} x {} = {}'.format(num, i, num * i))