# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = int(input('Informe o seu salário: R$'))

if salario == 280:
    por = (20 / 100.0) * salario
    resultado = salario + por
    print(f'Seu novo salário será R${resultado}')

elif salario >= 280 and salario <= 700:
    por = (15 / 100) * salario
    resultado = salario + por
    print(f'Seu novo salário será R${resultado}')

elif salario >= 700 and salario <= 1500:
    por = (10 / 100) * salario
    resultado = salario + por
    print(f'Seu novo salário será R${resultado}')

elif salario >= 1500:
    por = (5 / 100) * salario
    resultado = salario + por
    print(f'Seu antigo salário era R${salario}')
    print('Seu salário aumentou 5% ')
    print(f'O valor aumentado foi R${por}')
    print(f'Seu novo salário é R${resultado}')

