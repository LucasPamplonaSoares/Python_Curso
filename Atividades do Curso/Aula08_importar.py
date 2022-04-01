from Aula07_calculadora import calcu
from Aula08_contador import contador_letras

if __name__ == '__main__':
    calculadora = calcu(5, 6)
    print(calculadora.soma())
    lista = ['Gato', 'Cachorro', 'Elefante']
    print(contador_letras(lista))



