salarioInicial = float(input('Qual é o valor do salário do funcionário? '))

aumento = (15/100) * salarioInicial
salarioFinal = salarioInicial + aumento

print('O valor final do salário é de R${}'.format(salarioFinal))