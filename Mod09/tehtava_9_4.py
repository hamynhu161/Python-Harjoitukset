
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

# Luo lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta 
autot = []

for i in range(1,11):
    auto = Auto(("ABC-"+ str(i)), random.randint(100,200))
    autot.append(auto)
    print(f"Autolla on: rekistertunnus: {autot[i-1].rekisteritunnus}, huippunopeus: {autot[i-1].huippunopeus}")

# kilpailu: nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä yhden tunnin ajan
while True:
    for auto in autot:
        auto.kiihdytä(random.randint(-10,+15))
        auto.kulje(1)
    
    if auto.kuljettuMatka >= 10000:
        break

# tulosta kunkin auton kaikki ominaisuudet taulukoksi  
print(f"{"Rekisteritunnus":<15} {"Huippunopeus":<15} {"Nopeus":<10} {"Matka":<10}")
      
for auto in autot:
    print(f"{auto.rekisteritunnus:<15} {auto.huippunopeus:<15} {auto.tamanhetkinenNopeus:<10} {auto.kuljettuMatka:<10}")
