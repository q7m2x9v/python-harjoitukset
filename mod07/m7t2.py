import random

def heitä_noppaa(tahkot):
    silmäluku = random.randint(1, tahkot)
    return silmäluku

tahkot = int(input("Anna nopan tahkojen määrä: "))

silmäluku = heitä_noppaa(tahkot)

while silmäluku != tahkot:
    print(silmäluku)
    silmäluku = heitä_noppaa(tahkot)

print(silmäluku)

