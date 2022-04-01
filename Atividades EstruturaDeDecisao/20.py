# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite uma nota: '))
n3 = float(input('Digite uma nota: '))

media = (n1 + n2 + n3) / 3

if media >= 7 and media <10:
    print(f'Parabens sua média foi {media}')
    print('APROVADO')

elif media < 7:
    print(f'Estude na proxima vez, sua média foi {media}')
    print('REPROVADO')

elif media == 10:
    print(f'VC É FODA, SUA MÉDIA FOI {media}')
    print('APROVADO COM DISTINÇÃO')