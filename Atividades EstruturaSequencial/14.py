# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (
# 50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
# limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens
# adequadas.

peso_peixe = eval(input('Informe o peso do Peixe: '))
if peso_peixe > 50:
    peso_excesso = peso_peixe - 50
    multa = 4 * peso_excesso
    print(f'Hoje João pescou {peso_peixe}Kg de peixes, {peso_excesso}Kg a mais que o estabelecido pelo regulamento e isso gerou uma multa de R${multa:.2f}')
else:
    print(f'Hoje João pescou {peso_peixe}Kg de peixes, está dentro do limite estabelecido pelo regulamento')