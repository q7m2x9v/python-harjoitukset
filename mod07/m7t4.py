
def laske_summa(luvut):
    summa = 0

    for luku in luvut:
        summa += luku
    return summa

luvut = [1, 2, 3, 4, 5]

tulos = laske_summa(luvut)
print("Lukujen summa on:", tulos)

