import math
H,u,d,N=15,5,3,0
#a)
h0=0
if u>d:
    N=math.ceil((H-h0-u)/(u-d)+1)
print('Daca buburuza incepe sa urce stalpul de la pamant aceasta va ajunge la varf peste',N,'zile.')
#b)
h0=6
if u>d:
    N=math.ceil((H-h0-u)/(u-d)+1)
print('Daca buburuza incepe sa urce stalpul de la inaltimea de 6 m aceasta va ajunge la varf peste',N,'zile.') 
#c)
if u>d:
    N=math.ceil((H-h0-u+d)/(u-d)+1)
print('Daca buburuza incepe sa urce stalpul noaptea de la inaltimea de 6 m aceasta va ajunge la varf peste',N,'zile.')
