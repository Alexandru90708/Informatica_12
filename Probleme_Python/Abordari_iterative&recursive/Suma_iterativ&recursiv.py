x = int(input('Dati nr x = '))
#Suma nr pare recursiv si iterativ
def sum_pare_rec(a):
    if a<=0:
        return 0
    elif a%2 ==0:
        return a+sum_pare_rec(a-2)
    else:
        return sum_pare_rec(a-1)
print(f'Suma nr pare pana la {x} este egala cu {sum_pare_rec(x)}')
def sum_pare_iter(a):
    sum_even = 0
    for i in range(a+1):
        if i%2==0:
            sum_even+=i
    return sum_even
print(f'Suma nr pare pana la {x} este egala cu {sum_pare_iter(x)}')
#Suma nr impare recursiv si iterativ
def sum_impare_rec(a):
    if a<=0:
        return 0
    elif a%2==1:
        return a+sum_impare_rec(a-2)
    else:
        return sum_impare_rec(a-1)
print(f'Suma nr impare pana la {x} este egala cu {sum_impare_rec(x)}')
def sum_impare_iter(a):
    sum_odd = 0
    for i in range(a+1):
        if i%2==1:
            sum_odd+=i
    return sum_odd
print(f'Suma nr impare pana la {x} este egala cu {sum_impare_iter(x)}')
#Suma nr din 5 in 5 recursiv si iterativ
def sum_5_rec(a):
    if a<=0:
        return 0
    if a%5==0:
        return a+sum_5_rec(a-5)
    elif a%5==1:
        return sum_5_rec(a-1)
    elif a%5==2:
        return sum_5_rec(a-2)
    elif a%5==3:
        return sum_5_rec(a-3)
    else:
        return sum_5_rec(a-4)
print(f'Suma nr din 5 in 5 pana la {x} este egala cu {sum_5_rec(x)}')
def sum_5_iter(a):
    sum_5 = 0
    if a%5==0:
        for i in range(0,a+1,5):
            sum_5+=i
    elif a%5==1:
        for i in range(0,(a),5):
            sum_5+=i
    elif a%5==2:
        for i in range(0,(a-1),5):
            sum_5+=i
    elif a%5==3:
        for i in range(0,(a-2),5):
            sum_5+=i
    else:
        for i in range(0,(a-3),5):
            sum_5+=i
    return sum_5
print(f'Suma nr din 5 in 5 pana la {x} este egala cu {sum_5_iter(x)}')
