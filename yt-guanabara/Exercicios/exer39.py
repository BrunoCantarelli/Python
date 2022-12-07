anoNasc = int(input('Em que ano voê nasceu? '))
anoAtual = int(input('Qual é o ano atual? '))
idade = anoAtual - anoNasc

if idade < 18:
    print('Você terá que se alistar futuramente!')
    print('Falta {} anos para seu alistamento'.format(18 - idade))
elif idade == 18:
    print('Você precisa se alistar esse ano!')
elif idade > 18:
    print('O tempo para se alistar já passou!') 
    print('Você está atrasado {} ano(s)!'.format(idade - 18))