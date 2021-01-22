class Carro:
    def __init__(self, marca="nissan", color="blanco", modelo="tsuru", peso=400, enmarcha=False):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.enmarcha = enmarcha

    def encender(self, encen):
        self.enmarcha = encen
        if self.enmarcha:
            return "El carro esta encendido"
        else:
            return "El carro esta apagado"


    def avanzar(self):
        pass

    def detener(self):
        pass

    def girarizquierda(self):
        pass

    def girarderecha(self):
        pass


carro1 = Carro("Audi", "rojo", "deportivo", 500)
carro2 = Carro("BMW", "negro", "turismo", 450)
# carro3 = Carro("seat", "plateado", "todoterreno", 600)
print(carro1.encender(True))

