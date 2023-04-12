"""Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A
passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar
os valores trocados. Ex: Início A vale 3 e B vale 5 no final da execução A valerá 5 e B valerá 3."""

A= int(input('Informe o valor de A: '))
B= int(input('Informe o valor de B: '))

print(f'No ínicio A vale {A} e B vale {B}')
manterA = A
A = B
B = manterA

print(f'Após a execusão A passa a valer {A} e B passa a valer {B}')