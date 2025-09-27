def divizor (a6,b6):
    for i in reversed(range(1,min(a6+1,b6+1))):
        if a6%i==0 and b6%i==0:
            return i
a,b=int(input('Introduce un numar:')),int(input('Introduce un numar:'))
print("Cel mai mare divizor comun al",a,"si",b,"este",divizor(a,b))
