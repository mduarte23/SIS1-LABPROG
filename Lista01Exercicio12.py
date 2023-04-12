"""A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça
um algoritmo que receba um valor de uma compra e mostre o valor das prestações.""" 

compra= float(input('Informe o valor da compra: R$'))

prestacoes= compra/5

print(f'Para a compra no valor de R${compra:.2f}, a prestação será no valor de 5xR${prestacoes:.2f}')
