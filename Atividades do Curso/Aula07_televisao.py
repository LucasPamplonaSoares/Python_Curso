class Televisao():
    def __init__(self):
        self.ligada = False
        self.canal = 1

    def ligar(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.canal:
            self.canal += 1

    def diminiu_canal(self):
        if self.canal:
            self.canal -= 1


tv = Televisao()
print('Televisão está ligada : {}'.format(Televisao.ligar))
tv.ligar()
print(Televisao.ligar)
tv.ligar()
print(Televisao.ligar)
Televisao.aumenta_canal()
print('Canal: {}'.format(Televisao.canal))
