"""O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do
distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de
um carro e escreva o custo ao consumidor."""

fabrica=float(input('Digite o valor de custo de fábrica do carro: R$'))

distribuidor= fabrica*0.28
impostos= fabrica*0.45

consumidor= fabrica+distribuidor+impostos

print(f'O valor final do carro para o consumidor será de R${consumidor:.2f}')