import random
n = int(input('n='))
X, Y, Z = set(), set(), set()
U=set(range(200))
for i in range(n):
    X.add(random.randint(0,199))
    Y.add(random.randint(0,199))
    Z.add(random.randint(0,199))
print("X =", X)
print("Y =", Y)
print("Z =", Z)
lege1_stanga= U - (X | Y | Z)
lege1_dreapta= (U - X) & (U - Y) & (U - Z)
lege2_stanga= U - (X & Y & Z)
lege2_dreapta= (U - X) | (U - Y) | (U - Z)
if lege1_stanga == lege1_dreapta and lege2_stanga == lege2_dreapta:
    print("\nDa, legile lui De Morgan sunt demonstrate corect!")
else:
    print("\nNu sunt demonstrate corect.")
