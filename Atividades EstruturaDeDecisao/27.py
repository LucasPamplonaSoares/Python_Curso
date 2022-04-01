# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
# desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em
# Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morango = int(input('Digite a quantidade de morangos [Kg] '))
maca = int(input('Digite a quantidade de maças [Kg] '))


if morango > 5:
    preco_morango = morango * 2.50
else:
    preco_morango = morango * 1.80

if maca > 5:
    preco_maca = maca * 2.20
else:
    preco_maca = maca * 1.50

preco_total = preco_maca + preco_morango

if preco_total > 25 or (maca + morango) > 8:
    print('Preço final: ', (preco_total - (preco_total * 0.01)))
else:
    print(f'Preco final {preco_total}')