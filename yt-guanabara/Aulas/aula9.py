# Strings

frase = 'Curso em Vídeo'

# FATIAMENTO

# Exemplos:


# frase = 'C u r s o   e m   V í  d  e  o'
#          0 1 2 3 4 5 6 7 8 9 10 11 12 13

# frase[9] = 'V'
print(frase[9])

# frase[9:13] = 'Víde' (começa no 9 e termina antes do outro parâmetro, no caso vai até 12)
print(frase[9:13])

# frase[:5] = 'Curso' (se não nada antes dos ":" quer dizer que inicia no 0 até o anterior do número colocado)
print(frase[:5])

# frase[9:] = 'Vídeo' (ele vai do número escolhido até o final)
print(frase[9:])

# frase[9::3] = 'Ve' (começa no 9, vai até o final e pula de 3 em 3)
print(frase[9::3])

# ------------------------------------------------------

# ANÁLISE

# Exemplos: 

# frase = 'C u r s o   e m   V í  d  e  o'
#          0 1 2 3 4 5 6 7 8 9 10 11 12 13

# len(frase) -> mostra o tamanho da frase
print(len(frase))

# frase.count('o') -> conta quantos 'o' tem na frase
print(frase.count('o'))

# frase.count('o',0,5) -> podemos tambem colocar o fatiamento, nesse caso vai procurar 'o' do 0 até o 4 caractere
print(frase.count('o',0,5))

# frase.find('deo') -> vai dizer onde começa a string, neste caso na posição 11
print(frase.find('deo'))


# frase.find('android') -> não vai achar essa palavra, então retornará -1
print(frase.find('android'))

# 'Curso' in frase -> vai dizer se existe dentro da string ou não, neste caso retornaria True
print('Curso' in frase)

# ------------------------------------------------------

# TRANSFORMAÇÃO

# Exemplos:

# frase.replace('Curso', 'Aula') -> vai trocar a palavra 'Curso' pela palavra 'Aula', porem não diretamente na string
print(frase.replace('Curso', 'Aula'))

# frase.upper() -> vai deixar a frase em maiuscula
print(frase.upper())

# frase.lower() -> deixa a frase em minusculo
print(frase.lower())

# frase.capitalize() -> deixa todas as letras iniciais das palavras em maiusculo
print(frase.capitalize())

# frase.title() -> analisa quantas palavras tem na frase (palavras != letras)
print(frase.title())

# frase.strip() -> remove apenas os espaços inuteis da frase
# ex:
# 'XXXAprenda PythonXX'

# frase.rstrip() -> remove somente os ultimos espaços inuteis 
# ex:
# '   Aprenda PythonXX'

# frase.lstrip() -> remove somente os primeiro espaços inuteis 
# ex:
# 'XXXAprenda Python  '

# ------------------------------------------------------

# DIVISÃO

# Exemplo:

# frase.split() -> pega onde tem espaço e cria uma divisão
#               -> gera basicamente uma lista 

# ex:
#'C u r s o   e m   V í d e o'
# 0 1 2 3 4   0 1   0 1 2 3 4
#     0        1        2

# ------------------------------------------------------

# JUNÇÃO       

# Exemplo:

# '-'.join(frase) -> vai adicionar um '-' entre as palavras
