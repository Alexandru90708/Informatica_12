import random
n=int(input('n='))
c6=0
for i in range(n): 
    nr1=random.randint(1,6)
    nr2=random.randint(1,6)
    print(nr1,nr2)
    if nr1==nr2:
        c6+=1
print('Cifra 6 a nimerit de ', c6,'ori')

