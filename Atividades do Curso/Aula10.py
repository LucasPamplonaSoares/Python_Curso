from datetime import *

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.month)
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()]) # Pega o dia da semana atual convertido
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_atual.strftime('%c'))


def trabalhando_datetime():
    data_atual = date.today() # tras a data atual
    data_atual_str = data_atual.strftime('%A %B %C ') # Dia da semana Mes e Ano
    print(data_atual_str)


def trabalhando_time():
    horario = time(hour=15, minute=10, second=30)
    horario_srt = horario.strftime('%H:%M:%S')
    print(horario_srt)


if __name__ == '__main__':
    trabalhando_datetime()
    trabalhando_time()
    trabalhando_com_datetime()