import math
def multiplu (a7,b7):
    return math.lcm(a7,b7)
a,b=int(input('Introduce un numar:')),int(input('Introduce un numar:'))
print("Cel mai mic multiplu comun al",a,"si",b,"este",multiplu(a,b))