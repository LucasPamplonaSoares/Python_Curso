# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor1 = []
vetor2 = []
vetor3 = []

for elemento in range(0, 10):
    vetor1.append(int(input('Digite um número para o Vetor 1: ')))

for elemento in range(0, 10):
    vetor2.append(int(input('Digite um número para o Vetor 2: ')))

for elemento in range(0, 10):
    vetor3.append(vetor1[elemento])
    vetor3.append(vetor2[elemento])

print(vetor3)
