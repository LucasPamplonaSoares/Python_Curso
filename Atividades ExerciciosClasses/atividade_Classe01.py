# Classe Bola: Crie uma classe que modele uma bola:

# A) Atributos: Cor, circunferência, material
# B) Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor="unknown", circunf=0, material="unknown"):
        self.cor = cor
        self.circunf = circunf
        self.material = material

    def troca_cor(self):
        troca = str(input(f"Deseja mudar a cor atual {self.cor}? [s/n]"))
        troca = troca[0].lower()

        if troca == "s":
            nova_cor = str(input(f"\nA cor atual é {self.cor}"))
            self.cor = nova_cor
        else:
            print(f"Ok a cor continua {self.cor}")

    def mostrar_cor(self):
        print(f"\nA cor atual é {self.cor}")       

def main():
    bola = Bola("Azul", 5, "Metal")

    while True:
        bola.mostrar_cor()
        bola.troca_cor()

        continuar = str(input("Continuar? [s/n]"))
        continuar = continuar[0].lower()
        if continuar == "n":
            break

    bola.mostrar_cor()    

main()