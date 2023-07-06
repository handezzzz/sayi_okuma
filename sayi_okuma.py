def sayi_okunus_fonk(sayi):
    
        #sayi, ondalik_sayi = str(sayi).split(".")
        
    sayi_okunus = {1 : "bir",
                   2 : "iki",
                   3 : "uc",
                   4 : "dort",
                   5 : "bes",
                   6 : "alti",
                   7 : "yedi",
                   8 : "sekiz",
                   9 : "dokuz"
                   }
    
    sayi_okunus_onlar = {1 : "on",
                         2 : "yirmi",
                         3 : "otuz",
                         4 : "kirk",
                         5 : "elli",
                         6 : "altmis",
                         7 : "yetmis",
                         8 : "seksen",
                         9 : "doksan"
                         }
    
    sayilar = []
    b=0
    while(int(sayi) > 0):
        a = int(sayi) % 10
        sayilar.append(a)
        sayi = int(sayi) / 10   
        b+=1
        
    sayilar.reverse()
    
    for i in sayilar:
        if(b==2):
            print(sayi_okunus_onlar[i])
            b-=1
            
        else:
            print(sayi_okunus[i])
            if(b==4):
                print("bin")
            if(b==3):
                print("yuz")
            b-=1

sayi = input()
sayi_okunus_fonk(sayi)
        
        
        
        
        
            
            
            
            
        
