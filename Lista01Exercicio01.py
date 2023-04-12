"""1. A velocidade média de um veículo é dado pela expressão 𝑉𝑚 = ∆𝑆/∆𝑡, onde:
∆𝑆: variação de espaço (ponto de chegada – ponto de partida) em quilometros
∆𝑡: variação de tempo (tempo final – tem inicial) em horas
Escreva um programa para calcular a velocidade média dada a variação espacial e a variação
temporal.
"""

deltas=float(input('Digite quantos quilometros você percorreu: '))
deltat=float(input('Digite quanto tempo você gastou em horas: '))


velmedia= deltas/deltat
print ('='*25)

print(f'A velocidade média foi de {velmedia:.1f} KM/H')



