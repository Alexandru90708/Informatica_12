import random
n=int(input('n='))
c6=0
for i in range(n): 
    nr=random.randint(1,6)
    print(nr)
    if nr==6:
        c6+=1
print('Cifra 6 a nimerit de ', c6,'ori')

