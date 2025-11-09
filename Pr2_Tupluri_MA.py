data=(9, 11, "duminică")
zile=["miercuri", "joi", "vineri", "sâmbătă", "duminică", "luni","marți"]
zi_an=313
for i in range(7):
    if zile[i]==data[2]:
        if zi_an%7>i:
            nr=zi_an//7+1
        else:
            nr=zi_an//7
        print("Au fost",nr,"zile de",data[2])
