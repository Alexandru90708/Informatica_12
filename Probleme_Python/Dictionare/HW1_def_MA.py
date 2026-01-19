def verificare(n, b):
    for c in n:
        if c < '0' or c > '9' or int(c) >= b:
            return False
    return True

def in10(n, b):
    v = 0
    for c in n:
        v = v * b + int(c)
    return v

def din10(v, b):
    if v == 0:
        return "0"
    s = ""
    while v > 0:
        s = str(v % b) + s
        v //= b
    return s

def aduna(a, b1, b):
    return din10(in10(a, b) + in10(b1, b), b)

def scade(a, b1, b):
    d = in10(a, b) - in10(b1, b)
    if d < 0:
        return "-" + din10(-d, b)
    return din10(d, b)

def inmulteste(a, b1, b):
    return din10(in10(a, b) * in10(b1, b), b)

b = int(input("Introduceti un numar de la 1 exclusiv pana la 10 exclusiv:"))
n1 = str(input("Scrie un numar:"))
n2 = str(input("Scrie un numar:"))

print(verificare(n1, b))
print(verificare(n2, b))
print(aduna(n1, n2, b))
print(scade(n1, n2, b))
print(inmulteste(n1, n2, b))
