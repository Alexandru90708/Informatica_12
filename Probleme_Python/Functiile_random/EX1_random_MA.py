import random
n = int(input('n='))   
spoz = 0                
sneg = 0               
for i in range(n):
    nr = random.randint(-50, 50)  
    print(nr, end=' ')            
    if nr > 0:
        spoz += nr
    elif nr < 0:
        sneg += nr
print('Suma numerelor pozitive este', spoz)
print('Suma numerelor negative este', sneg)
