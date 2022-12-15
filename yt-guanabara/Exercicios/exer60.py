from math import factorial

num = int(input('Digite um número: '))
fatorial = factorial(num)

while num < 0:
    num = int(input('Digite um número: '))
    
print('O fatorial de {} é {}.'.format(num, fatorial))
    

