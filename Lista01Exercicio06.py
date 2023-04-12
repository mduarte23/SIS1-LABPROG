"""Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no
semestre. No final informar o nome do aluno e a sua média (aritmética) """

nome= input('Digite o nome do aluno: ')
prova1=float(input('Digite a nota da 1° prova: '))
prova2=float(input('Digite a nota da 2° prova: '))
prova3=float(input('Digite a nota da 3° prova: '))

media= (prova1+prova2+prova3)/3

print(f'A nota média do(a) aluno(a) {nome} foi de {media}.')