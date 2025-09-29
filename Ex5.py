import math
a,b,c,d = int(input("a=")), int(input("b=")), int(input("c=")), int(input("d="))
def suma_4(a1,b1,c1,d1): #a)
    return a1+b1+c1+d1
print("a) Suma numerelor ", a ,",", b ,",", c ," și ", d ," este:", suma_4(a,b,c,d))
def media(a2,b2,c2,d2):  #b)
    return (a2+b2+c2+d2)/4
a,b,c,d=int(input("a=")),int(input("b=")),int(input("c=")),int(input("d="))
print("b) Media numerelor", a ,",", b ,",", c ," și ", d ," este:", media(a,b,c,d))
def minimum(a3,b3,c3,d3):  #c)      
    return min(a3,b3,c3,d3)
a,b,c,d=int(input("a=")),int(input("b=")),int(input("c=")),int(input("d="))
print("c) Cea mai mică valoare dintre", a ,",", b ,",", c ," și ", d ," este:", minimum(a,b,c,d))
def radacina(a, b):   #f)
    if a == 0:
        if b == 0:
            return "O infinitate de soluții"
        else:
            return "Nu are soluții"
    else:
        return -b/a
a,b=int(input("a=")),int(input("b="))
print("f) Rădăcina ecuației este:", radacina(a, b))
def divizor_mic(a5):   #g)
    for i in range(2,a5+1):
        if a5 % i == 0:
            return i
a=int(input("a="))
print("g) Cel mai mic divizor al lui", a, "în afară de 1, este", divizor_mic(a))
def divizor_mare(a6,b6):   #h)
    for i in reversed(range(1,min(a6+1,b6+1))):
        if a6 % i == 0 and b6 % i == 0:
            return i
a,b=int(input("a=")),int(input("b="))
print("h) Cel mai mare divizor comun al lui", a, "și", b, "este", divizor_mare(a,b))
def multiplu(a7,b7):   #i)
    return abs(a7*b7) // math.gcd(a7,b7)
a,b=int(input("a=")),int(input("b="))
print("i) Cel mai mic multiplu comun al lui", a, "și", b, "este", multiplu(a,b))
def ultima_cifra(n8):   #j)
    return n8 % 10
n = int(input('Introduce un număr: '))
if n <= 0:
    print("j) Numărul trebuie să fie pozitiv!")
else:
    print("j) Ultima cifră zecimală a numărului întreg ", n, "este", ultima_cifra(n))
def nr_cifre(n1):    #k)
    return len(str(n1))
nr = int(input('Introduce un număr: '))
if nr <= 0:
    print("k) Numărul trebuie să fie pozitiv!")
else:
    print("k) Numărul de cifre în notația zecimală a numărului întreg ", nr, "este", nr_cifre(nr))
def sup(n1): #l)
    N1 = str(n1)
    m = len(N1)
    return int(n1 // pow(10,m-1))
n_sup = int(input('Introduce un număr: '))
if n_sup <= 0:
    print("l) Numărul trebuie să fie pozitiv!")
else:
    print("l) Cifra superioară în notația zecimală a numărului întreg ", n_sup, "este", sup(n_sup))