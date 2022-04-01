# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
# calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

mes = ['Janeiro', 'Fevereio', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperatura = []

for i in range(0, len(mes)):
    temperatura.append(float(input('Digite a temperatura do Mes de ' + mes[i] + ': ')))

media_anual = sum(temperatura) / len(temperatura)

for i in range(0, len(temperatura)):
    if temperatura[i] > media_anual:
        print(str(i+1) + ' - ' + mes[i])
