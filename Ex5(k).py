def zeci(n1):
    N1=str(n1)
    m=len(N1)
    return m
n = int(input('Introduce un număr: '))
if n<=0:
    print("Numarul trebuie sa fie pozitiv!")
else:
    print("Numarul de cifre in notatia zecimala al numarului intreg ", n, "este", zeci(n))