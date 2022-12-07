v = float(input('Qual é a velociade do carro? '))
multa = (v - 80) * 7

if v > 80:
    print('Você ultrapassou a velocidade limite. Você recebeu uma multa!')
    print('A multa é de R${}'.format(multa))
else: 
    print('Você está dentro da velocidade permitida, continue assim!')