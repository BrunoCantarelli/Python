genero = str(input('Qual é seu sexo [M / F]? ')).upper().strip()[0]

while genero not in 'MF':
    genero = str(input('Dados inválidos, por favor insira seu sexo [M / F]? ')).upper().strip()[0]

if genero == 'M' or genero == 'm':
    genero = 'Masculino'
elif genero == 'F' or genero == 'f':
    genero = 'Feminino'
    
print('Informações aceitas!')   
print('Você é do sexo {}.'.format(genero))