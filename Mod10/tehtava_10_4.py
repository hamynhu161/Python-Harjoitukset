import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
            self.rekisteritunnus = rekisteritunnus
            self.huippunopeus = huippunopeus
            self.tamanhetkinenNopeus = 0
            self.kuljettuMatka = 0
            
    def kiihdytä (self, nopeudenmuutos):
        if self.tamanhetkinenNopeus + nopeudenmuutos <= 0:
            self.tamanhetkinenNopeus = 0
        elif self.tamanhetkinenNopeus + nopeudenmuutos >= self.huippunopeus:
            self.tamanhetkinenNopeus = self.huippunopeus
        else:
            self.tamanhetkinenNopeus += nopeudenmuutos
    
    def kulje (self, tuntimaara):
        self.kuljettuMatka += tuntimaara * self.tamanhetkinenNopeus
            
class Kilpailu:
    def __init__(self, nimi, kilometrimäärä, autot):
        self.nimi = nimi
        self.kilometrimäärä = kilometrimäärä
        self.autot = autot
    
    # luo metodi tuntu_kuluu, tunti_kuluu, joka arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10,+15))
            auto.kulje(1)
    
    # luo metodi tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
    def tulosta_tilanne (self):
        print(f"{"Rekisteritunnus":<15} {"Huippunopeus":<15} {"Nopeus":<10} {"Matka":<10}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<15} {auto.huippunopeus:<15} {auto.tamanhetkinenNopeus:<10} {auto.kuljettuMatka:<10}")

    # luo metodi kilpailu_ohi, joka palauttaa True, jos se on ajanut vähintään kilpailun kokonaiskilometrimäärän
    def kilpailu_ohi(self):
        if auto.kuljettuMatka >= self.kilometrimäärä:
            return True
        else:
            return False
            
autot = []
for i in range(1,11):
    auto = Auto(("ABC-"+ str(i)), random.randint(100,200))
    autot.append(auto)
    
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

# Ajantasainen tilanne tulostetaan kymmenen tunnin välein sekä kertaalleen sen jälkeen
tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()

# Ajantasainen tilanne tulostetaan kun kilpailu päättynyt.
kilpailu.tulosta_tilanne()