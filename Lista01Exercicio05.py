"""Faça um algoritmo que receba dois números e ao final mostre a soma, subtração, multiplicação e a
divisão dos números lidos.
"""

numero1 = int(input('Digite o 1° número: '))
numero2 = int(input('Digite o 2° número: '))

soma = numero1+numero2
subtracao= numero1-numero2
multiplicacao= numero1*numero2
divisao= numero1/numero2

print(f'Os resultados são:\nSoma: {soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao}\nDivisao: {divisao} ')