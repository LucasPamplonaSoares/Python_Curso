# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

altura = []
idade = []

for i in range(1, 6):
    idade.append(int(input('Digite a sua idade: ')))
    altura.append(float(input('Digite a sua altura: ')))


print('--- Ordem inversa Altura ---')
print(altura[::-1])
print(idade[::-1])

print('--- Ordem lida ---')
print(f'Altura: {altura}')
print(f'Idade: {idade}')

