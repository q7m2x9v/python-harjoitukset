class Pelaaja:
    def __init__(self, nimi, ika, sijainti):
        self.nimi = nimi
        self.ika = ika
        self.sijainti = sijainti
        self.raha = 0
        self.esineet = []
        self.saalis = []
        self.keratyt_roskat = 0
        self.palkitut_roskat = 0
        self.tutkitut_paikat = []
        self.tutkimuspalkkio = False
        self.vene_korjattu = False

    def liiku(self, kohde):
        self.sijainti = kohde
        print("Siirryit paikkaan:", kohde.nimi)

    def keraa_esine(self):
        if self.sijainti.esine is None:
            print("Täällä ei ole kerättävää esinettä.")
        else:
            esine = self.sijainti.esine
            nimi = input("Kirjoita kerättävän esineen nimi (" + esine.nimi + "): ").strip()
            if nimi.lower() != esine.nimi.lower():
                print("Esinettä ei kerätty. Kirjoita paikassa näkyvän esineen nimi.")
                return
            self.esineet.append(esine)
            self.sijainti.esine = None
            print("Keräsit esineen:", esine.nimi)
