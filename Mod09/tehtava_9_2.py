class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
            self.rekisteritunnus = rekisteritunnus
            self.huippunopeus = huippunopeus
            self.tamanhetkinenNopeus = 0
            self.kuljettuMatka = 0
    
    # Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.        
    def kiihdytä (self, nopeudenmuutos):
        if self.tamanhetkinenNopeus + nopeudenmuutos <= 0:
            self.tamanhetkinenNopeus = 0
        elif self.tamanhetkinenNopeus + nopeudenmuutos >= self.huippunopeus:
            self.tamanhetkinenNopeus = self.huippunopeus
        else:
            self.tamanhetkinenNopeus += nopeudenmuutos

# luo auto1, auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.   
auto1 = Auto("ABC-123", 142)
auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
print(f"Autolla nyt on {auto1.tamanhetkinenNopeus} km/h.")

# hätäjarrutus määräämällä nopeuden muutos -200 km/h
auto1.kiihdytä(-200)
print(f"Autolla nyt on {auto1.tamanhetkinenNopeus} km/h.")