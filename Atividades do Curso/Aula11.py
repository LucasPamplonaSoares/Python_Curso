lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    # x = a
except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por ZERO')
except IndexError:
    print('Erro ao acessar um indice invalido da lista')
except BaseException as ex:
    print(f'Erro desconhecido. Erro: {ex}')
else:
    print('Executa quando não tem exceção ')
finally:
    print('Sempre executam')
    print('Fechando arquivo')
    arquivo.close()

