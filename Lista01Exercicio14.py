"""A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de bolos a cada
dia. Cada pãozinho custa R$ 0,12 e o pedaço de bolo custa R$ 1,50. Ao final do dia, o dono quer
saber quanto arrecadou com a venda dos pães e bolos (juntos), e quanto' deve guardar numa conta
de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono.
Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de bolos vendidos, e
depois calcular quanto arrecadou naquele dia e quanto deve guardar na poupança."""


paes=int(input('Informe a quantidade de pães vendidos: '))
bolo=int(input('Informe a quantidade de pedaço de bolo vendidos: '))

arrecadado= (paes*0.12)+(bolo*1.5)
guardar= arrecadado*0.10

print (f'O valor arrecadado hoje foi de R${arrecadado:.2f} e deverá ser guardado na poupança o valor de R${guardar:.2f}.')