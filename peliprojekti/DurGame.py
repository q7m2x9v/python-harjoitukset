#Pelaajan reppu
reppu = []

#Funktio
def tutki_huonetta():
    print("Tutkitaan huonetta...")
    print("Löysit tavarat: miekka, köysi, avain")

def katso_reppuun():
    print("Repussa on:")
    for tavara in reppu:
        print(tavara)

def lisää_tavara():
    tavara = input("Minkä tavaran haluat lisätä reppuun?")
    reppu.append(tavara)
    print(tavara, "lisättiin reppuun.")

#Kysytään nimi ja ikä
nimi = input("Anna nimi: ")
ikä = int(input("Anna ikä: "))


#Ikäraja ja päävalikko
if ikä < 12:
    print("Olet liian nuori pelaamaan.")

else: 
    print("Tervetuloa pelaamaan", nimi + "!")
    while True:
        print("PÄÄVALIKKO")
        print("1) Tutki huonetta")
        print("2) Katso reppuun ")
        print("3) Lisää tavara reppuun")
        print("lopeta")

        komento = input("Anna komento: ")
        if komento == "lopeta":
            print("Peli päättyy. Kiitos pelaamisesta!")
            break
        elif komento == "1":
            tutki_huonetta()
        elif komento == "2":
            katso_reppuun()
        elif komento == "3":
            lisää_tavara()
        else:
            print("Käytössä olevat komennot: 1, 2, 3, lopeta")
