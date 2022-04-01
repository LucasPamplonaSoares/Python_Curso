class calcu:
    def __init__(self, a, b): # Ele vai passar pelo metodo init quando for instancia
        self.a = a
        self.b = b

    def soma(self):  # def vai definir algo ou um retorno como retornar os valores de a e b
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b

    def mult(self):
        return self.a * self.b

if __name__ == '__main__':
    calcu = calcu( 10, 2) # Isso é istanciar
    print(calcu.soma())
    print(calcu.div())
    print(calcu.mult())
    print(calcu.sub())

''''def soma(a, b): # def vai definir algo ou um retorno como retornar os valores de a e b
    return a + b


def sub(a,b):
    return a - b


def div(a, b):
    return a / b


def mult(a,b):
    return  a * b


print(soma(5,6))
print(sub(78, 67))
print(div(7, 9))
print(mult(67, 8))'''