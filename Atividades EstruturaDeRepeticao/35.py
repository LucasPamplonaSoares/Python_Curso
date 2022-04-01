# Encontrar números primos é uma tarefa difícil.
# Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

n = int(input('Digite um número: '))
lista = []

for i in range(n + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)

print(f'Números primos: {n}')