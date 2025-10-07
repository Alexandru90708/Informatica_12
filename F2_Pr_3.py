import math
a,b,c=float(input("a=")),float(input("b=")),float(input("c="))
def mediana_a():
    global a
    global b    
    global c
    return 0.5 * (math.sqrt(2 * b**2 + 2 * c**2 - a**2))

def mediana_b():
    global a
    global b    
    global c
    return 0.5 * (math.sqrt(2 * a**2 + 2 * c**2 - b**2))

def mediana_c():
    global a
    global b    
    global c
    return 0.5 * (math.sqrt(2 * b**2 + 2 * a**2 - c**2))
print("Mediana laturii a=",mediana_a())
print("Mediana laturii b=",mediana_b())
print("Mediana laturii c=",mediana_c())