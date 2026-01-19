elev1 = ("Popescu", "Ion", "M", 8, 9, 7)
elev2 = ("Ionescu", "Maria", "F", 10, 10, 10)
elev3 = ("Georgescu", "Andrei", "M", 4, 6, 5)
elev4 = ("Dumitrescu", "Elena", "F", 9, 9, 9)
elev5 = ("Vasilescu", "Mihai", "M", 7, 8, 6)
elevi = [elev1, elev2, elev3, elev4, elev5]

print("Notele medii:")
for elev in elevi:
    medie = sum(elev[3:6]) / 3
    print(elev[0], elev[1], 'are media:', round(medie, 2))

print("\nRestanțieri:")
for elev in elevi:
    if elev[3] < 5 or elev[4] < 5 or elev[5] < 5:
        print(elev[0], elev[1], "este restanțier.")

print("\nEminenti:")
for elev in elevi:
    if elev[3] >= 9 and elev[4] >= 9 and elev[5] >= 9:
        print(elev[0], elev[1], "este eminent")
