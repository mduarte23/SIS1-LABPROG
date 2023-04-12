"""Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%. Após o aumento, desconte 8% de impostos. Imprima o salário inicial, o salário com o aumento e o salário final."""
salario = float(input('Informe o salário do funcionário: R$'))

aumento= (salario*0.15) + salario
desconto = aumento - (aumento * 0.08)

print(f'O funcionário com o salário inicial de R${salario:.2f}, com o aumento passará para R${aumento:.2f}, e com o desconto irá receber R%{desconto:.2f}.')