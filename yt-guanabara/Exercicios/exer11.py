altura = float(input('Qual é a altura da parede? '))
largura = float(input('Qual é a largura da parede? '))
area = altura * largura
qtdTinta = area / 2

print('Você precisa de {} litros para pintar essa parede!'.format(qtdTinta))
