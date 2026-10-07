import random

from esine import Esine
from huone import Huone


def luo_paikat():
    satama = Huone("Satama", "Veneesi odottaa korjausta. Täällä myydään kalat ja maksetaan palkkiot.")
    ranta = Huone("Ranta", "Rannalla on tutkimusväline. Polku jatkuu järvelle.",
                  Esine("Tutkimusväline", 2.0))
    jarvi = Huone("Järvi", "Järven rannalla on onki. Täällä voi kalastaa ja kerätä roskia.",
                  Esine("Onki", 1.5))
    return [satama, ranta, jarvi]


def onko_esine(pelaaja, nimi):
    for esine in pelaaja.esineet:
        if esine.nimi == nimi:
            return True
    return False


def liiku(pelaaja, paikat):
    print("Reitti: Satama - Ranta - Järvi")
    print("1) Satama  2) Ranta  3) Järvi  0) Peruuta")
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
    print(pelaaja.sijainti.kuvaus)
    if pelaaja.sijainti.esine is not None:
        print("Löydät esineen:", pelaaja.sijainti.esine.nimi)
        print("Saat sen valitsemalla Kerää esine.")


def kalasta(pelaaja, roskat):
    if pelaaja.sijainti.nimi != "Järvi":
        print("Voit kalastaa vain järvellä.")
    elif not onko_esine(pelaaja, "Onki"):
        print("Tarvitset ongen. Kerää se järven rannalta.")
    elif roskat >= 5:
        print("Roskia on liikaa! Kerää niitä pois, kunnes jäljellä on alle 5.")
    else:
        kalat = ["ahven", "hauki", "kuha"]
        kala = random.choice(kalat)
        pelaaja.saalis.append(kala)
        print("Sait kalan:", kala)


def keraa_roska(pelaaja, roskat):
    if pelaaja.sijainti.nimi != "Järvi":
        print("Roskia kerätään järveltä.")
    elif roskat == 0:
        print("Kaikki roskat on kerätty!")
    else:
        roskat = roskat - 1
        pelaaja.keratyt_roskat = pelaaja.keratyt_roskat + 1
        print("Keräsit yhden roskan. Jäljellä:", roskat)
        print("Satamassa saat jokaisesta keräämästäsi roskasta 10 euroa.")
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
            print("Kirjasit havaintoja veneilyn vaikutuksista veteen.")
        elif paikka == "Ranta":
            print("Tutkit, miten roskat kulkeutuvat rannalta vesistöön.")
        else:
            print("Kirjasit järven roskamäärän:", roskat)
        print("Tutkittuja paikkoja:", len(pelaaja.tutkitut_paikat), "/ 3")
        print("Kolmen paikan tutkimuksesta saat satamassa 100 euroa.")


def lunasta_palkkiot(pelaaja):
    if pelaaja.sijainti.nimi != "Satama":
        print("Palkkiot lunastetaan satamassa.")
        return 0
    # Jo palkittuja roskia ja tutkimuksia ei makseta uudestaan.
    palkkio = (pelaaja.keratyt_roskat - pelaaja.palkitut_roskat) * 10
    pelaaja.palkitut_roskat = pelaaja.keratyt_roskat
    if len(pelaaja.tutkitut_paikat) == 3 and not pelaaja.tutkimuspalkkio:
        palkkio = palkkio + 100
        pelaaja.tutkimuspalkkio = True
    pelaaja.raha = pelaaja.raha + palkkio
    print("Sait palkkioita", palkkio, "euroa.")
    return palkkio


def katso_tavarat(pelaaja):
    print("Pelaaja:", pelaaja.nimi, "Ikä:", pelaaja.ika)
    print("Rahaa:", pelaaja.raha, "euroa")
    print("Esineet:")
    if len(pelaaja.esineet) == 0:
        print("Ei esineitä.")
    for esine in pelaaja.esineet:
        print(esine.nimi, "-", esine.paino, "kg")
    print("Saalis:", pelaaja.saalis)
    print("Kerätyt roskat:", pelaaja.keratyt_roskat)
    print("Palkitsemattomat roskat:", pelaaja.keratyt_roskat - pelaaja.palkitut_roskat)
    print("Tutkitut paikat:", pelaaja.tutkitut_paikat)


def korjaa_vene(pelaaja):
    if pelaaja.vene_korjattu:
        print("Vene on jo korjattu.")
        return True
    if pelaaja.sijainti.nimi != "Satama":
        print("Vene odottaa satamassa.")
    elif pelaaja.raha < 100:
        print("Tarvitset vielä", 100 - pelaaja.raha, "euroa.")
    else:
        pelaaja.raha = pelaaja.raha - 100
        pelaaja.vene_korjattu = True
        print("Maksoit 100 euroa. Vene on korjattu. VOITIT PELIN!")
        return True
    return False
