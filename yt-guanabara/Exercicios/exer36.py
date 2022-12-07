vcasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você quer pagar? '))
prestacao = vcasa / (anos * 12)
minimoprestacao = (30/100) * salario

print('Para pagar uma casa de R${:.2f} em {} anos'.format(vcasa, anos), end='')
print(' A prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimoprestacao:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
 