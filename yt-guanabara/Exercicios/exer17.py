import math

# c1 = int(input('Digite o valor do cateto 1: '))
# c2 = int(input('Digite o valor do cateto 2: '))
# h = (pow(c1,2)) + (pow(c2, 2))


# print('O valor da hipotenusa é {}.'.format(sqrt(h)))

ca = int(input('Digite o valor do cateto adjacente: '))
co = int(input('Digite o valor do cateto oposto: '))
h = math.hypot(ca, co)
print('O valor da hipotenusa é {}.'.format(h))