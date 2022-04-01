# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos.

qtd_turma = int(input('Quantas turmas existem: '))
alunos_turmas = []
turma = 1

for i in range(qtd_turma):
    print('Turma', turma)
    alunos = int(input('Quantos alunos tem nessa turma ? : '))
    while alunos > 40:
        print('Turma', turma, '[Cada turma deve haver até 40 alunos em sala]')
    turma += 1
    alunos_turmas.append(alunos)

media = sum(alunos_turmas) / len(alunos_turmas)
print(f'A media de alunos é {media}')
