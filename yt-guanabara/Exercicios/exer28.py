import random

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('   Bem Vindo(a) ao jogo!!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


chute = int(input('Chute um número de 0 a 5: '))
aleatorio = random.randint(0,5)

if aleatorio == chute:
    print('Parabéns, você adivinhou!')
else: 
    print('Infelizmento você errou! O número correto era {}'.format(aleatorio))



