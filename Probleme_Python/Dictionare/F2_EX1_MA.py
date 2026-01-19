a,b,c,d=int(input("a=")),int(input("b=")),int(input("c=")),int(input("d="))
def exista_triunghi(a, b, c, d):
    def triunghi(x, y, z):
        return x + y > z and x + z > y and y + z > x

    if triunghi(a, b, c):
        return f"{a}, {b}, {c} pot fi laturi"
    if triunghi(a, b, d):
        return f"{a}, {b}, {d} pot fi laturi"
    if triunghi(a, c, d):
        return f"{a}, {c}, {d} pot fi laturi"
    if triunghi(b, c, d):
        return f"{b}, {c}, {d} pot fi laturi"
    return "Nicio combinatie nu poate forma un triunghi"

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
d = int(input("d="))

print(exista_triunghi(a, b, c, d))
