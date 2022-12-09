print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

chute = 0
numero_secreto = 42
total_de_tentativas = 0

while (chute != numero_secreto and total_de_tentativas >= 0):
    chute_str = input("Digite o seu número: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
    
    total_de_tentativas += 1

    print("Fim do jogo")
print('O total de tentativas foi {}'.format(total_de_tentativas))