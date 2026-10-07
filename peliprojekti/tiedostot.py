import json
import os

from pelaaja import Pelaaja
from toiminnot import luo_paikat


def tiedoston_polku(nimi):
    # Tiedostot löytyvät myös silloin, kun peli käynnistetään eri kansiosta.
    kansio = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(kansio, nimi)


def lue_teksti(nimi):
    try:
        with open(tiedoston_polku(nimi), "r", encoding="utf-8") as tiedosto:
            return tiedosto.read()
    except OSError:
        return "Tekstitiedostoa ei voitu lukea: " + nimi


def tallenna_peli(pelaaja, roskat):
    esineet = []
    for esine in pelaaja.esineet:
        esineet.append(esine.nimi)
    # JSON-tiedostoon tallennetaan tavallisia arvoja, ei suoraan olioita.
    tiedot = {
        "nimi": pelaaja.nimi,
        "ika": pelaaja.ika,
        "sijainti": pelaaja.sijainti.nimi,
        "raha": pelaaja.raha,
        "esineet": esineet,
        "saalis": pelaaja.saalis,
        "roskat": roskat,
        "keratyt_roskat": pelaaja.keratyt_roskat,
        "palkitut_roskat": pelaaja.palkitut_roskat,
        "tutkitut_paikat": pelaaja.tutkitut_paikat,
        "tutkimuspalkkio": pelaaja.tutkimuspalkkio,
        "vene_korjattu": pelaaja.vene_korjattu
    }
    try:
        with open(tiedoston_polku("tallennus.json"), "w", encoding="utf-8") as tiedosto:
            json.dump(tiedot, tiedosto, ensure_ascii=False, indent=4)
        print("Peli tallennettu.")
        return True
    except OSError:
        print("Tallennus epäonnistui. Tarkista kansion kirjoitusoikeus.")
        return False


def lataa_peli():
    try:
        with open(tiedoston_polku("tallennus.json"), "r", encoding="utf-8") as tiedosto:
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
        pelaaja = Pelaaja(tiedot["nimi"], int(tiedot["ika"]), sijainti)
        pelaaja.raha = int(tiedot["raha"])
        pelaaja.saalis = tiedot["saalis"]
        pelaaja.keratyt_roskat = int(tiedot["keratyt_roskat"])
        pelaaja.palkitut_roskat = int(tiedot["palkitut_roskat"])
        pelaaja.tutkitut_paikat = tiedot["tutkitut_paikat"]
        pelaaja.tutkimuspalkkio = tiedot["tutkimuspalkkio"]
        pelaaja.vene_korjattu = tiedot["vene_korjattu"]
        roskat = int(tiedot["roskat"])
        if not isinstance(pelaaja.saalis, list) or not isinstance(pelaaja.tutkitut_paikat, list):
            raise ValueError
        # Kerätyt esineet siirretään paikoista takaisin pelaajalle.
        for paikka in paikat:
            if paikka.esine is not None and paikka.esine.nimi in tiedot["esineet"]:
                pelaaja.esineet.append(paikka.esine)
                paikka.esine = None
        print("Tallennus ladattu.")
        return pelaaja, paikat, roskat
    except FileNotFoundError:
        print("Tallennettua peliä ei vielä ole.")
    except (OSError, ValueError, KeyError, TypeError):
        print("Tallennusta ei voitu lukea. Voit aloittaa uuden pelin.")
    return None
