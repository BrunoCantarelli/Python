genero = str(input('Qual é seu sexo [M / F]? ')).upper().strip()[0]
print(genero)

while genero == 'M' or genero == 'F':
    print(genero)
    
print('Informações aceitas!')