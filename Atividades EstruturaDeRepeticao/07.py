# Faça um programa que leia 5 números e informe o maior número.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
n5 = int(input('Digite um número: '))

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print(f'{n1} é maior que os outros números informados')
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print(f'{n2} é maior que os outros números informados')
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    print(f'{n3} é maior que os outros números informados')
elif n4 > n1 and n4 > n3 and n4 > n2 and n4 > n5:
    print(f'{n4} é maior que os outros números informados')
else:
    print(f'{n5} é maior que os outros números informados')