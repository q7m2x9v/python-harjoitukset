
def yksikköhinta(halkaisija, hinta):
    säde = halkaisija / 2 / 100
    pinta_ala = 3.14 * säde * säde
    yksikköhinta = hinta / pinta_ala
    return yksikköhinta

halkaisija1 = float(input("Anna 1. pizzan halkaisija(cm): "))
hinta1 = float(input("Anna 1. pizzan hinta(€): "))

halkaisija2 = float(input("Anna 2. pizzan halkaisija (cm): "))
hinta2 = float(input("Anna 2. pizzan hinta(€): "))

yksikköhinta1 = yksikköhinta(halkaisija1, hinta1)
yksikköhinta2 = yksikköhinta(halkaisija2, hinta2)

if yksikköhinta1 < yksikköhinta2:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif yksikköhinta2 < yksikköhinta1:
    print("Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Pizzojen yksikköhinnat on samat")