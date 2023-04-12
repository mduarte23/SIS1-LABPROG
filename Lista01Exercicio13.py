"""Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se
que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário."""

custo=float(input('Informe o preço de custo do produto: R$'))
porcentagem= float(input('Informe a porcentagem de lucro do produto: '))

lucro= custo*(porcentagem/100)
venda=lucro+custo

print(f'O produto com preço de custo de R${custo:.2f} com {porcentagem}% de lucro será vendido por R${venda:.2f}.')
