dias_Alugados = int(input('Por quantos dias o carro foi alugado? '))
km_Percorridos = float(input('Quantos Km foram rodados com o carro? '))
custos_Diario = 60
custos_KmRodado = 0.15
custo_final = (dias_Alugados * custos_Diario) + (dias_Alugados + custos_KmRodado)

print('O valor a ser pago é de R${}!'.format(custo_final))

