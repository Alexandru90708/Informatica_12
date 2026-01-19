x,y=int(input('a=')), int(input('b='))

def suma_ab(a,b): #a
    return a+b

def produs_ab(a,b): #b
    return a*b

def media_ab(a,b):    #c
    return (a+b)/2
    
def cmmdc_ab(a, b):   #d
    while b!= 0:
        a,b = b, a%b
    return a

def cmmmc_ab(a,b):    #e
    return abs(a * b) // cmmdc_ab(a, b)
    
def min_ab(a,b):      #f
    return min(a,b)

def maxim_ab(a,b):    #g
    return max(a,b)
    
def divizori(a,b):    #j
    divizor=[]
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            divizor.append(i)
    return divizor
    
def multipli_c(a,b):   #k
    k=5
    multipli=[]
    i=1
    while len(multipli) <k:
        if i%a==0 and i%b==0:
            multipli.append(i)
        i+=1
    return multipli

def cifre_c(a,b): #l
    A=str(a)
    B=str(b)
    cifre=[]
    for i in range (0,len(A)):
        if A[i] in B and A[i] not in cifre:
            cifre.append(A[i])
    return cifre
    
def cifre_a(a,b): #m
    A=str(a)
    B=str(b)
    cifre_A=[]
    for i in range (0,len(A)):
        if A[i] not in B and A[i] not in cifre_A:
            cifre_A.append(A[i])
    return cifre_A

def prietenie(a,b):
    na,nb=0,0
    for i in range (1,a+1):
        if a%i==0:
            na+=1
    for i in range (1,b+1):
        if b%i==0:
            nb+=1
    if na==nb:
        return 'PRIETENIE'
    else:
        return "Numerele nu sunt prietene."

print('a) Suma numerelor =', suma_ab(x,y))
print('b) Produsul numerelor = ', produs_ab(x, y))
print('c) Media numerelor = ', media_ab(x,y))
print('d) Cel mai mare divizor comun =', cmmdc_ab(x,y))
print('e) Cel mai mic multiplu comun =', cmmmc_ab(x,y))
print('f) Minimul numerelor = ', min_ab(x, y))
print('g) Maximul numerelor=', maxim_ab(x,y))
print('h) ',x,'+',y,'=',suma_ab(x,y))
print('i) ',x,'*',y,'=',produs_ab(x,y))
print('j) Divizorii comuni sunt:', divizori(x,y))
print('k) Cinci multipli comuni ai', x,'si',y,'sunt', multipli_c(x,y))
print('l) Cifrele comune in ambele numere sunt',cifre_c(x,y))
print("m) Cifrele care se contin doar in primul numar",x,'si nu in al doilea numar',y,'sunt',cifre_a(x,y))
print("n)",prietenie(x,y))
