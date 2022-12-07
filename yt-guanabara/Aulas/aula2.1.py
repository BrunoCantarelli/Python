a = input('Digite um número: ')
b = input('Digite uma string: ')
c = input('Digite um valor alpha-numérico: ')
d = input('Escrever qualquer palavra')

print(a.isnumeric())
# .isnumeric() "pergunta" pro print se a variavel é um numero e dependendo vai retornar true ou false

print(b.isalpha())
# .isalpha() "pergunta" pro print se a variavel é uma string

print(c.isalnum())
# is.alnum() "pergunta" pro print se a variavel é alpha-numérico(string e numeros ou os dois juntos)

print(d.isupper())
# is.upper "pergunta" pro print se a variavel é composta totalmente por letras MAIUSCULAS