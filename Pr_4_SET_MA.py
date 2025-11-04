A = {1, 2, 3, 'A', 'B', 'C'}
elemente=list(A)
print("Submulțimile mulțimii A sunt:\n")
n = len(elemente)
for i in range(2 ** n):   
    submultime = set()
    for j in range(n):
        if i & (1 << j):  
            submultime.add(elemente[j])
    print(submultime)
