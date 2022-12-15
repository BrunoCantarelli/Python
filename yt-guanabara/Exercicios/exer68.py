import random

parimpar = str(input('Você que ser PAR ou ÍMPAR? ')).strip().upper()
cont = 0

while True:
    escolhaComputador = random.randint(0, 10)
    escolha = int(input('Qual número entre 0 e 10 você escolhe? '))
    soma = escolhaComputador + escolha
    
    if escolha < 0:
        print('Só pode números positivos!!')
    elif parimpar == 'PAR':
        if soma % 2 == 0:
            print('GANHOU!')
            print(f'Você escolheu {escolha} e o computador escolheu {escolhaComputador}!')
            print(f'A soma foi {soma}! Par ganhou!')
            cont += 1
        elif soma % 2 != 0:
            print('PERDEU!')
            break
        
    if escolha < 0:
        print('Só pode números positivos!!')
    elif parimpar == 'IMPAR':
        if soma % 2 != 0:
            print('GANHOU!')
            print(f'Você escolheu {escolha} e o computador escolheu {escolhaComputador}!')
            print(f'A soma foi {soma}! Impar ganhou!')
            cont += 1

        elif soma % 2 == 0:
            print('PERDEU!')
            break

print(f'Você ganhou {cont} vezes do computador.')