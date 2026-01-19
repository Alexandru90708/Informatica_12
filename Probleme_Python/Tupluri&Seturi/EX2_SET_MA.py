import random
n=int(input('n='))
X=set()
Y=set()
for i in  range(n):
    randx=random.randint(0,199)
    randy=random.randint(0,199)
    X.add(randx)
    Y.add(randy)
print('a)',X|Y)
print('b)',X&Y)
print('c)',X-Y)
print('d)',(X-Y)|(Y-X))
print('e)',(X-Y)&(Y-X))
