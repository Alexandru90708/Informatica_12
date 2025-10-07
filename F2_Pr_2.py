print("Dati numerele reale de la a1...a10")
a1,a2,a3,a4,a5,a6,a7,a8,a9,a10=float(input("a1=")),float(input("a2=")),float(input("a3=")),float(input("a4=")),float(input("a5=")),float(input("a6=")),float(input("a7=")),float(input("a8=")),float(input("a9=")),float(input("a10="))

def maxim(a,b):
    return max(a,b)
def minim(a,b):
    return min(a,b)
def suma():
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global a8
    global a9
    global a10
    return round(maxim(minim(a1,a2),maxim(a3,a4))+minim(maxim(a5,a6),minim(a7,a8)),2)
def total():
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global a8
    global a9
    global a10
    return round(minim(a1,a2)+minim(a3,a4)+minim(a5,a6)+minim(a7,a8)+minim(a9,a10)+maxim(a1,a2)+maxim(a3,a4)+maxim(a5,a6)+maxim(a7,a8)+maxim(a9,a10),2)
print("Suma=",suma())
print("Total=",total())