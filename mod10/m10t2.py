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


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []

        # Luodaan hissit ja lisätään ne talon listaan.
        for i in range(hissien_lukumaara):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print("Tätä hissiä ei ole.")
            return

        
        hissi = self.hissit[hissin_numero - 1]

        print("Ajetaan hissiä", hissin_numero)
        hissi.siirry_kerrokseen(kohdekerros)



talo = Talo(1, 10, 3)

talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 8)
talo.aja_hissiä(3, 3)


talo.aja_hissiä(1, 1)