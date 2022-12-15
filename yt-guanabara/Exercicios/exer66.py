soma = 0
cont = 0

while True:
    nums = int(input('Digite um número: '))
    
    if nums == 999:
        break

    soma = soma + nums
    cont += 1
    

print(f'A soma de todos os {cont} digitados foi {soma}')
    

