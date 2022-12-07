# --> Importar bibliotecas <-- #

# Um exemplo muito famoso é a biblioteca "math", utilizada para operações matemáticas.

# Essa biblioteca importa:
# ceil = arredonda pra cima
# floor = arredonda pra baixo
# trunc = elimina da virgula pra frente
# pow = para fazer potenciação
# sqrt = para raiz quadrada
# factorial = fatorar um número

import math 

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
numFinal = math.trunc(raiz)

print('A raiz quadrada de {} é {}'.format(num, math.ceil(numFinal))) # Arredondando pra cima

import random 

n = random.random() # Imprime um numero aleatório
p = random.randint(1, 10) # Imprime um numero inteiro de 1 até 10
print(n)

import emoji

print(emoji.emojize("Olá, Mundo! :earth_americas:"), use_alises=True)