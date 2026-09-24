class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

auto = Auto("ABC-123", 142)

print(auto.rekisteritunnus)
print(auto.huippunopeus)
print(auto.nopeus)
print(auto.kuljettu_matka)