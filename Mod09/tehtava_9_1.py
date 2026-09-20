# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka. 
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. 

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinenNopeus = 0
        self.kuljettuMatka = 0

uuden_auto = Auto("ABC-123", 142)

print(f"Autolla {uuden_auto.rekisteritunnus} on huippunopeus {uuden_auto.huippunopeus} km/h. Tämänhetkinen nopeus on {uuden_auto.tamanhetkinenNopeus}. Kuljettu matka on {uuden_auto.kuljettuMatka}.")
        