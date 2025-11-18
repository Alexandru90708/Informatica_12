def dictionairy_1():    
    key_value = {}        
    key_value[2] = 56    
    key_value[1] = 2    
    key_value[5] = 12    
    key_value[4] = 24    
    key_value[6] = 18    
    key_value[3] = 323
    print('key_value', key_value)
    for i in sorted(key_value.keys()):        
        print(i, end=" ")
    print()
    print(':cheile sortate in ordine crescatoare.')
def dictionairy_2():    
    key_value = {}        
    key_value[2] = 56    
    key_value[1] = 2    
    key_value[5] = 12    
    key_value[4] = 24    
    key_value[6] = 18    
    key_value[3] = 323
    for i in sorted(key_value.keys()):        
        print(i, end=" ")
    print()
    print(':valorile sortate in ordine crescatoare dupa cheie (implicit).')
def dictionairy_3():
    key_value = {}        
    key_value[2] = 56    
    key_value[1] = 2    
    key_value[5] = 12    
    key_value[4] = 24    
    key_value[6] = 18    
    key_value[3] = 323

    for k in sorted(key_value, key=lambda x: key_value[x]):
        print(key_value[k], end=" ")
    print()
    print(":valorile sortate in ordine crescatoare dupa valoare.")
def dictionairy_4():
    key_value = {}        
    key_value[2] = 56    
    key_value[1] = 2    
    key_value[5] = 12    
    key_value[4] = 24    
    key_value[6] = 18    
    key_value[3] = 323

    rezultat = sorted(key_value.items(), key=lambda x: x[1])
    print(rezultat)
    print(":lista tuplurilor sortata dupa valoare.")
def main():   
    dictionairy_1()
    dictionairy_2()
    dictionairy_3()
    dictionairy_4()
if __name__ == "__main__":    
    main()