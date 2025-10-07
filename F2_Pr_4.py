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
    return 