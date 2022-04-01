# Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idade = [10, 15, 9, 22, 13, 12, 14, 19, 18, 17, 16, 20, 21, 23, 25, 26, 27, 28, 29, 30, 34, 35, 36, 38, 50, 51, 52, 53, 53, 63]
altura = [1.60, 1.35, 1.76, 1.98, 1.77, 1.66, 1.80, 1.60, 1.35, 1.76, 1.98, 1.77, 1.66, 1.80, 1.60, 1.35, 1.76, 1.98, 1.77, 1.66, 1.80, 1.60, 1.35, 1.76, 1.98, 1.77, 1.66, 1.80, 1.60, 1.35]
qtd_alunos = 0
media_altura = sum(altura) / len(altura)

for i in range(0, len(idade)):
    if idade[i] > 13 and idade[i] < media_altura:
        qtd_alunos += 1

print(f'Os alunos que tem mais de 13 anos e altura inferior a média dos outros alunos é {qtd_alunos}')

