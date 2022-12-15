import random

pedra = 'PEDRA'
papel = 'PAPEL'
tesoura = 'TESOURA'

print('x' * 20)
print('       JoKenPo')
print('x' * 20)

print(' ')

while escolha == escolhaComputador:
    escolha = str(input('Escolha entre PEDRA, PAPEL ou TESOURA: ')).upper().strip()
    escolhaComputador = random.choice([pedra, papel, tesoura])

    if escolha == pedra and escolhaComputador == pedra:
        print('Empate, o computador também escolheu Pedra!')
    elif escolha == papel and escolhaComputador == papel: 
        print('Empate, o computador também escolheu Papel!')
    elif escolha == tesoura and escolhaComputador == tesoura:
        print('Empate, o computador também escolheu Tesoura!')
    elif escolha == pedra and escolhaComputador == tesoura:
        print('Parabéns, você ganhou! O computador escolheu Tesoura!')
    elif escolha == pedra and escolhaComputador == papel:
        print('Você perdeu! O computador escolheu Papel!')
    elif escolha == papel and escolhaComputador == tesoura:
        print('Você perdeu! O computador escolheu Tesoura!')
    elif escolha == papel and escolhaComputador == pedra:
        print('Parabéns, você ganhou! O computador escolheu Pedra!')
    elif escolha == tesoura and escolhaComputador == papel:
        print('Parabéns, você ganhou! O computador escolheu Papel!')
    elif escolha == tesoura and escolhaComputador == pedra:
        print('Você perdeu! O computador escolheu Pedra!')
