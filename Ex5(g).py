def divizor (a5):
    for i in range(2,a5+1):
        if a5%i==0:
            return i
a=int(input('Introduce un numar:'))
print("Cel mai mic divizor al lui",a," ,inafara de 1, este",divizor(a))