from datetime import date

anoAtual = date.today().year
maior = 0
menor = 0

for pessoa in range(1, 8):
    anoNasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = anoAtual - anoNasc
    if idade >= 18:
        print('Maior de Idade! ')
        maior += 1
    else: 
        print('Menor de idade!')
        menor += 1
        
print('O número de pessoas maior de idade é {}'.format(maior))
print('O número de pessoas menor de idade é {}'.format(menor))


    
