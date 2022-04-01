# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
# Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
# menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no
# mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
# Salário Bruto: (5 * 220)        : R$ 1100,00 (-) IR (5%)                     : R$   55,00 (-) INSS ( 10%)
# : R$  110,00 FGTS (11%)                      : R$  121,00 Total de descontos              : R$  165,00 Salário
# Liquido                 : R$  935,00

hora = int(input('Informa o valor recebido por hora trabalhada: '))
qtd_hora = int(input('Informe a quantidade de horas trabalhadas no mes: '))

salario_base = hora * qtd_hora
fgts = (salario_base * 11) / 100
sind = (salario_base * 3) / 100

if salario_base <= 900:
    salario_liquido = salario_base - sind
    print(f'Seu salário bruto é R${salario_base}')

elif salario_base >900 and salario_base <= 1500:
    ir = (salario_base * 5) / 100
    salario_liquido = salario_base - ir - sind
    print(f'O valor de seu FGTS e de: {fgts}')

elif salario_base > 1500 and salario_base <= 2500:
    ir = (salario_base * 10) / 100
    salario_liquido = salario_base- ir - sind
    print(f'O sindicato vai te levar: {sind}')

else:
    ir = (salario_base * 20) / 100
    salario_liquido =  salario_base - ir - sind
    print(f'Seu salario liquido e de: {salario_liquido}')