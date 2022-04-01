# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

n = int(input('Digite um número: '))

if n % 2 == 0 and n != 2:
    print('Não é um número primo')
else:
    print('Primo')