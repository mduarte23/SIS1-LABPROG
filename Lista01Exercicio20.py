"""Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. Faça um programa para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais. Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. Não havendo moeda de um tipo, a quantidade respectiva é zero."""

cents1= int(input('Informe a quantidade de moedas de R$0,01: '))
cents5= int(input('Informe a quantidade de moedas de R$0,05: '))
cents10= int(input('Informe a quantidade de moedas de R$0,10: '))
cents25= int(input('Informe a quantidade de moedas de R$0,25: '))
cents50= int(input('Informe a quantidade de moedas de R$0,50: '))
real1= int(input('Informe a quantidade de moedas de R$1,00: '))

dinheiro= real1 + (0.50 * cents50) + (0.25 * cents25) + (0.10 * cents10) + (0.05 * cents5) + (0.01 * cents1)

print(f'Ototal economizado por Pedrinho foi R${dinheiro:.2f}.')
