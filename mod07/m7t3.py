def gallonat_litroiksi(num):
    litrat = num * 3.785
    return litrat
num = int(input("Syötä gallonamäärä: "))
while num >= 0:
    print(f"{num} gallonaa on {gallonat_litroiksi(num)} litraa")
    num = int(input("Syötä seuraava gallonamäärä: "))

