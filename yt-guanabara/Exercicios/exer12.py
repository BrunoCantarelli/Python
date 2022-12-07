precoProduto = float(input('Qual é o preço do produto sem desconto? '))

desconto = (5/100) * precoProduto
precoFinal = precoProduto - desconto

print('O preço do produto com 5 por cento de desconto é {}'.format(precoFinal))
