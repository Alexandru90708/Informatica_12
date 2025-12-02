def descompune_suma(lei):
    suma = int(lei * 100)
    valute = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
    rezultat = {}
    for v in valute:
        if suma >= v:
            nr = suma // v
            rezultat[v] = nr
            suma -= nr * v
    return rezultat
salariu = float(input("Introduceți salariul: "))
rezolvare = descompune_suma(salariu)
print("\n")
for i, nr in rezolvare.items():
    if i >= 100:
        print(f"{i // 100} lei : {nr}")
    else:
        print(f"{i} bani : {nr}")