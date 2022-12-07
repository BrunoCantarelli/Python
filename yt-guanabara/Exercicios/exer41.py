anoNasc = int(input('Em que ano você nasceu? '))
anoAtual = int(input('Em que ano estamos? '))
idade = anoAtual - anoNasc

if idade <= 9:
    print('MIRIM!')
elif idade >= 10 and idade <= 14:
    print('INFANTIL!')
elif idade >= 15 and idade <= 19:
    print('JUNIOR!')
elif idade == 20:
    print('SÊNIOR!')
elif idade > 20:
    print('MASTER!')
