media = 0
soma = 0
maiorIdade = -999
nomevelho = ''
mulher20 = 0


for n in range(1, 5):
    nome = str(input('Qual é nome da {}ª pessoa? '.format(n)))
    idade = int(input('Quantos anos a {}ª pessoa tem? '.format(n)))
    genero = str(input('Qual é o gênero da {}ª pessoa (Feminino, Masculino ou Outro)?  '.format(n))).upper()
    soma += idade
    media = soma / 4
    if idade > maiorIdade:
        maiorIdade = idade
        nomevelho = nome
    if idade > 20 and genero == 'FEMININO':
        mulher20 += mulher20 + 1 
        
print('O grupo tem a média de idade de {} anos'.format(media))
print('A pessoa mais velha do grupo é {} com {} anos'.format(nomevelho, maiorIdade))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(mulher20))
    