from peli import Huone, Esine, Pelaaja, Hahmo, Tiedot, asetukset, tulostaulukko, ladaa_tulos
import random

def luo_ohjeet():
    with open ("ohjeet.txt", "w") as tiedosto:
        tiedosto.write("""
            Seikkailun aikana kohtaat erilaisia tapahtumia yllättäen.
            Lue tehtävät ja viestit huolellisesti ja tee tilanteeseen sopiva valinta.
            Kerää hyödyllisiä esineitä, käytä niitä oikeissa tilanteissa ja etsi vihjeitä. 
            Kun olet saanut tarpeeksi vihjeitä, voit löytää seikkailun salaisuuden.""")
    return "ohjeet.txt"

def luo_intro():
    with open("intro.txt", "w") as tiedosto:
        tiedosto.write("""
            Tervetuloa Questoraan!
            Lähde seikkailumatkalle ja tutki erilaisia maailmoja. 
            Jokaisessa seikkailussa tavoitteena on löytää alueen salaisuus ja kirjoittaa löytö omaan seikkailupäiväkirjaasi.
            Jokainen askel voi tuoda eteesi uuden yllätyksen: voit löytää esineitä, kohdata hahmoja, tai saada vihjeitä.""")
    return "intro.txt"

# Luo kolme erillistä huonetta (teemaa), joista pelaaja voi valita seikkailun aloituspaikan
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

# Luo aloitus-funktio, jossa pelaaja voi valita haluamansa teeman tai huoneen ja aloittaa seikkailun        
def aloitus(pelaaja, teemat):
    # tyhjennä pelaajan aiemmat tiedot
    pelaaja.esineet.clear()
    pelaaja.piste.nollaa_piste()
    pelaaja.vinkki_maara = 0  
     
    # valitse teema   
    print(f"\nMitä teemaa, joka kiinnostaa sinua eniten!")
    print(f" 1. Metsä-seikkailu \n 2. Meri-seikkailu \n 3. Aavikko-seikkailu")
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
        
# Aloitetaan seikkailu    
def kulku_peli(pelaaja, tallennus):
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
            print("-----")
            print(f"Olet kerännyt {pelaaja.vinkki_maara}. Se riittää! Seuraa vihjeitä, niin löydät yllätyksen.")
            break
         
    if pelaaja.sijainti.nimi == "Metsäseikkailu":
        print("\nOnnea! Löysit piilotettu puumaja. Tutki paikkaa rauhassa ja lisää löytö omaan seikkailupäiväkirjaasi.")
    elif pelaaja.sijainti.nimi == "Meriseikkailu":
        print("\nOnnea! Löysit Aarrekartta. Tutki paikkaa rauhassa ja lisää löytö omaan seikkailupäiväkirjaasi.")
    elif pelaaja.sijainti.nimi == "Aavikko":
        print("\nOnnea! Löysit kadonnut keidas. Tutki paikkaa rauhassa ja lisää löytö omaan seikkailupäiväkirjaasi.")
    print(f"\nKokonaispisteesi tästä teemasta ovat {pelaaja.piste.piste}.")
                         
def main():
    tallennus = Tiedot("tallennetut_peli.txt")
    ohjeet = Tiedot("ohjeet.txt")
    intro = Tiedot("intro.txt")
    teemat = luo_huoneet()
    
    # näytä ohjeet ja intro pelissä
    luo_intro()
    luo_ohjeet()
    intro.lue_tiedosto()
    ohjeet.lue_tiedosto()
    
    pelaajat = tallennus.ladaa_tiedot()
    tulokset = ladaa_tulos()
        
    nimi = input("\nAnna sinun nimesi: ")
    ikä = int(input("Anna sinun ikäsi: "))
    pelaaja = Pelaaja(nimi, [], None)

    if pelaaja.tarkista_pelaaja(pelaajat, teemat):
        print(f"\nTervetuloa takaisin {pelaaja.nimi}!")
        print(f"Sinulla oli {len(pelaaja.esineet)} esinettä, {pelaaja.piste.piste} pistettä ja {pelaaja.vinkki_maara} vinkkiä. Viimeisin seikkailusi oli {pelaaja.sijainti.nimi}.")
        print("Jatketaan peliä.")
        if pelaaja.vinkki_maara == 2:
            aloitus(pelaaja, teemat)
            kulku_peli(pelaaja, tallennus)
        else:    
            kulku_peli(pelaaja, tallennus)
    else:
        print(f"\nTervetuloa {pelaaja.nimi}!")
        print(f"Osallistutaan seikkailuja ja tulkitaan salaisuusta näissä kiinnostuneissa seikkailuissa.")
    
    while True:    
        try:
            if ikä < 6:
                print(f"Olet alaikäinen. Peli suljetaan.")
                return
            else:
                break
        except ValueError:
            print("Anna ikä numerona!")
        
    while True:
        print("-------")
        print("Päävalikko: \n1. Asetukset \n2. Aloitus \n3. Tulostaulukko")
        komento = input("Anna komento: ")
        print("-------")
        if komento == "1":
            asetukset()
        elif komento == "2":
            aloitus(pelaaja, teemat)
            kulku_peli(pelaaja,tallennus)
            tulokset.append([pelaaja.nimi, pelaaja.sijainti.nimi, pelaaja.piste.piste])
        elif komento == "3":
            tulostaulukko(tulokset)
        elif komento == "lopeta":
            break   
        else:
            print(f"Tuntematon komento. Valitset uudelleen.")     
    
if __name__=="__main__":
    main()




