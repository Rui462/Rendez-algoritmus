import os

def valasztas():
    menupont = 0
    flag = 0
    print("\n\nMit szeretnél csinálni?\n\n1 - Felhasználók listázása\n2 - Termékek listázása\n3 - Rendelési előzmények listázása\n4 - Algoritmus használata\n\n")
    while(flag==0):
        valasztas = input("Menüpont: ")
        if valasztas=='1':
            menupont = 1
            flag=1
        elif valasztas=='2':
            menupont = 2
            flag=1
        elif valasztas=='3':
            menupont = 3
            flag=1
        elif valasztas=='4':
            menupont = 4
            flag=1
        else:
            print("Hibás a megadott menüpont!")
    
    return menupont

def felhasznalolistazas():
    fajl = open("felhasznalok/users.txt","r")
    print("Felhasználónév\tEmail cím\tTelefonszám\n")
    for x in fajl:
        x = x.strip().split()
        print(f"{x[0]}\t{x[1]}\t{x[2]}")
    fajl.close()
    print("----------------------")
    menupont(valasztas())

def termeklistazas():
    fajl = open("termekek/termekek.txt","r")
    print("Terméknév\tKategória\n")
    for x in fajl:
        x = x.strip().split()
        print(f"{x[0]}\t{x[1]}")
    fajl.close()
    print("----------------------")
    menupont(valasztas())

def rendeleslistazas():
    fajl = open("felhasznalok/userhistory.txt","r")
    print("Felhasználó\tRendelés azonosító\tTermék\n")
    for x in fajl:
        x = x.strip().split()
        print(f"{x[0]}\t{x[1]}\t{x[2]}")
    fajl.close()
    print("----------------------")
    
    menupont(valasztas())

def elozmenyalgo(fnev):
    fajl = open("felhasznalok/userhistory.txt","r")
    lista = []
    listaset = set()
    for x in fajl:
        x = x.strip().split()
        if x[0]==fnev:
            lista.append(x[2])
            listaset.add(x[2])
    fajl.close()
    
    osszetett = []
    
    for i in listaset:
        db = 0
        for x in range(len(lista)):
            if lista[x]==i:
                db+=1
        osszetett.append([i,db])
        
        for i in range(0, len(osszetett)):
            for j in range(0, len(osszetett)-i-1):
                if (osszetett[j][1] > osszetett[j + 1][1]):
                    tempo = osszetett[j]
                    osszetett[j] = osszetett[j + 1]
                    osszetett[j + 1] = tempo
            
    osszetett = osszetett[::-1]
    
    if len(osszetett)>=5:
        print()
        for i in range(5):
            print(f"{i+1}. {osszetett[i][0]} - ({osszetett[i][1]} db rendelt)")
    else:
        print("KEVESEBB MINT 5 TERMÉKET RENDELT A FELHASZNÁLÓ (Előzmény alapján kiíratjuk amit lehet)")
        print()
        for i in range(len(osszetett)):
            print(f"{i+1}. {osszetett[i][0]} - ({osszetett[i][1]} db rendelt)")   

def toptermekek():
    fajl = open("felhasznalok/userhistory.txt","r")
    lista = []
    listaset = set()
    for x in fajl:
        x = x.strip().split()
        lista.append(x[2])
        listaset.add(x[2])
    fajl.close()
    
    osszetett = []
    
    for i in listaset:
        db = 0
        for x in range(len(lista)):
            if lista[x]==i:
                db+=1
        osszetett.append([i,db])
        
        for i in range(0, len(osszetett)):
            for j in range(0, len(osszetett)-i-1):
                if (osszetett[j][1] > osszetett[j + 1][1]):
                    tempo = osszetett[j]
                    osszetett[j] = osszetett[j + 1]
                    osszetett[j + 1] = tempo
            
    osszetett = osszetett[::-1]
    
    if len(osszetett)>=5:
        print()
        for i in range(5):
            print(f"{i+1}. {osszetett[i][0]} - ({osszetett[i][1]} db rendelt)")
    else:
        print("KEVESEBB MINT 5 TERMÉK VOLT RENDELVE A WEBSHOPBAN (Előzmény alapján kiíratjuk amit lehet)")
        print()
        for i in range(len(osszetett)):
            print(f"{i+1}. {osszetett[i][0]} - ({osszetett[i][1]} db rendelt)")   
            

def termekalgo(termek):
    fajl = open("felhasznalok/userhistory.txt","r")
    termekek = [] 
    listaset = set()
    for x in fajl:
        x = x.strip().split()
        if x[2]==termek:
            listaset.add(x[1])
        termekek.append(x)
    fajl.close()
    
    szukitettlista = []
    
    for i in listaset:
        for x in termekek:
            if i==x[1] and x[2]!=termek:
                szukitettlista.append(x)
    
    szukitettset = set()
    
    for i in szukitettlista:
        szukitettset.add(i[2])
    
    aktualis = []
    
    for i in szukitettset:
        db=0
        for x in szukitettlista:
            if x[2]==i:
                db+=1
        aktualis.append([i, db])
        
    for i in range(0, len(aktualis)):
        for j in range(0, len(aktualis)-i-1):
            if (aktualis[j][1] > aktualis[j + 1][1]):
                tempo = aktualis[j]
                aktualis[j] = aktualis[j + 1]
                aktualis[j + 1] = tempo
            
    aktualis = aktualis[::-1]
    hossz = len(aktualis)
    
    if hossz>=5:
        print()
        for i in range(5):
            print(f"{i+1}. {aktualis[i][0]}")
    else:
        print("KEVESEBB MINT 5 KAPCSOLÓDÓ TERMÉK VOLT RENDELVE. (KIÍRUNK ANNYIT AMENNYIT LEHET)")
        print()
        for i in range(hossz):
            print(f"{i+1}. {aktualis[i][0]}")
    

def algoritmusok():
    fajl = open("felhasznalok/users.txt","r")
    felhasznalonevek = [] 
    for x in fajl:
        x = x.strip().split()
        felhasznalonevek.append(x[0])
    fajl.close()
    flag = 0
    while(flag==0):
        fnev = input("Add meg egy felhasználónak a nevét: ")
        
        if fnev not in felhasznalonevek:
            print("!! NINCS ILYEN FELHASZNÁLÓ !!")
        else:
            flag = 1
            print(100*"\n")
            print(f"A kiválasztott felhasználó: [{fnev}]")
            
    if flag==1:
        print("----------------------\n")
        print("Top 5 termék felhasználói előzmény alapján:")
        elozmenyalgo(fnev)
        print()
        print("----------------------\n")
        print("Top 5 termék az összes felhasználó előzményei alapján (TOP TERMÉKEK):")
        toptermekek()
        print()
        print("----------------------\n")
        print("Top 5 termék amit megadott termékkel együtt szoktak venni: ")
        termeknev = input("Add meg egy termék nevét: ")
        termekalgo(termeknev)
        print("----------------------\n")
        menupont(valasztas())
    
def menupont(menu):
    print(100*"\n")
    if menu==1:
        print("FELHASZNÁLÓK LISTÁZÁSA")
        print("----------------------")
        felhasznalolistazas()
    if menu==2:
        print("TERMÉKEK LISTÁZÁSA")
        print("----------------------")
        termeklistazas()
    if menu==3:
        print("RENDELÉSI ELŐZMÉNYEK LISTÁZÁSA")
        print("----------------------")
        rendeleslistazas()
    if menu==4:    
        algoritmusok()

print("TERMÉK RENDEZŐ ALGORITMUS")
print("by: Tátrai Péter")
print("=========================")

menupont(valasztas())
    