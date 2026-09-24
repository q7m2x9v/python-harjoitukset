lentoasemat = {}

while True:
    toiminto = input("Valitse toiminto: uusi, hae tai lopeta" )

    if toiminto == "uusi":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif toiminto == "hae":
        icao = input("Anna ICAO-koodi: ")
        print(lentoasemat[icao])

    elif toiminto == "lopeta":
        break
