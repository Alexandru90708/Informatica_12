V=int(input("Volumul rucsacului V = "))
n=int(input("Numarul de obiecte n = "))
v=[0]*n
p=[0]*n
print("Introduceti volumele v[i]:")
for i in range(n):
    v[i] = float(input(f"v[{i+1}] = "))
print("Introduceti preturile p[i]:")
for i in range(n):
    p[i] = float(input(f"p[{i+1}] = "))
raport = [(p[i] / v[i], v[i], p[i], i) for i in range(n)]
raport.sort(reverse=True, key=lambda x: x[0])
x=[0]*n
i=0
vt=0
pt=0
while vt < V and i < n:
    dens, vol, pret, idx = raport[i]
    if vt + vol <= V:
        x[idx] = 1
        pt = pt + pret
        vt = vt + vol
    else:
        x[idx] = (V - vt) / vol
        pt = pt + pret * x[idx]
        vt = V
    i += 1
print("\n-------------------------------------")
print("Pretul total al obiectelor din rucsac =", pt)
print("Volumul ocupat =", vt)
print("In rucsac s-au introdus: ")
for i in range(n):
    if x[i] > 0:
        print(f"- obiectul {i+1} (volum introdus: {v[i]*x[i]}, pret: {p[i]*x[i]})")
