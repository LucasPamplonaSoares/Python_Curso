# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em
# Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tam_arquivo = float(input('Qual o tamanho do arquivo (MB) ? '))
velocidade_internet = float(input('Qual a velocidade da internet (Mbps) ? '))
tempo = ((tam_arquivo * 8) / velocidade_internet) / 60

print (f'O tempo aproximado de download é de {tempo} minutos')