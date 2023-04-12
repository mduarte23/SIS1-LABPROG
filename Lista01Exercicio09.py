"""Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o
preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no
tanque."""

valor=float(input('Informe o preço do litro da gasolina: '))
pagamento = float(input('Informe o valor que foi abastecido: '))

litros = pagamento/valor

print(f'Para o valor de R${pagamento} deve ser colocado {litros:.2f} litros de gasolina')

