import math
n=int(input('n='))
an=0
if n<0:
    print('Valoarea lui n nu corespunde cerintei.')
elif n>=0:
    an=(pow((1+math.sqrt(5))/2,n+1)-pow((1-math.sqrt(5))/2,n+1))/math.sqrt(5)
    print('Valoarea lui a de',n, 'este egala cu',int(an))
