import random

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('   Bem Vindo(a) ao jogo!!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

tentativas = 1
chute = 0
aleatorio = 1

while chute != aleatorio:
    chute = int(input('Chute um número de 0 a 10: '))
    aleatorio = random.randint(0,10)

    if aleatorio == chute:
        print('Parabéns, você adivinhou! O número correto era {}'.format(aleatorio))
    else: 
        print('Infelizmento você errou! O número correto era {}'.format(aleatorio))
        tentativas += 1

print('Você precisou de {} tentativas para acertar o número!'.format(tentativas))   