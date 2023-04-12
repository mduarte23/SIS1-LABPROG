"""Uma loja de roupas está fazendo uma liquidação e está oferecendo um desconto de 30% em todas as peças. Faça um programa em que o vendedor informe o valor da roupa e o programa retorna quanto ela custará durante a liquidação?"""

roupa= float(input('Informe o valor da roupa comprada: R$'))

liquidacao = roupa - (roupa*0.30)

print(f'A roupa que custa R${roupa:.2f}, na liquidação irá custar R${liquidacao:.2f}.')
