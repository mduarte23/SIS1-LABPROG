"""O restaurante a quilo Bem-Bão cobra R$19,00 por cada quilo de refeição. Escreva um algoritmo que
leia o peso do prato montado pelo cliente (em quilos) e escreva o valor a pagar. Assuma que a
balança já desconte o peso do prato."""

peso= float(input('Informe o peso do prato em KG: '))

valor= peso * 19

print(f'O valor à se pagar será de R${valor:.2f}')