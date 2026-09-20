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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
         super().__init__(rekisteritunnus, huippunopeus)
         self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
         super().__init__(rekisteritunnus, huippunopeus)
         self.bensatankki = bensatankki
         
sahkoauto = Sähköauto("ABC-15", 180, 52.5)
sahkoauto.kiihdytä(60)
sahkoauto.kulje(3)
print(f"{sahkoauto.rekisteritunnus}: autojen matkamittarilukemat {sahkoauto.kuljettuMatka} km.")
      
polttomoottoriauto = Polttomoottoriauto ("ACD-123", 165, 32.3)
polttomoottoriauto.kiihdytä(80)
polttomoottoriauto.kulje(3)
print(f"{polttomoottoriauto.rekisteritunnus}: autojen matkamittarilukemat {polttomoottoriauto.kuljettuMatka} km.")
  


    
             