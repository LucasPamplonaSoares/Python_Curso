# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa
# que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
# bem como a média das temperaturas.

qtd_temperatura = int(input('Digite quantas temperaturas irá digitar: '))
temperatura = []
temperaturas = 1

for i in range(qtd_temperatura):
    print('Temperatura n°', qtd_temperatura)
    temperaturas = temperatura.append(float(input('Informe qual a temperatura: ')))
    qtd_temperatura += 1

print('A Maior temperatura foi = ', max(temperatura))
print('A menor temperatura foi = ', min(temperatura))
print('Média = ', round(sum(temperatura) / len(temperatura), 2))

