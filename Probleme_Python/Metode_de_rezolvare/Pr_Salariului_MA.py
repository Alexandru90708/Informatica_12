def nr_bancnote(lei):
    suma = int(lei)
    bancnote = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    rezultat = {}
    for v in bancnote:
        if suma >= v:
            nr = suma // v
            rezultat[v] = nr
            suma -= nr * v
    return rezultat
def nr_monede(bani):
    suma = (bani - int(bani))*100
    monede=[50, 25, 10, 5, 1]
    rezultat = {}
    for v in monede:
        if suma >= v:
            nr = suma // v
            rezultat[v] = int(nr)
            suma -= nr * v
    return rezultat
salariu = float(input("Introduceți salariul: "))
rezolvare_bancnote = nr_bancnote(salariu)
rezolvare_monede =nr_monede(salariu)
print("Salariul il vom primi in cel mai eficient mod in felul urmator:")
for i, nr in rezolvare_bancnote.items():
    print(f"{i} lei : {nr}")
for i, nr in rezolvare_monede.items():
    print(f"{i} bani : {nr}")
