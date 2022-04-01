# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

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

'''FALTA RESOLVER O PROBLEMA DE INTERCALAR ENTRE OS 3 VETORES'''