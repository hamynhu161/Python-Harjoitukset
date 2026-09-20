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
    
    # kulje metodi kasvattaa kuljettua matkaa
    def kulje (self, tuntimaara):
        self.kuljettuMatka += tuntimaara * self.tamanhetkinenNopeus
        
auto1 = Auto("ABC-123", 142)

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
print(f"Auton nopeus nyt: {auto1.tamanhetkinenNopeus} km/h.")
auto1.kiihdytä(-200)
print(f"Auton nopeus nyt: {auto1.tamanhetkinenNopeus} km/h.")
