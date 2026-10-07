class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros = self.kerros + 1
            print("Hissi on kerroksessa", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros = self.kerros - 1
            print("Hissi on kerroksessa", self.kerros)

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.alin_kerros or kohdekerros > self.ylin_kerros:
            print("Tätä kerrosta ei ole.")
            return

        while self.kerros < kohdekerros:
            self.kerros_ylos()

        while self.kerros > kohdekerros:
            self.kerros_alas()


h = Hissi(1, 10)

print("Siirrytään viidenteen kerrokseen:")
h.siirry_kerrokseen(5)

print("Palataan alimpaan kerrokseen:")
h.siirry_kerrokseen(h.alin_kerros)