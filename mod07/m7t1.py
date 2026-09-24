import random

def heitä_noppaa():
    silmäluku = random.randint(1, 6)
    return silmäluku

#pääohjelma alkaa tästä
silmäluku = heitä_noppaa()

while silmäluku != 6:
    print(silmäluku)
    silmäluku = heitä_noppaa()
  
print(silmäluku)