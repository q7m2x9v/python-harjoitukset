import random
import json
import os


# LUOKAT

class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino


class Huone:
    def __init__(self, nimi, esine=None):
        self.nimi = nimi
        self.esine = esine


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
            self.esineet.append(esine)
            self.sijainti.esine = None
            print("Keräsit esineen:", esine.nimi)


# TEKSTITIEDOSTOT

def tiedoston_polku(nimi):
    kansio = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(kansio, nimi)


def luo_tekstitiedostot():
    intro = """PELASTA VENE

Veneesi on hajonnut. Korjaaminen maksaa 100 euroa.
Voit hankkia rahat kalastamalla, keräämällä roskia
tai tekemällä ympäristötutkimusta.

Aloitat satamasta. Rannan kautta pääset järvelle.
Järvi laskee mereen, joten sen puhtaus vaikuttaa myös mereen.
"""

    ohjeet = """OHJEET

Valitse toiminto kirjoittamalla numero ja painamalla Enter.

Paikat: Satama - Ranta - Järvi.
Kulje aina viereiseen paikkaan.

KALASTUSREITTI:
Kerää onki järveltä.
Kerää roskia, kunnes niitä on jäljellä alle 5.
Kalasta ja myy kalat satamassa.
Ahven = 5 euroa, hauki = 10 euroa, kuha = 15 euroa.

YMPÄRISTÖNSUOJELUREITTI:
Kerää järveltä kaikki 10 roskaa.
Lunasta satamassa 10 euroa jokaisesta kerätystä roskasta.
Voit lunastaa palkkiot myös osissa.

TUTKIMUSREITTI:
Kerää tutkimusväline rannalta.
Tee tutkimus satamassa, rannalla ja järvellä.
Lunasta satamassa 100 euron tutkimuspalkkio.

Reittejä voi myös yhdistellä.
Kun sinulla on 100 euroa, korjaa vene satamassa.

Pelin aikana valinta 11 tallentaa.
Valinta 0 tallentaa ja palaa aloitusvalikkoon.
Jatka myöhemmin valitsemalla Jatka tallennusta.
Käytössä on yksi tallennuspaikka.

Kestävä kehitys: YK:n tavoite 14, Vedenalainen elämä.
Roskat estävät kalastamisen. Siivoaminen auttaa vesistöä.
Roskaraja ja palkkiot ovat yksinkertaistettuja pelisääntöjä.
"""

    if not os.path.exists(tiedoston_polku("intro.txt")):
        with open(tiedoston_polku("intro.txt"), "w",
                  encoding="utf-8") as tiedosto:
            tiedosto.write(intro)

    if not os.path.exists(tiedoston_polku("ohjeet.txt")):
        with open(tiedoston_polku("ohjeet.txt"), "w",
                  encoding="utf-8") as tiedosto:
            tiedosto.write(ohjeet)


def lue_teksti(nimi):
    try:
        with open(tiedoston_polku(nimi), "r",
                  encoding="utf-8") as tiedosto:
            return tiedosto.read()
    except OSError:
        return "Tiedostoa ei voitu lukea: " + nimi


# PELIN ALOITTAMINEN

def luo_paikat():
    satama = Huone("Satama")
    ranta = Huone("Ranta", Esine("Tutkimusväline", 2))
    jarvi = Huone("Järvi", Esine("Onki", 1))

    return [satama, ranta, jarvi]


def kysy_nimi():
    while True:
        nimi = input("Anna pelaajan nimi: ").strip()

        if nimi != "":
            return nimi

        print("Nimi ei saa olla tyhjä.")


def kysy_ika():
    while True:
        try:
            ika = int(input("Anna pelaajan ikä: "))

            if ika >= 0 and ika <= 120:
                return ika

            print("Anna ikä väliltä 0-120.")
        except ValueError:
            print("Anna ikä kokonaislukuna.")


# PELIN TOIMINNOT

def onko_esine(pelaaja, nimi):
    for esine in pelaaja.esineet:
        if esine.nimi == nimi:
            return True

    return False


