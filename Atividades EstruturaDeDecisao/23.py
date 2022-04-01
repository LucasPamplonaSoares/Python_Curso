# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

n = float(input('Informe um número: '))
if n == round(n):
    print('Inteiro')
else:
    print('Decimal')