x = int(input('x = '))
def fibonacci_recursiv(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursiv(n-1) + fibonacci_recursiv(n-2)
print(f'Elementul cu nr {x} din sirul Fibonacci este {fibonacci_recursiv(x)}')
def fibonacci_iterativ_elem(n):  
    if n == 0: return 0
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b
print(f'Elementul cu nr {x} din sirul Fibonacci este {fibonacci_iterativ_elem(x)}')
