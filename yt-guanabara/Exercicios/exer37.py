num = int(input('Digite um número: '))
conversao = int(input('Digite 1 para binário, 2 para octal e 3 para hexadecimal: '))
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)

if conversao == 1:
    print('O número {} em binário é {}'.format(num, binario))
elif conversao == 2:
    print('O número {} em octal é {}'.format(num, octal))
elif conversao == 3:
    print('O número {} em hexadecimal é {}'.format(num, hexadecimal))
