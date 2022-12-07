print('-='*20)
print('Analisador de Triânglos')
print('-='*20)

reta1 = float(input('Qual o comprimento da reta 1? '))
reta2 = float(input('Qual o comprimento da reta 2? '))
reta3 = float(input('Qual o comprimento da reta 3? '))

print(' ')


if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As medidas podem formar um triângulo!')
else: 
    print('Algum dos comprimentos não é combatível, tente novamente!')
    
print(' ')  
print(' ')

print('-='*20)
print('Tipo de Triângulo')
print('-='*20)

print(' ')

if reta1 == reta2 and reta2 == reta3:
    print('Triângulo Equilátero!')
elif reta1 == reta2 and reta1 != reta3 and reta2 != reta3:
    print('Triângulo Isóceles!')
elif reta1 == reta3 and reta1 != reta2 and reta2 != reta3:
    print('Triângulo Isóceles!')
elif reta2 == reta3 and reta1 != reta3 and reta2 != reta1:
    print('Triângulo Isóceles!')
elif reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
    print('Triângulo Escaleno!')



