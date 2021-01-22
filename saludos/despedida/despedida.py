class Coche:
    def __init__(self, color="verde", rueda="4", largo=250, enmarcha=False):
        self.color = color
        self.rueda = rueda
        self.largo = largo
        self.enmarcha = enmarcha

    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        if self.enmarcha:
            return "El coche esta en marcha"
        else:
            return "El coche no esta en marcha"

    def colorear(self):
        self.color = "Black"
        return "El coche es color negro"

    def masruedas(self):
        self.rueda = 6
        print(f"el coche tiene {self.rueda} ruedas y es un marcianno")


coche1 = Coche()
coche1.arrancar()
print(coche1.enmarcha)
