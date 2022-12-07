import random

al1 = str(input('Qual o nome do aluno 1: '))
al2 = str(input('Qual o nome do aluno 2: '))
al3 = str(input('Qual o nome do aluno 3: '))
al4 = str(input('Qual o nome do aluno 4: '))
alunos = [al1, al2, al3, al4] 
sorteado = random.choice(alunos)

print('O aluno sorteado foi {}!'.format(sorteado))