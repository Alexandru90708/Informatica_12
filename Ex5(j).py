def zeci(n8):
    return n8%10
n = int(input('Introduce un număr: '))
if n<=0:
    print("Numarul trebuie sa fie pozitiv!")
else:
    print("Ultimul numar  zecimal al numarului intreg ", n, "este", zeci(n))