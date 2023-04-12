"""Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida ela
possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa com 19
anos possui 6935 dias de vida; veja um exemplo de saída:
Ex: Tibúrcio, você já viveu 6935 dias."""

nome= input('Informe o seu nome: ')
idade= int(input('Informe a sua idade: '))

dias= 365*idade

print(f'{nome}, você ja viveu {dias} dias!')