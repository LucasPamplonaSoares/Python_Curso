# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

lista_notas = []
notas_alunos = []

for i in range(10):
    media = 0
    notas_alunos = []
    aluno = str(input('Aluno : '))
    for j in range(4):
        notas_alunos.append(float(input('Nota: ')))
        media += notas_alunos[j]
        print(media)
    media = media / 4
    lista_notas.append(media)

print(lista_notas)