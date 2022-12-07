distancia = float(input('Qual a distância da viagem? '))
valor1 = 0.50
valor2 = 0.45

if distancia <= 200:
    print('O preço a pagar vai ser R${}'.format(valor1 * distancia))
if distancia > 200:
    print('O preço a pagr vai ser R${}'.format(valor2 * distancia))