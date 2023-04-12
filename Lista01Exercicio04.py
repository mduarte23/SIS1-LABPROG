"""Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a
distância total percorrida pelo automóvel e o total de combustível gasto"""

distancia= float(input('Digite a distância percorrida em KM: '))
combustivel= float(input('Digite o total de combustível gasto em litros: '))

media= distancia/combustivel

print(f'O consumo médio de combustível foi de {media:.2f} km/l')