from distutils import core


class Bola:
    def __init__(self, cor, raio, material):
        self.cor = cor
        self.raio = raio
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostrarCor(self):
        print(self.cor)

x = Bola('amarelo', 10, 'plastico')

x.trocaCor('vermelho')

x.mostrarCor()