num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num1 < num3:
    print('{}, {}, {}'.format(num3, num1, num2))
if num2 > num1 and num1 > num3:
    print('{}, {}, {}'.format(num2, num3, num1))
if num1 > num2 and num2 > num3:
    print('{}, {}, {}'.format(num1, num2, num3))
