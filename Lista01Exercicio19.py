"""A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra."""

qtde_sanduiche= int(input('Informe a quantidade de sanduiches que deseja fazer: '))

queijo = ((50*2)*qtde_sanduiche) / 1000
presunto = (50* qtde_sanduiche) / 1000
hamburguer = (100* qtde_sanduiche) / 1000

print(f'Para fazer {qtde_sanduiche} sanduiches, sera necessário {queijo}Kg de queijo, {presunto}Kg de presunto e {hamburguer}Kg de carne.')

