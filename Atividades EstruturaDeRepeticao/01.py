# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

n = int(input('Digite um número entre 0 e 10: '))
while n > 10 or n < 0:
    n = int(input('Número Inválido. Digite um número entre 0 e 10: '))