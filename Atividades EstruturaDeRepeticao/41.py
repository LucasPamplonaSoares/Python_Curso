# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
# valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67

divida = float(input('Digite o valor da divida: '))
parcela = 1
print('\n' * 5)
print('Valor da divida: ', end="  ")
print('Valor do juros: ', end="  ")
print('Quantidade de parcelas: ', end="  ")
print('Valor da parcela: ')

for i in range(5):
    if parcela == 1:
        juros = 1
        valor_juros = 0
    elif parcela == 4:
        juros = 3
        valor_juros = 10
    elif parcela == 7 or parcela == 6:
        juros = 6
        valor_juros = 15
    elif parcela == 10 or parcela == 9:
        juros = 9
        valor_juros = 20
    elif parcela == 13 or parcela == 12:
        juros = 12
        valor_juros = 25

    valor_juros = divida * (juros - 1)
    divida_juros = divida * juros
    valor_parcela = divida_juros / parcela

    print('R$', round(divida_juros, 2), end='            ')
    print(round(valor_juros, 2), end='                  ')
    print(parcela, end='                        ')
    print('R$ ', round(valor_parcela, 2))
    parcela += 3
