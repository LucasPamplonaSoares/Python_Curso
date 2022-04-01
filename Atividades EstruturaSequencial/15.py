# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
# A) salário bruto.
# B) quanto pagou ao INSS.
# C) quanto pagou ao sindicato.
# D) o salário líquido.
# E) calcule os descontos e o salário líquido, conforme a tabela abaixo
'''+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$'''
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salario_hora = float(input('Quanto vc ganha por hora ? : R$'))
hora_trabalho = int(input('Quantas horas vc trabalha no mes ? '))
salario_bruto = salario_hora * hora_trabalho
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print(f'R${salario_bruto}')
print(f'Foi pago pro INSS R${inss}')
print(f'Foi pago pro Sindicato R${sindicato}')
print(f'Desconto pro imposto de renda foi R${ir}')
print(f'Salário liquido é de R${salario_liquido}')