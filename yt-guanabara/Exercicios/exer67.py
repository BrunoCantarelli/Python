while True:
    num = int(input('Digite um número: '))
    print('-'*20)
    
    if num < 0:
        print('PROGRAMA ENCERRADO!')
        break
    
    for c in range(1,11):
            print(f'{num}x{c} = {num*c}')

    print('-'*20)
