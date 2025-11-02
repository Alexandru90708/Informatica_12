import random
zar1,zar2=1,2  
while zar1!=zar2:
    zar1=random.randint(1, 6)
    zar2=random.randint(1, 6)
    print(zar1, zar2)
print('S-a obținut o dublă!')
print('Suma punctelor este', zar1+zar2)
