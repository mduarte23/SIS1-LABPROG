"""Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina informe quanto será o valor arrecadado."""

pequena= int(input('Informe a quantidade de camisetas pequenas vendidas: '))
media= int(input('Informe a quantidade de camisetas medias vendidas: '))
grande= int(input('Informe a quantidade de camisetas grandes vendidas: '))

v_pequena= pequena * 10
v_media= media * 12
v_grande = grande * 15
arrecadado = v_pequena + v_media + v_grande

print(f'O valor arrecadado pela venda das camisetas será de R${arrecadado:.2f}.')