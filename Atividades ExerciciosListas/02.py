# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

listaNumero = []

for i in range(10):
    listaNumero.append(float(input('Numero: ')))
listaNumero.reverse()
print(listaNumero)
