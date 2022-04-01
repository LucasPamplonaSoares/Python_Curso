# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
# representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
# Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

n_alunos = []
altura_aluno = []

for i in range(10):
    print('\nDigitação número ', i + 1, ' :')
    alunos = int(input('Digite o número de alunos: '))
    while alunos in n_alunos:
        print('Este Número já foi digitado')
        alunos = int(input('Digite outro número: '))
    altura = altura_aluno.append(float(input('Digite a altura do aluno: ')))
    n_alunos.append(alunos)

indice_baixo = altura_aluno.index(min(altura_aluno))
indice_alto = altura_aluno.index(max(altura_aluno))

print('Aluno mais baixo \nNúmero: ', n_alunos[indice_baixo], '\nAltura: ', min(altura_aluno))
print('Aluno mais alto \nNúmero: ', n_alunos[indice_alto], '\nAltura: ', max(altura_aluno))
