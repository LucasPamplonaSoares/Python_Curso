# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

lista = []
count = 0

qtd = int(input('Digite a quantidade de número que deseja digitar: '))
while qtd != count:
    numero = lista.append(float(input('Digite um número: ')))
    count += 1

print('Lista: ', lista, '\nMaior: ', max(lista), '\nMenor: ', min(lista))
print('Soma: ', max(lista) + min(lista))