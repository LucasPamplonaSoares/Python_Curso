# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# A) par ou ímpar;
# B) positivo ou negativo;
# C) inteiro ou decimal.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
operacao = input('Informe qual operação deseja realizar : [+, -, /, *] ')

def check():
    if resultado // 1 == resultado:
        print('Inteiro')
        if resultado % 2 == 0:
            print('Par')
            if resultado > 0:
                print('Positivo')
            else:
                print('Negativo')
        else:
            print('Impar')
    else:
        print('Decimal')

if operacao == '+':
    resultado = n1 + n2
    print('Resultado: ', resultado)
    check()
elif operacao == '-':
    resultado = n1 - n2
    print('Resultado: ', resultado)
    check()
elif operacao == '/':
    resultado = n1 / n2
    print('Resultado: ', resultado)
    check()
elif operacao == '*':
    resultado = n1 * n2
    print('Resultado: ', resultado)
    check()
else:
    print('Valor Invalido')
