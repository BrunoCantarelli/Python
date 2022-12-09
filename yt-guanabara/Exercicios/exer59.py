from time import sleep

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é {}'.format(num1, num2, soma))
    elif opcao == 2:
        produto = num1 * num2
        print('O resultado de {} x {} é {}'.format(num1, num2, produto))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o maior valor é {}'.format(num1, num2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
        print('Programa finalizado com sucesso!')
    else:
        print('Opção inválida. Tente novamente.')
  
    
   
