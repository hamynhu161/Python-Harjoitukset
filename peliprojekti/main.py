from peli import Huone, Esine, Pelaaja, Hahmo, Tiedot, asetukset, tulostaulukko
import random

# luo kolme erillistä huonetta (teemaa), joista pelaaja voi valita seikkailun aloituspaikan
def luo_huoneet():
    esine1 = Esine("Miekka", 1.5)
    esine2 = Esine("Sytytin", 0.07)
    esine3 = Esine("Tikari", 0.6)
    esine4 = Esine("Köysi", 0.12)
    esine5 = Esine("Taskulamppu", 0.7)
    esine6 = Esine("Vesipullo", 0.3)
    
    hahmo1 = Hahmo("Karhu", "Iso ja nälkäinen hyökkäjä!")
    hahmo2 = Hahmo("Käärme", "Myrkyllinen käärme luikertelee tiellesi!")
    hahmo3 = Hahmo("Hai", "Hiljainen mutta vaarallinen hyökkääjä")
    hahmo4 = Hahmo("Kameli", "Janoinen kameli tarvitsee vettä.")
    hahmo5 = Hahmo("Kissa", "On jäänyt loukkuun pensaikkoon.")
    hahmo6 = Hahmo("Meritähti", "Jäänyt loukkuun merileväkasaan ja tarvitsee apua.")

    huoneet = [Huone("Metsä", [esine1, esine4], [hahmo1, hahmo5]), Huone("Meri", [esine3, esine5], [hahmo3, hahmo6]), Huone("Aavikko", [esine2, esine6], [hahmo2, hahmo4])]
    return huoneet    

# palauta mitä pelaaja haluaa tehdä ensin pelissä
def valikko(ohjeet):
    while True:
        print("-------")
        print("Päävalikko: \n1. Asetukset \n2. Lue ohjeet \n3. Aloitus \n4. Tulostaulukko \n5. Lopeta")
        
        komento = input("Anna komento: ")
        print("-------")
        
        if komento == "1":
            asetukset()
        elif komento == "2":
            ohjeet.lue_tiedosto()
        elif komento in ["3", "4", "5"]:
            return komento
        else:
            print(f"Tuntematon komento. Valitset uudelleen.")  

# tarkista pelaajan tilanteen ja mahdollisesti jatkaa peliä
def alkukohta(pelaaja, pelaajat, teemat):
    if pelaaja.tarkista_pelaaja(pelaajat, teemat):
        print(f"\nTervetuloa takaisin {pelaaja.nimi}!")
        print(f"Sinulla oli {len(pelaaja.esineet)} esinettä, {pelaaja.piste.piste} pistettä ja {pelaaja.vinkki_maara} vinkkiä. Viimeisin seikkailusi oli {pelaaja.sijainti.nimi}.")
        
        # jos viimeinen seikkailu on vielä kesken
        if pelaaja.vinkki_maara < 2:
            kysy = input("\nHaluatko jatkaa viimeistä seikkailua (k/e)? ")  
            if kysy == "k":  
                return True
    else:
        print(f"\nTervetuloa {pelaaja.nimi}!")
        print(f"Osallistutaan seikkailuja ja tulkitaan salaisuusta näissä kiinnostuneissa seikkailuissa.")
        
    return False

# pelaaja valitsee seikkailun teeman ja aloittaa uuden seikkailun 
def aloitus(pelaaja, teemat):
    # tyhjennä pelaajan aiemmat tiedot
    pelaaja.esineet.clear()
    pelaaja.piste.nollaa_piste()
    pelaaja.vinkki_maara = 0  
    
    # valitse teema   
    print(f"\nMitä teemaa, joka kiinnostaa sinua eniten!")
    print(f" \n1. Metsä-seikkailu \n2. Meri-seikkailu \n3. Aavikko-seikkailu")
    while True:
        try:
            uusi_huone = int(input("Valinta on: "))
            print("-------")
            if uusi_huone == 1:
                pelaaja.liiku(teemat[0])
                break
            elif uusi_huone == 2:
                pelaaja.liiku(teemat[1])
                break
            elif uusi_huone == 3:
                pelaaja.liiku(teemat[2])
                break
            else:
                print("Valitset uudelleen.")                   
        except ValueError:
            print("Anna valinta numerona 1-3!")
        
