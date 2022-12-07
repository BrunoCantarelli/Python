primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for i in range(1, 11):
    print('{} -> '.format(primeiro), end='')
    primeiro += razao
