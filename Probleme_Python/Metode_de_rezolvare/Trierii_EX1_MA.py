def suma_cifrelor(x):
    d={}
    if x == 0:
        d[0] = 1
    while x > 0:
        c = x % 10
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1
        x = x // 10
    s = 0
    for c in d:
        s = s + c * d[c]
    return s
    
def numara_numere(n, m):
    K = 0
    for i in range(0, n + 1):      
        if suma_cifrelor(i) == m:
            K = K + 1
    return K
    
n = int(input("n = "))
m = int(input("m = "))
print("K =", numara_numere(n, m))
