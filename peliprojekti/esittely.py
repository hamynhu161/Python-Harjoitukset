from peli import Huone, Esine, Pelaaja

#Luo kolme erillistä huonetta tai teemaa, joista pelaaja voi valita seikkailun aloituspaikan
def luo_huoneet():
    esine1 = Esine("miekka", 1.5)
    esine2 = Esine("kompassi", 0.3)
    esine3 = Esine("taskulamppu", 0.7 )

    huoneet = [Huone("Metsäseikkailu", esine1), Huone("Meriseikkailu", esine3), Huone("Aavikko", esine2)]
    return huoneet

#Luo asetukset-funktio, jonka avulla pelaaja voi muuttaa äänenvoimakkuutta tai kirkkautta.
def asetukset():
    ääni = input("Anna sopiva äänenvoimakkuus: ")
    kirkkaus = input("Ann sopiva kirkkaus: ")
    print(f"Asetukset tallennettu: ääni {ääni}, kirkkaus: {kirkkaus}")

#Luo tulostaulukko-funktio, jonka avulla pelaaja voi nähdä oman sijoituksen.
def tulostaulukko(pisteet, pelaaja, pelaajat):
    print(f"Pelilla on {len(pelaajat)} pelaajaa.")
    
    pisteet.append(pelaaja.piste)
    print(f"Paras pistemäärä on: {max(pisteet)}")
    print(f"Sinun pistemäärä on: {pelaaja.piste}")

#Luo aloitus-funktio, jossa pelaaja voi valita haluamansa teeman tai huoneen ja aloittaa seikkailun        
def aloitus(pelaaja, teemat):
    print(f"Mitä teemaa, joka kiinnostaa sinua eniten!")
    print(f" 1. Metsäseikkailu \n 2. Meriseikkailu \n 3. Aavikko")
    
    uusi_huone = int(input("Valinta on: "))
    
    print("-------")

    if uusi_huone == 1:
        pelaaja.liiku(teemat[0])
    elif uusi_huone == 2:
        pelaaja.liiku(teemat[1])
    elif uusi_huone == 3:
        pelaaja.liiku(teemat[2])
    else:
        print("Valitset uudelleen.")
        return                          #loppuu funktio
    
    pelaaja.keraa_esine()               #kutsutaan kun valinta on 1-3

#main()-funktio näyttää pelin kulun 
def main():
    nimi = input("Anna sinun nimesi: ")
    ikä = int(input("Anna sinun ikäsi: "))

    pelaaja = Pelaaja(nimi, [], None)
    teemat = luo_huoneet()
    pelaajat = ["Anna", "Teemu", "Hanna", "Aatu"]   #oletetaan, että tämä on aiemmin tallennettu pelaajien tieto
    pisteet = [100,232,554,321,98]                  #oletetaan, että tämä on aiemmin tallennettu pelaajien tieto
    pelaajat.append(pelaaja) 
    
    if ikä < 12:
        print(f"Olet alaikäinen. Peli suljetaan.")
        return
    else:
        print(f"Tervetuloa {pelaaja}!")
    
    while True:
        print("-------")
        print("Päävalikko: \n1. Asetukset \n2. Aloitus \n3. Tulostaulukko")
        komento = input("Anna komento: ")
        print("-------")
        if komento == "1":
            asetukset()
        elif komento == "2":
            aloitus(pelaaja, teemat)
        elif komento == "3":
            tulostaulukko(pisteet, pelaaja, pelaajat)
        elif komento == "lopeta":
            break   
        else:
            print(f"Tuntematon komento. Valitset uudelleen.")       

if __name__=="__main__":
    main()




