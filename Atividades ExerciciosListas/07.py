# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

lista_numero = []
multiplicacao = 0
soma = 0
for i in range(5):
    lista_numero.append(int(input('Digite um número: ')))
    soma += lista_numero[i]
    multiplicacao
print(f'A soma de todos os números resultou nesse resultado: {soma}')
print(multiplicacao)
print(lista_numero)