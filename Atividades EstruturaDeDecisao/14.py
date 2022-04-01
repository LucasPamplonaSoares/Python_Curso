# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2) / 2

if media >= 9 and media <= 10:
    print('Voce tirou um "A"')
    print('Voce foi Aprovado')
    print('-----------------')
    print(f'Sua média foi {media}')

elif media >= 7.5 and media <= 9:
    print('Voce tirou um "B"')
    print('Voce foi Aprovado')
    print('-----------------')
    print(f'Sua média foi {media}')

elif media >= 6 and media <= 7.5:
    print('VOce tirou "C"')
    print('Voce foi Aprovado')
    print('-----------------')
    print(f'Sua média foi {media}')

elif media >= 4 and media <= 6:
    print('Voce tirou "D"')
    print('Voce foi Reprovado')
    print('-----------------')
    print(f'Sua média foi {media}')

elif media <= 4 and media >= 0:
    print('Voce tirou "E"')
    print('Voce foi Reprovado')
    print('-----------------')
    print(f'Sua média foi {media}')