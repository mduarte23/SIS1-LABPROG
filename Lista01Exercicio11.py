"""Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após
um mês. Considere fixo o juro da poupança em 0,70% a. m. """

deposito= float(input('Informe a quantia em reais depositada: R$'))

juros=deposito*0.007

rendimento=juros+deposito

print(f'O valor da aplicação de R${deposito:.2f} após um mês de rendimento é de R${rendimento:.2f}.')
