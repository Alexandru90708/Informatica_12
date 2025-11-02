import random
n=int(input("n="))
k=[]
s=0
for i in range(1,n+1):
    k.extend([random.randint(-100,100)])
maxim=max(k)
for x in k:
    if x<maxim:
        s+=x
print("Suma elementelor mai mici ca elementul maxim",maxim,' al tabloului',k,' este',s)
