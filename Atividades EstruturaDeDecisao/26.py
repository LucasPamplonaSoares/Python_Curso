# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# A) Álcool:
# B) até 20 litros, desconto de 3% por litro
# C) acima de 20 litros, desconto de 5% por litro
# D) Gasolina:
# E) até 20 litros, desconto de 4% por litro
# F) acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago
# pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combustivel = str(input('Qual combustivel vc quer abastecer ? (A-álcool, G-gasolina) '))
qtd_combustivel = float(input('Quanto vc quer abastecer ? : '))
preco = 0
if combustivel == 'G' or combustivel == 'g':
    preco = qtd_combustivel * 2.50
    if qtd_combustivel <= 20:
        desconto = preco - (preco * 4 / 100)
        print(f'O valor a se pagar será R${desconto}')
    else:
        desconto = preco - (preco * 6 / 100)
        print(f'O valor a se pagar será R${desconto}')

elif combustivel == 'A' or combustivel == 'a':
    preco_A = qtd_combustivel * 1.90
    if qtd_combustivel <= 20:
        desconto = preco_A - (preco_A * 3 / 100 )
        print(f'O valor a se pagar será R${desconto}')
    else:
        desconto = preco_A - (preco_A * 5 / 100)
        print(f'O valor a se pagar será R${desconto}')