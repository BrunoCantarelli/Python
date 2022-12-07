nome = str(input('Digite seu nome: ')).strip()

print(nome.lower())
print(nome.upper())
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