def liiku(pelaaja, paikat):
    print("\nReitti: Satama - Ranta - Järvi")
    print("1) Satama")
    print("2) Ranta")
    print("3) Järvi")
    print("0) Peruuta")

    valinta = input("Minne menet? ").strip()

    if valinta == "0":
        return

    if valinta not in ["1", "2", "3"]:
        print("Tuntematon paikka.")
        return

    kohde = paikat[int(valinta) - 1]
    nykyinen = pelaaja.sijainti.nimi

    if nykyinen == kohde.nimi:
        print("Olet jo täällä.")
    elif nykyinen == "Satama" and kohde.nimi == "Järvi":
        print("Kulje ensin rannan kautta.")
    elif nykyinen == "Järvi" and kohde.nimi == "Satama":
        print("Kulje ensin rannan kautta.")
    else:
        pelaaja.liiku(kohde)


def tutki_paikkaa(pelaaja):
    paikka = pelaaja.sijainti

    if paikka.nimi == "Satama":
        print("Veneesi odottaa korjausta.")
        print("Täällä voit myydä kalat ja lunastaa palkkiot.")
    elif paikka.nimi == "Ranta":
        print("Rannalta johtaa polku satamaan ja järvelle.")
    else:
        print("Täällä voit kalastaa ja kerätä roskia.")

    if paikka.esine is not None:
        print("Näet esineen:", paikka.esine.nimi)
        print("Saat sen valitsemalla Kerää esine.")


def kalasta(pelaaja, roskat):
    if pelaaja.sijainti.nimi != "Järvi":
        print("Voit kalastaa vain järvellä.")
    elif not onko_esine(pelaaja, "Onki"):
        print("Tarvitset ongen. Kerää se järveltä.")
    elif roskat >= 5:
        print("Vedessä on liikaa roskia.")
        print("Kerää roskia, kunnes niitä on jäljellä alle 5.")
    else:
        kalat = ["ahven", "hauki", "kuha"]
        kala = random.choice(kalat)
        pelaaja.saalis.append(kala)
        print("Sait kalan:", kala)


def keraa_roska(pelaaja, roskat):
    if pelaaja.sijainti.nimi != "Järvi":
        print("Roskia kerätään järveltä.")
    elif roskat == 0:
        print("Kaikki roskat on jo kerätty!")
    else:
        roskat = roskat - 1
        pelaaja.keratyt_roskat = pelaaja.keratyt_roskat + 1
        print("Keräsit yhden roskan.")
        print("Roskia jäljellä:", roskat)

    return roskat


def myy_kalat(pelaaja):
    if pelaaja.sijainti.nimi != "Satama":
        print("Kalat myydään satamassa.")
        return 0

    ansaittu = 0

    for kala in pelaaja.saalis:
        if kala == "ahven":
            ansaittu = ansaittu + 5
        elif kala == "hauki":
            ansaittu = ansaittu + 10
        elif kala == "kuha":
            ansaittu = ansaittu + 15

    pelaaja.raha = pelaaja.raha + ansaittu
    pelaaja.saalis.clear()

    print("Sait kalojen myynnistä", ansaittu, "euroa.")
    return ansaittu


def tee_tutkimus(pelaaja, roskat):
    paikka = pelaaja.sijainti.nimi

    if not onko_esine(pelaaja, "Tutkimusväline"):
        print("Tarvitset rannalta löytyvän tutkimusvälineen.")
    elif paikka in pelaaja.tutkitut_paikat:
        print("Olet jo tutkinut tämän paikan.")
    else:
        pelaaja.tutkitut_paikat.append(paikka)

        if paikka == "Satama":
            print("Tutkit veneilyn vaikutuksia vesistöön.")
        elif paikka == "Ranta":
            print("Tutkit roskien kulkeutumista veteen.")
        else:
            print("Kirjasit järven roskamäärän:", roskat)

        print("Tutkittuja paikkoja:",
              len(pelaaja.tutkitut_paikat), "/ 3")

        if len(pelaaja.tutkitut_paikat) == 3:
            print("Tutkimus valmis! Lunasta palkkio satamassa.")


