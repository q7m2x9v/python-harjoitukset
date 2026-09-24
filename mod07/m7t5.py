luvut = [2, 7, 4, 9, 10, 3]

def laske_parilliset(luvut):
    määrä = 0
    for luku in luvut:
        if luku % 2 == 0:
            määrä += 1
    return määrä

tulos = laske_parilliset(luvut)
print(tulos)
