# Condições 

# nome = str(input('Qual é seu nome? '))

# if nome == 'Bruno':
#     print('Que nome lindo você tem {}!'.format(nome))
# else:
#     print('Você não se chama Bruno!')
    
# print('Bem vindo(a)!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) / 2

print('A sua media foi {:.1f}'.format(m))

if (m > 6.9):
    print('Você passou! Parabéns!')
else: 
    print('Infelizmente você não passou de ano.')
    
# Podemos representar de outra forma mais simples também.

print('Aproveite a suas férias!' if m > 6.9 else 'Você não conseguiu, estude mais!')
    


