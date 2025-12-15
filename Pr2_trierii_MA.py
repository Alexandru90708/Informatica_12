def dictionar_cifre(x):
    d = {}
    for c in x:
        cifra = int(c)
        if cifra in d:
            d[cifra] = d[cifra] + 1
        else:
            d[cifra] = 1
    return d

def prietenoase(a, b):
    d1 = dictionar_cifre(a)
    d2 = dictionar_cifre(b)
    for c in d1:
        if c not in d2:
            return False
    for c in d2:
        if c not in d1:
            return False

    return True

a = input("Primul numar = ")
b = input("Al doilea numar = ")
if prietenoase(a, b):
    print("Numerele sunt prietenoase")
else:
    print("Numerele nu sunt prietenoase")

