print('========= LOJAS CANTARELLI =========')

preco = float(input('Qual é o preço do produto? R$'))
condicao = int(input('''FORMAS DE PAGAMENTO: 
[ 1 ] - À vista dinheiro/cheque. 
[ 2 ] - À vista no cartão. 
[ 3 ] - 2x no cartão. 
[ 4 ] - 3x ou mais no cartão.
Qual opção você escolhe? '''))

A_vista_dinheiro_cheque = preco - ((10/100) * preco)
A_vista_cartao = preco - ((5/100) * preco)
cartao2x = preco
cartao3x = preco + ((20/100) * preco)

if condicao == 1:
    print('O valor do produto com 10% de desconto é R${}'.format(A_vista_dinheiro_cheque))
elif condicao == 2:
    print('O valor do produto com 5% de desconto é R${}'.format(A_vista_cartao))
elif condicao == 3:
    print('O valor do produto é R${}'.format(cartao2x))
elif condicao == 4:
    print('O valor do produto com 20% de juros é R${}'.format(cartao3x))
