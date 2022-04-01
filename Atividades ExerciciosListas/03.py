# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista_numero = []
media = 0
for i in range(4):
    lista_numero.append(int(input('Digite uma notta: ')))
    media += lista_numero[i]
media = media / 4
print(lista_numero)
print(media)