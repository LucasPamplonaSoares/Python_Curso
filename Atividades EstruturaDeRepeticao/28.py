# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

qtd_cds = int(input('Digite a quantidade de CDs: '))
cds = []
n_cd = 1

for i in range(qtd_cds):
    print('Cd número', n_cd)
    valor_cd = cds.append(float(input('Digite o valor do Cd: R$')))
    n_cd += 1

media = sum(cds) / len(cds)
print(f'A media para cada CDs é {media}')