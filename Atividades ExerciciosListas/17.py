# Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# O resultado do atleta será determinado pela média dos cinco valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
# depois informe o nome, os saltos e a média dos saltos.
# O programa deve ser encerrado quando não for informado o nome do atleta.
# A saída do programa deve ser conforme o exemplo abaixo:

"""Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m"""

atletas = []
while True:
    nome = str(input('Digite o seu nome [Caso não queira digitar, aperte ENTER pare encerrar]: '))
    if nome == '':
        break
    atleta = {'nome': nome,
               'saltos': [],
               'media': 0,
               'melhor_salto': 0,
               'pior_salto': 0, }

    for i in range(5):
        atletas.get('saltos').append(float(input(f'Distancia do {i + 1}° salto: ')))

    atleta.get('saltos').sort()
    atleta['pior salto'] = atleta.get('saltos').pop(0)
    atleta['melhor salto'] = atleta.get('saltos').pop()
    atleta['media'] = sum(atleta.get('saltos')) / 3
    print(f"\nMelhor salto: {atleta.get('melhor_salto'):.1f} m"
          f"\nPior salto: {atleta.get('pior_salto'):.1f} m"
          f"\nMédia dos demais saltos: {atleta.get('media'):.1f} m\n")

    atletas.append(atleta)


print("\n\nResultado final")
for atleta in atletas:
    print(f"{atleta.get('nome')}: {atleta.get('media'):.1f} m")