import random
n=int(input('n='))
X=set()
Y=set()
Z=set()
for i in  range(n):
    randx=random.randint(0,199)
    randy=random.randint(0,199)
    randz=random.randint(0,199)
    X.add(randx)
    Y.add(randy)
    Z.add(randz)
print(X)
print(Y)
print(Z)
if not(X|Y|Z)==(not(X))&(not(Y))&(not(Z)) and not(X&Y&Z)==(not(X))|(not(Y))|(not(Z)):
    print('Da negatiile sunt egale. Am demonstrat legile lui Morgan!')
else:
    print('Nu am demostrat legile lui Morgan')