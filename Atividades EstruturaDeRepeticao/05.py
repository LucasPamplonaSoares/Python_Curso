# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

A = float(input('Informe a população da cidade A '))
B = float(input('Informe a população da cidade B '))
ano = 0
taxa_crescimentoA = float(input('informe a taxa de crescimento da população da cidade A '))
taxa_crescimentoB = float(input('informe a taxa de crescimento da população da cidade B '))
while A < B:
    A += round((A * taxa_crescimentoA) / 100)
    B += round((A * taxa_crescimentoB) / 100)
    ano = ano + 1

print(f'levará {ano} anos para população da cidade A ser maior que a cidade B')
print(f'populaçãoB--> {B} habitantes')
print(f'populaçãoA--> {A} habitantes')
