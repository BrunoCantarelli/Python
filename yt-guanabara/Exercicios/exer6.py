from math import sqrt # Biblioteca para poder utilizar elementos para auxiliar em contas matemáticas, como por exemplo raiz quadrada que está sendo importada

num1 = int(input('Digite um número: '))
raiz = math.sqrt(num1)

print('O dobro do número digitado é: {}'.format(num1 * 2))
print('O tripo do número digitado é: {}'.format(num1 * 3))
print('A raiz quadrada desse número é: {:.3f}'.format(raiz))