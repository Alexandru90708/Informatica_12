x = int(input('x = '))
def factorial_recursiv(a):
    if a==0:
        return 1
    if a==1:
        return 1
    return a*factorial_recursiv(a-1)
print(f'Factorialul nr {x} = {factorial_recursiv(x)}')
def factorial_iterativ(a):
    product = 1
    for i in range(1,a+1):
        product*=i
    return product
print(f'Factorialul nr {x} = {factorial_iterativ(x)}')
