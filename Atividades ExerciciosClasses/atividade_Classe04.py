# Classe Pessoa: Crie uma classe que modele uma pessoa:

# A) Atributos: nome, idade, peso e altura
# B) Métodos: Envelhercer, engordar, emagrecer, crescer. 
# Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso 
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5

        self.idade += 1

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

    def mostra_pessoa(self):
        print(f"Nome: {self.nome}, idade: {self.idade} anos, peso: {self.peso}kg, altura: {self.altura}cm")  


Lucas = Pessoa("Lucas", 19, 64, 190)
Lucas.mostra_pessoa()
Lucas.envelhecer()
Lucas.emagrecer(5)
Lucas.mostra_pessoa()