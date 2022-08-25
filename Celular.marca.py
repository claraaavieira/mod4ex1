class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir1(self):
        print(self.marca, self.modelo)


class Celular2:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir(self):
        print(self.marca, self.modelo)


Celular = Celular('Marca: Iphone', '\nModelo:Xs')
Celular.exibir1()

Celular2 = Celular2('Marca: xiaomi', '\nnote 9')
Celular2.exibir()