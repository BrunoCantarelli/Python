nome = input('Qual é seu nome? ')
peso = input('Qual é seu é seu peso? ')

ano_nascimento = int(input('Em que ano você nasceu? '))
ano_atual = int(input('Em que ano estamos? '))

idade = (ano_atual - ano_nascimento)

print('Seu nome é', nome, '!', 'você tem', idade, 'anos', 'e está atualmente pesando', peso, 'Kg')