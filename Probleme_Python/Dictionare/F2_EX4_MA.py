import math
a,b,c=float(input("a=")),float(input("b=")),float(input("c="))
def aria():
    global a
    global b    
    global c
    return math.sqrt((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))
def ha():
    global a
    global b    
    global c
    return 2*aria()/a
def hb():
    global a
    global b    
    global c
    return 2*aria()/b
def hc():
    global a
    global b    
    global c
    return 2*aria()/c
print("Inaltimea fata de latura a este egala cu",ha())
print("Inaltimea fata de latura b este egala cu",hb())
print("Inaltimea fata de latura c este egala cu",hc())
