luvut = []
luku = input("Anna luku tai lopeta painamalla ENTER ")
while luku != "":
    luvut.append(int(luku))
    luku = input("Anna luku tai lopeta painamalla ENTER ")
luvut.sort(reverse=True)
print(luvut[:5])

