# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

lista = []
count = 0

qtd = int(input('Digite a quantidade de número que deseja digitar: '))
while qtd != count:
    numero = float(input('Digite um número: '))

    while numero > 1000 or numero < 0:
        numero = float(input('Digite novamente um número entre 0 e 1000: '))

    lista.append(numero)
    count += 1

print('Lista: ', lista, '\nMaior: ', max(lista), '\nMenor: ', min(lista))
print('Soma: ', max(lista) + min(lista))