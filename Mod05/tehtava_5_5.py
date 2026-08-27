k = 0

while k < 5: 
    käyttäjätunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if käyttäjätunnus != "python" or salasana != "rules":
        print("Tarkistetaan käyttäjätunnus ja salasana uudelleen.")
        k = k + 1
    else:
        print("Tervetuloa")
        break

if k == 5:
    print("Pääsy evätty")
    
    
      
