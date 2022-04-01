# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

tabuada = int(input('Qual número deseja ver a tabuada? : '))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )