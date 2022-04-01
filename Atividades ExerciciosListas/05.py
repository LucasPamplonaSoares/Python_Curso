# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

lista_numero = []
par = []
impar = []
numero = 0

for i in range(20):
    lista_numero.append(int(input('Digite um número: ')))
    numero = lista_numero[i]
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(lista_numero)
print(par)
print(impar)