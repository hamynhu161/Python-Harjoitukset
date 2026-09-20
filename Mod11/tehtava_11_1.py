class Julkaisu:
    julkaisu_lukumaara = 0
    
    def __init__(self, nimi):
        Julkaisu.julkaisu_lukumaara = Julkaisu.julkaisu_lukumaara + 1
        self.julkaisu_numero = Julkaisu.julkaisu_lukumaara
        self.nimi = nimi
    
    def tulosta_tiedot(self):
        print(f"{self.julkaisu_numero}: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
    
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}, {self.sivumaara} sivua.")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja
    
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.päätoimittaja}")

julkaisut = []

julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for i in julkaisut:
    i.tulosta_tiedot()