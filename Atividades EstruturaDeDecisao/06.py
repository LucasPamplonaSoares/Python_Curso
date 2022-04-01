# Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input('DIgite um número: '))
n2 = int(input('DIgite um número: '))
n3 = int(input('DIgite um número: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} é maior')

elif n2 > n1 and n2 > n3:
    print(f'{n2} é maior')

else:
    print(f'{n3} é maior')