m1,m2=float(input("Introduceți masa de apă1:")),float(input("Introduceți masa de apă2:"))
T1,T2=float(input("Introduceți temperatura inițială1:")),float(input("Introduceți temperatura inițială2:"))
Tf=(m1*T1+m2*T2)/(m1+m2)
print('După ce amestecăm două cantități de apă cu masele de',m1,'kg și respectiv',m2,'kg și la temperaturile inițiale de',T1,'grade celsius și respectiv',T2,'grade celsius obținem o cantitate de apă cu temperatura de',Tf,'de grade celsius.')
