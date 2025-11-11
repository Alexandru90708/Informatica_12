data_curenta = (2025, 11, 11) 
an_c, luna_c, zi_c = data_curenta
produse = [
    ("Lapte", 2025, 10, 10, 2025, 11, 10, 20.0),
    ("Branza", 2025, 9, 1, 2025, 11, 20, 45.0),
    ("Iaurt", 2025, 11, 1, 2025, 11, 12, 10.0),
    ("Paine", 2025, 11, 9, 2025, 11, 13, 8.0),
    ("Ulei", 2024, 11, 10, 2026, 11, 10, 30.0)
]
preturi_actuale = []
expirate = []
reducere50 = []
reducere20 = []
valabil_min1an = []
valabil_max1luna = []
for p in produse:
    den, af, lf, zf, ae, le, ze, pret_init = p
    zile_fab = af * 365 + lf * 30 + zf
    zile_exp = ae * 365 + le * 30 + ze
    zile_curent = an_c * 365 + luna_c * 30 + zi_c
    zile_total = zile_exp - zile_fab
    zile_ramase = zile_exp - zile_curent
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
print("=== PRODUSE ȘI PREȚURI ACTUALE ===")
for x in preturi_actuale:
    print(f"{x[0]}: inițial {x[1]} lei, actual {round(x[2], 2)} lei")
print("\n=== LISTE CERUTE ===")
print("Produse expirate:", expirate)
print("Reducere 50%:", reducere50)
print("Reducere 20%:", reducere20)
print("Valabile cel puțin 1 an:", valabil_min1an)
print("Valabile cel mult 1 lună:", valabil_max1luna)
