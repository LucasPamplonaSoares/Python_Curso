# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês.

salario_hora = float(input('Quanto voce ganha por hora ? : R$'))
hora_mes = float(input('Quantas horas por mes vc trabalha ? : '))
salario_total = salario_hora * hora_mes
print(f'Seu salário é R${salario_total} por mes')