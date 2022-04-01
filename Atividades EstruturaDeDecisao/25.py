# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# A) "Telefonou para a vítima?"
# B) "Esteve no local do crime?"
# C) "Mora perto da vítima?"
# D) "Devia para a vítima?"
# E) "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
# responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5
# como "Assassino". Caso contrário, ele será classificado como "Inocente".

res1 = int(input('Telefonou para a vítima? 1/Sim ou 0/Não: '))
res2 = int(input('Esteve no local do crime? 1/Sim ou 0/Não: '))
res3 = int(input('Mora perto da vítima? 1/Sim ou 0/Não: '))
res4 = int(input('Devia para a vítima? 1/Sim ou 0/Não: '))
res5 = int(input('Já trabalhou com a vítima? 1/Sim ou 0/Não: '))

soma_respostas = res1 + res2 + res3 + res4 + res5

if soma_respostas < 2:
    print('Inocente')

elif soma_respostas == 2:
    print('Suspeita')

elif soma_respostas >= 3 and soma_respostas <=4:
    print('Cúmplice')

elif soma_respostas == 5:
    print('Assassino')
