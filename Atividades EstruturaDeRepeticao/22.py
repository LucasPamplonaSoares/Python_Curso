# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

n = int(input('Digite um número: '))
lista = []

if n % 2 != 0 or n == 2:
    print('Primo')
else:
    for i in range(n):
        if n % (i + 1) == 0:

            lista.append(i + 1)

print(f'Os números divisiveis por {n} são {lista}')