# pelataan seikkailu ja käsitellään satunnaiset tapahtumat 
def kulku_peli(pelaaja, tulokset, tallennus, tulos_tiedot):
    while True:
        # pelaaja etenee satunnaisen määrän askelia
        tapahtu = random.randint(1,6)       
        print(f"\nMennään {tapahtu} askelta eteenpäin.\n")
        
        # pelaaja kohtaavat satunnaisia ​​haasteita tai ongelmia
        if tapahtu == 1:
            if pelaaja.sijainti.hahmot[0] is not None:
                hahmo = pelaaja.sijainti.hahmot[0]
                hahmo.tulosta_tieto()
                print("Varo! Se voi syödä sinut ennen kuin ehdit tutkia tämän seikkailun salaisuuksia.")
                print(f"Voit suojella itseäsi käyttämällä jotakin esinettä.")
                pelaaja.tulosta_esineet()
                print("")
                hahmo.hyökkää_hahmo(pelaaja)               
            else:
                print("Tässä on rauhallinen ja turvallinen.")
        elif tapahtu == 2:
            if pelaaja.sijainti.hahmot[1] is not None:
                hahmo = pelaaja.sijainti.hahmot[1]
                hahmo.tulosta_tieto()
                hahmo.autettava_hahmo(pelaaja)
            else:
                print("Täältä ei löydy enää vinkkejä.")
        elif tapahtu == 3:
            if pelaaja.sijainti.esineet[0] not in pelaaja.esineet:
                pelaaja.keraa_esine(pelaaja.sijainti.esineet[0])
            else:
                print("Tässä on yhden esine. Sinulla on jo tämä esine. Täästä ei löyty enää mitään.")
        elif tapahtu == 4:
            if pelaaja.sijainti.esineet[1] not in pelaaja.esineet:
                pelaaja.keraa_esine(pelaaja.sijainti.esineet[1])
            else:
                print("Sinulla on jo tämä esine. Täästä ei löyty mitään.")         
        elif tapahtu == 5:
            pelaaja.loyta_vinkki()
        else:
            pelaaja.meneta_esine()
            
        # tallenna pelaajan nykyinen tilanne jokaisen tapahtuman jälkeen
        tallennus.tallenna_tiedot(pelaaja)
        
        # pelaaja voittaa, jos hän kerää 2 vinkkiä
        if pelaaja.vinkki_maara >= 2:
            tulokset.append([pelaaja.nimi, pelaaja.sijainti.nimi, pelaaja.piste.piste])
            tulos_tiedot.tallenna_tulos(tulokset)
            print("-----")
            print(f"Olet kerännyt {pelaaja.vinkki_maara}. Se riittää! Seuraa vihjeitä, niin löydät yllätyksen.")
            break
         
    if pelaaja.sijainti.nimi == "Metsä":
        print("\nOnnea! Löysit piilotettu puumaja. Tutki paikkaa rauhassa ja lisää löytö omaan seikkailupäiväkirjaasi.")
    elif pelaaja.sijainti.nimi == "Meri":
        print("\nOnnea! Löysit Aarrekartta. Tutki paikkaa rauhassa ja lisää löytö omaan seikkailupäiväkirjaasi.")
    elif pelaaja.sijainti.nimi == "Aavikko":
        print("\nOnnea! Löysit kadonnut keidas. Tutki paikkaa rauhassa ja lisää löytö omaan seikkailupäiväkirjaasi.")
    print(f"\nKokonaispisteesi tästä teemasta ovat {pelaaja.piste.piste}.")
                         
def main():
    tallennus = Tiedot("peliprojekti/tallennetut_peli.txt")
    tulos_tiedot = Tiedot("peliprojekti/tallennetut_tulos.txt")
    ohjeet = Tiedot("peliprojekti/ohjeet.txt")
    intro = Tiedot("peliprojekti/intro.txt")

    # näytä intro pelissä
    intro.lue_tiedosto()
    
    # lataa data pelille
    teemat = luo_huoneet()
    pelaajat = tallennus.lataa_tiedot()
    tulokset = tulos_tiedot.lataa_tulos()
    
    # kerää pelaajan tiedot
    nimi = input("\nAnna sinun nimesi: ")
    ikä = int(input("Anna sinun ikäsi: "))
    
    # luo pelaaja-olio
    pelaaja = Pelaaja(nimi, [], None)
    
    # tarkista pelajaan ikä, eli peli sopii kouluaikaiselle tai enemmän
    while True:    
        try:
            if ikä < 6:
                print(f"Olet alaikäinen. Peli suljetaan.")
                return
            else:
                break
        except ValueError:
            print("Anna ikä numerona!")
    
    # pelaaja haluaa jatkaa viimeistä seikkailua
    jatka = alkukohta(pelaaja, pelaajat, teemat)
    if jatka:
        kulku_peli(pelaaja, tulokset, tallennus, tulos_tiedot)
        
    # näytetään päävalikko
    while True:
        komento = valikko(ohjeet)
        
        if komento == "3":
            aloitus(pelaaja, teemat)
            kulku_peli(pelaaja, tulokset, tallennus, tulos_tiedot)
        elif komento == "4":
            tulostaulukko(tulokset)
        elif komento == "5":
            break        
    
if __name__=="__main__":
    main()




