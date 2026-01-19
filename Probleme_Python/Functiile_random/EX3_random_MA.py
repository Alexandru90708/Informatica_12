import random
nr=round(random.random()*10**9)
print(nr)
nr=str(nr)
n0,n1,n2,n3,n4,n5,n6,n7,n8,n9=0,0,0,0,0,0,0,0,0,0
for i in nr:
    if int(i)==0:
        n0+=1
    if int(i)==1:
        n1+=1
    if int(i)==2:
        n2+=1
    if int(i)==3:
        n3+=1
    if int(i)==4:
        n4+=1
    if int(i)==5:
        n5+=1
    if int(i)==6:
        n6+=1
    if int(i)==7:
        n7+=1
    if int(i)==8:
        n8+=1
    if int(i)==9:
        n9+=1
print('0 apare de ',n0,'ori')
print('1 apare de ',n1,'ori')
print('2 apare de ',n2,'ori')
print('3 apare de ',n3,'ori')
print('4 apare de ',n4,'ori')
print('5 apare de ',n5,'ori')
print('6 apare de ',n6,'ori')
print('7 apare de ',n7,'ori')
print('8 apare de ',n8,'ori')
print('9 apare de ',n9,'ori')
    
