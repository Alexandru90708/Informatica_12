pers1 = (17, 165, 55, "F", "nu")
pers2 = (25, 180, 80, "M", "da")
pers3 = (30, 175, 72, "F", "nu")
pers4 = (45, 178, 85, "M", "da")
pers5 = (22, 160, 60, "F", "nu")
pers6 = (19, 172, 68, "M", "nu")
persoane = [pers1, pers2, pers3, pers4, pers5, pers6]
n = len(persoane)
sub20 = inalt = peste18 = femei_cond = intre2050 = 0
masa_tot = 0
for p in persoane:
    if p[0] < 20: sub20 += 1
    if p[1] > 170: inalt += 1
    if p[0] > 18:
        masa_tot += p[2]
        peste18 += 1
masa_medie = masa_tot / peste18
for p in persoane:
    if p[3] == "F" and p[0] > 20 and p[4] == "nu": femei_cond += 1
    if 20 <= p[0] <= 50 and p[2] > masa_medie: intre2050 += 1
print("Procentul persoanelor sub 20 de ani:", sub20 / n * 100, "%")
print("Procentul persoanelor ce au o inălțime mai mare decat 170cm:", inalt / n * 100, "%")
print("Masa medie a persoanelor ce au mai mult de 18 ani:", round(masa_medie, 2))
print("Procentul femeilor cu varsta mai mare de 20 de ani, necăsătorite:", femei_cond / n * 100, "%")
print("Procentul persoanelor intre 20–50 ani cu greutatea mai mare decat masa medie:", intre2050 / n * 100, "%")
