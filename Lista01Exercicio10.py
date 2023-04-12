"""Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre
suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês."""

nome= input('Informe o nome do funcionário: ')
salario= float(input('Informe o salário fixo do funcionário: R$'))
vendas= int(input('Informe a quantidade de vendas realizada pelo funcionário: '))

comissao= salario * 0.15
salario_final= (comissao*vendas)+salario

print(f'O vendedor {nome} tem um salário de R${salario:.2f} mensal, porém com {vendas} vendas realizadas, seu salário será de R${salario_final:.2f}.')
