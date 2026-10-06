from .pelaaja import Pelaaja

class Hahmo:
    def __init__(self, nimi, kuvaus):
        self.nimi = nimi
        self.kuvaus = kuvaus
    
    def tulosta_tieto(self):
        print(f"{self.nimi} ilmestyy. {self.kuvaus}")
        print("")
        
    def hyökkää_hahmo(self, pelaaja):
        if pelaaja.kayta_sopivaesine():
            pelaaja.sijainti.hahmot[0] = None
        else:
            print("Et pystynyt puolustautumaan.")
            
    def autettava_hahmo(self, pelaaja):
        while True:
            kysy = input("\nTämä eläin näyttää tarvitsevan apua. Haluatko auttaa sitä (k/e)? ")
            
            if kysy == "k":
                print("\nKiitos avustasi! Sait sen turvaan. Se jätti sinulle merkin, joka johdattaa seuraavan vihjeen luo.")
                pelaaja.loyta_vinkki()
                pelaaja.sijainti.hahmot[1] = None
                break
            elif kysy == "e":
                break
            else:
                print("Tuntematon komento. Valitset uudelleen.")
        
    
   
        