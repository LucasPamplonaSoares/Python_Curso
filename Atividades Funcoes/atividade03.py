#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(a, b, c):
    s = a + b + c
    return s

a = int(input("Primeiro Número: "))
b = int(input("Segundo Número: "))
c = int(input("Terceiro Número: "))

print("Soma = ", soma(a, b, c))