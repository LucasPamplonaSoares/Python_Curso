# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n1:
    maior = n3

menor = n1

if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3

print(f'O menor número foi o {menor}')
print(f'O maior número foi o {maior}')