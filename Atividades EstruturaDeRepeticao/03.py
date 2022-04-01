# Faça um programa que leia e valide as seguintes informações:
# A) Nome: maior que 3 caracteres;
# B) Idade: entre 0 e 150;
# C) Salário: maior que zero;
# D) Sexo: 'f' ou 'm';
# #) Estado Civil: 's', 'c', 'v', 'd';

nome = str(input('Informe o seu nome: '))
while len(nome) < 3:
    nome = str(input('Nome precisa ter mais de 3 caracteres. Informe o seu nome: '))

idade = int(input('Informe a sua idade: '))
while idade < 0 or idade >150:
    idade = int(input('Idade precisa ter entre 0 e 150. Informe a sua idade: '))

salario = float(input('Informe o seu salário: R$'))
while salario <= 0:
    salario = float(input('Salário precisa ser maior que 0. Informe o seu salário: R$'))

sexo = str(input('Informe o seu sexo (F-M): '))
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Informe o seu sexo (F-M): '))

estado_civil = str(input('Informe o seu Estado Civil: [S - C - V - D]'))
while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
    estado_civil = str(input('Informe o seu Estado Civil: [S - C - V - D]'))

print(f'Seu nome é {nome} e vc tem {idade} anos, vc recebe R${salario} e seu sexo é {sexo}. Seu estado civil atualmente é {estado_civil}')