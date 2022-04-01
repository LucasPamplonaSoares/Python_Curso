# Usado para simplificar codigos simples como no exemplo abaixo

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ('Cachorro', 'Gato', 'Coelho')
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
sub = lambda a, b: a - b
print(soma(5, 10))
print(sub(5, 10))

calculadora = {
    'Soma': lambda a, b: a + b,
    'subtração' : lambda a, b: a - b,
    'Divisão' : lambda a, b: a / b,
    'Multiplicação' : lambda  a, b: a * b
}

soma = calculadora['Soma']
multiplicacao = calculadora['Multiplicação']
divisao = calculadora['Divisão']
subtracao = calculadora['subtração']
print(f'A soma recebe {soma(10, 5)}')
print(f'A muliplicação recebe {multiplicacao(10, 5)}')
print(f'A divisao recebe {divisao(10, 5)}')
print(f'A subtracao recebe {subtracao(10, 5)}')
