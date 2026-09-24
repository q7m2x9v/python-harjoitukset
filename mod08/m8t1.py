vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä",  "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

kuukausi = int(input("Anna kuukauden numero: "))

if 1 <= kuukausi <= 12:
    print(vuodenajat[kuukausi -1])
else:
    print("Virheellinen kuukauden numero")


