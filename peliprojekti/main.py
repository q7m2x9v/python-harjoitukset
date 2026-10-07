from pelaaja import Pelaaja
from tiedostot import lue_teksti, tallenna_peli, lataa_peli
from toiminnot import (luo_paikat, liiku, tutki_paikkaa, kalasta, keraa_roska,
                       myy_kalat, tee_tutkimus, lunasta_palkkiot,
                       katso_tavarat, korjaa_vene)


def kysy_nimi():
    nimi = input("Anna pelaajan nimi: ").strip()
    while nimi == "":
        nimi = input("Nimi ei saa olla tyhjä. Anna nimi: ").strip()
    return nimi


def kysy_ika():
    while True:
        try:
            ika = int(input("Anna ikä kokonaislukuna: "))
            if ika >= 0 and ika <= 120:
                return ika
            print("Anna ikä väliltä 0-120.")
        except ValueError:
            print("Kirjoita ikä numerona.")


def paavalikko(pelaaja, roskat):
    print("\n=== PÄÄVALIKKO ===")
    print("Sijainti:", pelaaja.sijainti.nimi)
    print("Rahaa:", pelaaja.raha, "/ 100 euroa. Roskia vedessä:", roskat)
    print("1) Liiku")
    print("2) Tutki paikkaa")
    print("3) Kerää esine")
    print("4) Kalasta")
    print("5) Kerää roska")
    print("6) Myy kalat")
    print("7) Tee ympäristötutkimus")
    print("8) Lunasta palkkiot")
    print("9) Katso tavarat ja edistyminen")
    print("10) Korjaa vene")
    print("11) Ohjeet")
    print("12) Tallenna peli")
    print("lopeta) Tallenna ja sulje peli")
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
            katso_tavarat(pelaaja)
        elif valinta == "10":
            if korjaa_vene(pelaaja):
                if not tallenna_peli(pelaaja, roskat):
                    print("Voittoa ei tallennettu levylle.")
                break
        elif valinta == "11":
            print(lue_teksti("ohjeet.txt"))
        elif valinta == "12":
            tallenna_peli(pelaaja, roskat)
        elif valinta == "0":
            if tallenna_peli(pelaaja, roskat):
                break
        elif valinta == "lopeta":
            if tallenna_peli(pelaaja, roskat):
                return "lopeta"
        else:
            print("Tuntematon komento. Valitse valikossa oleva numero.")


def main():
    print(lue_teksti("intro.txt"))
    print(lue_teksti("ohjeet.txt"))
    while True:
        print("\n1) Uusi peli  2) Jatka tallennusta  3) Ohjeet  0) Lopeta")
        valinta = input("Valitse: ").strip()
        if valinta == "1":
            print("Uuden pelin tallentaminen korvaa edellisen tallennuksen.")
            nimi = kysy_nimi()
            ika = kysy_ika()
            print("Pelaajan nimi:", nimi)
            print("Pelaajan ikä:", ika)
            if ika < 12:
                print("Olet liian nuori pelaamaan.")
                return
            paikat = luo_paikat()
            pelaaja = Pelaaja(nimi, ika, paikat[0])
            print("Tervetuloa, " + nimi + "!")
            if pelaa(pelaaja, paikat, 10) == "lopeta":
                return
        elif valinta == "2":
            tallennus = lataa_peli()
            if tallennus is not None:
                pelaaja, paikat, roskat = tallennus
                print("Pelaajan nimi:", pelaaja.nimi)
                print("Pelaajan ikä:", pelaaja.ika)
                if pelaaja.ika < 12:
                    print("Olet liian nuori pelaamaan.")
                    return
                if pelaa(pelaaja, paikat, roskat) == "lopeta":
                    return
        elif valinta == "3":
            print(lue_teksti("ohjeet.txt"))
        elif valinta == "0" or valinta == "lopeta":
            print("Kiitos pelaamisesta!")
            break
        else:
            print("Tuntematon valinta.")


if __name__ == "__main__":
    main()
