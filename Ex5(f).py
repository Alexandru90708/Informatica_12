def radacina(a, b):
    if a == 0:
        if b == 0:
            return "O infinitate de solutii"
        else:
            return "Nu are solutii"
    else:
        return -b / a
a,b=int(input("a=")),int(input("b="))
print("Radacina ecuatiei este:", radacina(a, b))
