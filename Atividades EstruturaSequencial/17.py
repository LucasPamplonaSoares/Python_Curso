# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as
# quantidades de tinta a serem compradas e os respectivos preços em 3 situações: * comprar apenas latas de 18 litros;
# * comprar apenas galões de 3,6 litros; * misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area_para_pintar = float(input('Qual o tamanho em metros quadrados da area a ser pintada?'))
litro = area_para_pintar/6
latas = litro/18
galoes = litro/3.6
preco_lata = 80
preco_galao = 25

if area_para_pintar < 18:
    print(' Você não pode comprar uma lata.')
    print(' Comprando galões de 3,6l, gastará R$ ', round(galoes) * preco_galao, ".")

else:
    print(' Se você comprar apenas latas de 18l, gastará R$ ', round(latas)*preco_lata, ".")
    print(' Se você comprar apenas galões de 3,6l, gastará R$ ', round(galoes)*preco_galao, ".")

mistura_lata = int(latas)
mistura_galao = int(galoes)

if area_para_pintar > mistura_lata:
    total_galao = area_para_pintar * mistura_galao
    print(f'Você utilizará {total_galao} galões')
else:
    total_misto = area_para_pintar