def lunasta_palkkiot(pelaaja):
    if pelaaja.sijainti.nimi != "Satama":
        print("Palkkiot lunastetaan satamassa.")
        return 0

    # Samoista roskista maksetaan vain kerran.
    uudet_roskat = pelaaja.keratyt_roskat - pelaaja.palkitut_roskat
    palkkio = uudet_roskat * 10
    pelaaja.palkitut_roskat = pelaaja.keratyt_roskat

    if len(pelaaja.tutkitut_paikat) == 3:
        if not pelaaja.tutkimuspalkkio:
            palkkio = palkkio + 100
            pelaaja.tutkimuspalkkio = True

    pelaaja.raha = pelaaja.raha + palkkio
    print("Sait palkkioita", palkkio, "euroa.")

    return palkkio


def katso_tiedot(pelaaja):
    print("\nPelaaja:", pelaaja.nimi)
    print("Ikä:", pelaaja.ika)
    print("Rahaa:", pelaaja.raha, "euroa")

    print("Esineet:")
    if len(pelaaja.esineet) == 0:
        print("Ei esineitä.")

    for esine in pelaaja.esineet:
        print(esine.nimi, "-", esine.paino, "kg")

    print("Saalis:", pelaaja.saalis)
    print("Kerätyt roskat:", pelaaja.keratyt_roskat)
    print("Palkitut roskat:", pelaaja.palkitut_roskat)
    print("Tutkitut paikat:", pelaaja.tutkitut_paikat)


def korjaa_vene(pelaaja):
    if pelaaja.sijainti.nimi != "Satama":
        print("Vene on satamassa.")
    elif pelaaja.raha < 100:
        print("Sinulta puuttuu vielä", 100 - pelaaja.raha, "euroa.")
    else:
        pelaaja.raha = pelaaja.raha - 100
        pelaaja.vene_korjattu = True

        print("\nMaksoit korjauksesta 100 euroa.")
        print("Veneesi on jälleen kunnossa!")
        print("Pääset lähtemään saaristoon.")
        print("VOITIT PELIN!")

        return True

    return False


# TALLENNUS JA LATAUS

def tallenna_peli(pelaaja, roskat):
    esineiden_nimet = []

    for esine in pelaaja.esineet:
        esineiden_nimet.append(esine.nimi)

    # Sanakirja kokoaa tiedot JSON-tallennusta varten.
    tiedot = {
        "nimi": pelaaja.nimi,
        "ika": pelaaja.ika,
        "sijainti": pelaaja.sijainti.nimi,
        "raha": pelaaja.raha,
        "esineet": esineiden_nimet,
        "saalis": pelaaja.saalis,
        "roskat": roskat,
        "keratyt_roskat": pelaaja.keratyt_roskat,
        "palkitut_roskat": pelaaja.palkitut_roskat,
        "tutkitut_paikat": pelaaja.tutkitut_paikat,
        "tutkimuspalkkio": pelaaja.tutkimuspalkkio,
        "vene_korjattu": pelaaja.vene_korjattu
    }

    try:
        with open(tiedoston_polku("tallennus.json"), "w",
                  encoding="utf-8") as tiedosto:
            json.dump(tiedot, tiedosto, ensure_ascii=False, indent=4)

        print("Peli tallennettu.")
        return True
    except OSError:
        print("Tallennus epäonnistui. Tarkista kansion kirjoitusoikeus.")
        return False


def lataa_peli():
    try:
        with open(tiedoston_polku("tallennus.json"), "r",
                  encoding="utf-8") as tiedosto:
            tiedot = json.load(tiedosto)

        if tiedot is None:
            print("Tallennettua peliä ei vielä ole.")
            return None

        paikat = luo_paikat()
        sijainti = None

        for paikka in paikat:
            if paikka.nimi == tiedot["sijainti"]:
                sijainti = paikka

        if sijainti is None:
            raise ValueError

        pelaaja = Pelaaja(tiedot["nimi"], tiedot["ika"], sijainti)
        pelaaja.raha = tiedot["raha"]
        pelaaja.saalis = tiedot["saalis"]
        pelaaja.keratyt_roskat = tiedot["keratyt_roskat"]
        pelaaja.palkitut_roskat = tiedot["palkitut_roskat"]
        pelaaja.tutkitut_paikat = tiedot["tutkitut_paikat"]
        pelaaja.tutkimuspalkkio = tiedot["tutkimuspalkkio"]
        pelaaja.vene_korjattu = tiedot["vene_korjattu"]

        # Kerätyt esineet palautetaan pelaajalle.
        # Samalla ne poistetaan alkuperäisistä paikoistaan.
        for paikka in paikat:
            if paikka.esine is not None:
                if paikka.esine.nimi in tiedot["esineet"]:
                    pelaaja.esineet.append(paikka.esine)
                    paikka.esine = None

        roskat = tiedot["roskat"]

        print("Tallennus ladattu.")
        return pelaaja, paikat, roskat

    except FileNotFoundError:
        print("Tallennettua peliä ei vielä ole.")
    except (OSError, ValueError, KeyError, TypeError):
        print("Tallennusta ei voitu lukea.")

    return None


