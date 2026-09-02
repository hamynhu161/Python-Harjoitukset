nimi = input("Anna sinun nimesi: ")
ikä = int(input("Anna sinun ikäsi: "))

if ikä < 12:
    print(f"Olet alaikäinen. Peli suljetaan.")
else:
    print(f"Tervetuloa {nimi}!")
    
    while True:
        print("Päävalikon: \n1. Asetukset \n2. Aloitus \n3. Tulostaulukko")
        komento = input("Anna komento: ")
        if komento == "1":
            print("Tästä asetuksesta voi säätää musiikin ja äänien voimakkuutta.")
        elif komento == "2":
            print("Aloitetaan peli ja nautitaan siitä.")
        elif komento == "3":
            print("Tulostaulukosta näkyy oman sijoituksen ja parhaat pisteet.")
        elif komento == "lopeta":
            break
     