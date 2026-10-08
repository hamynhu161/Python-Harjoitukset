from .piste import Piste
import random

class Pelaaja:   
    def __init__(self, nimi, esineet, sijainti):
        self.nimi = nimi
        self.esineet = esineet
        self.sijainti = sijainti
        self.piste = Piste()
        self.vinkki_maara = 0

    # tarkista tallennetut_peli-tiedostosta saman niminen pelaaja ja käytä hänen viimeisintä tallennustaan
    def tarkista_pelaaja(self,pelaajat, teemat):
        loytyi = False
        for rivi in pelaajat:
            if rivi[0] == self.nimi:
                tallennettu_esineet = rivi[1]
                tallennettu_sijainti = rivi[2]
                self.piste.piste = rivi[3]
                self.vinkki_maara = rivi[4]               
                #palautetaan sijainti Huone-olioksi
                for huone in teemat:
                    if huone.nimi == tallennettu_sijainti:
                        self.sijainti = huone
                        break               
                #palautetaan esineet Esine-olioksi
                self.esineet = []              
                for esine_nimi in tallennettu_esineet:
                    for huone in teemat:
                        for esine in huone.esineet:
                            if esine_nimi == esine.nimi:
                                self.esineet.append(esine)
                                break                   
                loytyi = True            
        return loytyi

    # Siirty valitettuun huoneeseen
    def liiku(self, huone):
        self.sijainti = huone
        print(f"Tervetuloa {self.nimi}. Olet {self.sijainti.nimi}-seikkailulla nyt.")
        
    def tulosta_esineet(self):
        print("")
        print(f"Sinulla on nyt {len(self.esineet)} esinettä.")
        
        for i in range(len(self.esineet)):
            print(f"{i+1}. {self.esineet[i].nimi}. Sen paino on {self.esineet[i].paino}")

    def keraa_esine(self, esine):
        while True:
            keraa = input("Löysit esineen! Haluatko ottaa sen mukaasi (k/e)? ")
            
            if keraa == "k":
                self.esineet.append(esine)
                self.piste.lisaa_piste(15)
                print(f"Keräsit esineen: {self.esineet[-1].nimi}")
                break
            elif keraa == "e":
                print("Et kerännyt esinettä.")
                break
            else:
                print("Virheellinen valinta. Valitset k tai e?")
    
    def meneta_esine(self):
        print("Varo! Yksi esineistäsi on putoamassa.")
        
        if self.esineet:
            menetetty_esine = random.choice(self.esineet)
            print(f"Oho! Menetit esineen: {menetetty_esine.nimi}.")
            self.esineet.remove(menetetty_esine)
            self.piste.vahenna_piste(15)
        else:
            print(f"Onneksi sinulla ei ollut mitään menetettävää.")
        
    def kayta_sopivaesine(self):
        if len(self.esineet) > 0:
            valittu_esine = input("Mitä esinettä haluat käyttää: ")
            print("")
            if valittu_esine == self.sijainti.esineet[0].nimi:
                print(f"Se on nyt hallinnassa. Sinä voitit käyttämällä {valittu_esine}")
                self.piste.lisaa_piste(30)
                return True
            else:
                print(f"Tuo vaarallinen eläin on liian voimakas. Sinun kannattaa käyttää myöhemmin jotakin toista esinettä.")
                self.piste.vahenna_piste(10)
                return False
        else:
            print("Kerää esine mukaasi. Saatat tarvita sitä myöhemmin suojautumiseen.")
            return False
        
    def loyta_vinkki(self):
        print("Onnea! Löysit vihjeen! Se auttaa sinua pääsemään lähemmäs tämän seikkailun salaisuutta.")
        self.vinkki_maara += 1
        print(f"Sait +1 vinkin.")
        self.piste.lisaa_piste(50)
        
        
        



    
    