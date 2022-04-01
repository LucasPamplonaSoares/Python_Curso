# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.

lista_letra = []
consoantes = 0

for i in range(10):
    lista_letra.append(str(input('Digite uma letra: ')))
    c = lista_letra[i]
    if c not in ('a', 'e', 'i', 'o', 'u'):
        consoantes += 1
print(consoantes)
