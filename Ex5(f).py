def radacina(a, b):
    if a == 0:
        if b == 0:
            return "O infinitate de solu?ii"
        else:
            return "Nu are solu?ii"
    else:
        return -b / a
a,b=int(input("a=")),int(input("b="))
print("R?d?cina ecua?iei este:", radacina(a, b))
