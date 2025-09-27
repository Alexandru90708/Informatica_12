def sup(n1):
    N1=str(n1)
    m=len(N1)
    return int(n1/pow(10,m-1))
n = int(input('Introduce un număr: '))
if n<=0:
    print("Numarul trebuie sa fie pozitiv!")
else:
    print("Cifra superioara in notatia zecimala al numarului intreg ", n, "este", sup(n))