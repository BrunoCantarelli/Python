salario = float(input('Qual é seu salario? '))
aumento10 = (10/100) * salario
aumento15 = (15/100) * salario
salarioFinal10 = salario + aumento10
salarioFinal15 = salario + aumento15


if salario > 1250:
    print('Seu salario teve aumento de 10%, com isso passou a ser R${}'.format(salarioFinal10))
if salario <= 1250:
    print('Seu salario teve aumento de 15%, com isso passou a ser R${}'.format(salarioFinal15))