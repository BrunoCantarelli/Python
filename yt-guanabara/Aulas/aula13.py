# Laços de repetição

# for c in range(0, 6): # range(0, 6) = 0, 1, 2, 3, 4, 5
#     print(c)
# print('Fim') 

# print('=-=' * 10)

# for c in range(6, 0, -1): # Contagem regressiva
#     print(c)
# print('Fim') 

# print('=-=' * 10)

# for c in range(0, 7, 2): # 0, 2, 4, 6
#     print(c)
# print('Fim') 

n1 = int(input('Digite um número: '))
for c in range(0, n1):
    print(c)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
    
s = 0

for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))