# VALIKOT JA PELISILMUKKA

def paavalikko(pelaaja, roskat):
    print("\n========== PÄÄVALIKKO ==========")
    print("Sijainti:", pelaaja.sijainti.nimi)
    print("Rahaa:", pelaaja.raha, "/ 100 euroa")
    print("Roskia vedessä:", roskat)
    print()
    print("1) Liiku")
    print("2) Tutki paikkaa")
    print("3) Kerää esine")
    print("4) Kalasta")
    print("5) Kerää roska")
    print("6) Myy kalat")
    print("7) Tee ympäristötutkimus")
    print("8) Lunasta palkkiot")
    print("9) Katso pelaajan tiedot")
    print("10) Korjaa vene")
    print("11) Tallenna peli")
    print("12) Ohjeet")
    print("0) Tallenna ja palaa aloitusvalikkoon")

    return input("Valitse toiminto: ").strip()


def pelaa(pelaaja, paikat, roskat):
    if pelaaja.vene_korjattu:
        print("Tämä peli on jo voitettu. Voit aloittaa uuden pelin.")
        return

    while True:
        valinta = paavalikko(pelaaja, roskat)

        if valinta == "1":
            liiku(pelaaja, paikat)
        elif valinta == "2":
            tutki_paikkaa(pelaaja)
        elif valinta == "3":
            pelaaja.keraa_esine()
        elif valinta == "4":
            kalasta(pelaaja, roskat)
        elif valinta == "5":
            roskat = keraa_roska(pelaaja, roskat)
        elif valinta == "6":
            myy_kalat(pelaaja)
        elif valinta == "7":
            tee_tutkimus(pelaaja, roskat)
        elif valinta == "8":
            lunasta_palkkiot(pelaaja)
        elif valinta == "9":
            katso_tiedot(pelaaja)
        elif valinta == "10":
            if korjaa_vene(pelaaja):
                tallenna_peli(pelaaja, roskat)
                break
        elif valinta == "11":
            tallenna_peli(pelaaja, roskat)
        elif valinta == "12":
            print(lue_teksti("ohjeet.txt"))
        elif valinta == "0":
            if tallenna_peli(pelaaja, roskat):
                break
        else:
            print("Tuntematon valinta. Kirjoita valikon numero.")


def main():
    try:
        luo_tekstitiedostot()
    except OSError:
        print("Tekstitiedostoja ei voitu luoda.")
        print("Tallenna main.py kansioon, johon voit luoda tiedostoja.")
        return

    print(lue_teksti("intro.txt"))
    print(lue_teksti("ohjeet.txt"))

    while True:
        print("\n========== ALOITUSVALIKKO ==========")
        print("1) Uusi peli")
        print("2) Jatka tallennusta")
        print("3) Ohjeet")
        print("0) Lopeta")

        valinta = input("Valitse: ").strip()

        if valinta == "1":
            print("Uuden pelin tallennus korvaa aiemman tallennuksen.")

            nimi = kysy_nimi()
            ika = kysy_ika()
            paikat = luo_paikat()
            pelaaja = Pelaaja(nimi, ika, paikat[0])

            print("\nTervetuloa,", nimi + "!")
            pelaa(pelaaja, paikat, 10)

        elif valinta == "2":
            tallennus = lataa_peli()

            if tallennus is not None:
                pelaaja, paikat, roskat = tallennus
                pelaa(pelaaja, paikat, roskat)

        elif valinta == "3":
            print(lue_teksti("ohjeet.txt"))

        elif valinta == "0":
            print("Kiitos pelaamisesta!")
            break

        else:
            print("Tuntematon valinta.")


# Käynnistetään peli.
if __name__ == "__main__":
    main()