data_curenta=(2025, 11, 11)
an_c,luna_c,zi_c=data_curenta
produse=[]
with open("Produse.IN.txt", "r") as f:
    for linie in f:
        campuri = linie.split()
        if len(campuri) == 8:
            den = campuri[0]
            af, lf, zf = int(campuri[1]), int(campuri[2]), int(campuri[3])
            ae, le, ze = int(campuri[4]), int(campuri[5]), int(campuri[6])
            pret = float(campuri[7])
            produs = (den, af, lf, zf, ae, le, ze, pret)
            produse.append(produs)
preturi_actuale=[]
expirate=[]
reducere50=[]
reducere20=[]
valabil_min1an=[]
valabil_max1luna=[]
for p in produse:
    den, af, lf, zf, ae, le, ze, pret_init = p
    zile_fab=af * 365 + lf * 30 + zf
    zile_exp=ae * 365 + le * 30 + ze
    zile_cur=an_c * 365 + luna_c * 30 + zi_c
    zile_total=zile_exp - zile_fab
    zile_ramase=zile_exp - zile_cur
    if zile_ramase < 0:
        pret_actual = 0
        expirate.append(den)
    elif zile_ramase <= 0.25 * zile_total:
        pret_actual = pret_init * 0.5
        reducere50.append(den)
    elif zile_ramase <= 0.5 * zile_total:
        pret_actual = pret_init * 0.8
        reducere20.append(den)
    else:
        pret_actual = pret_init
    preturi_actuale.append((den, pret_init, pret_actual))
    if zile_total >= 365:
        valabil_min1an.append(den)
    if zile_total <= 30:
        valabil_max1luna.append(den)
print('   Tabelul cu produse:')
for x in produse:
    print(x)
print("   Produse și prețuri actuale:")
for x in preturi_actuale:
    print(x[0],'inițial', x[1], 'lei, actual', round(x[2], 2), 'lei')
print("\n    Liste cerute:")
print("Produsele expirate:", expirate)
print("Produsele cu reducere de 50%:", reducere50)
print("Produsele cu reducere de 20%:", reducere20)
print("Produsele valabile cel puțin 1 an:", valabil_min1an)
print("produsele valabile cel mult 1 lună:", valabil_max1luna)
