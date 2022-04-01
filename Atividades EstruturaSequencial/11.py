# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A) o produto do dobro do primeiro com metade do segundo .
# B) a soma do triplo do primeiro com o terceiro.
# C) o terceiro elevado ao cubo.

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = float(input('Informe um número real: '))

p = (n1 * 2) * (n2 / 2)
s = (3 * n1) + n3
e = n3**3

print(f'{p}')
print(f'{s}')
print(f'{e}')