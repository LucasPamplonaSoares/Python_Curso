# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

n = int(input('Digite um número: '))
lista = []
divisao = 0

for i in range(n + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)
        divisao += 1
    else:
        divisao += 1

print(f'Números primos {lista}')
print(f'Números de divisões {divisao}')
