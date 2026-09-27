class Pelaaja:
    def __init__(self, nimi, esineet, sijainti):
        self.nimi = nimi
        self.esineet = esineet
        self.sijainti = sijainti
        self.piste = 0

    def liiku(self, huone):
        self.sijainti = huone
        print(f"Tervetuloa {self.nimi}. Olet {self.sijainti.nimi}-seikkailulla nyt.")

    def keraa_esine (self):
        self.esineet.append(self.sijainti.esine)
        self.piste += 200
        print(f"Keräsit esineen: {self.sijainti.esine.nimi}")


    
    