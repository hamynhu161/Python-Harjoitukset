class Tiedot:
    def __init__(self, tiedot):
        self.tiedot = tiedot

    def lue_tiedosto(self):
        try:
            with open(self.tiedot, "r") as tiedosto:
                print(tiedosto.read())
        except FileNotFoundError:
            return "Tiedosto ei löytynyt."       
                
    def tallenna_tiedot(self,pelaaja):
        # tallentaa tiedostoon esineiden nimet
        if pelaaja.esineet is not None:
            esine_nimet = [esine.nimi for esine in pelaaja.esineet]
            esineet = ",".join(esine_nimet)
        else:
            esineet = ""
        # tallentaa tiedostoon huoneen nimi
        if pelaaja.sijainti is not None:
            sijainti = pelaaja.sijainti.nimi
        else:
            sijainti = ""
        # päivitetään pelaajan tallennetut tiedot
        uusi_rivi = (f"{pelaaja.nimi};{esineet};{sijainti};{pelaaja.piste.piste};{pelaaja.vinkki_maara}\n")
        rivit = []
        tieto_paivitetty = False
        try:
            with open (self.tiedot, "r") as tiedosto:
                rivit = tiedosto.readlines()
        except FileNotFoundError:
            pass
        
        with open(self.tiedot, "w") as tiedosto:
            for rivi in rivit:
                nimi = rivi.strip().split(";")[0]
                if nimi == pelaaja.nimi:
                    tiedosto.write(uusi_rivi)
                    tieto_paivitetty = True
                else:
                    tiedosto.write(rivi)
            if tieto_paivitetty == False:
                tiedosto.write(uusi_rivi)
                
    def ladaa_tiedot(self):
        pelaajat = []
        try:
            with open(self.tiedot, "r") as tiedosto:
                for rivi in tiedosto:
                    tallennettu_nimi, tallennettu_esineet, tallennettu_sijainti, tallennettu_pistemaara, tallennettu_vinkkimaara = rivi.strip().split(";")
                    if tallennettu_esineet:
                        esine_lista = tallennettu_esineet.split(",")
                    else:
                        esine_lista = []
                        
                    pelaajat.append([tallennettu_nimi, esine_lista, tallennettu_sijainti, int(tallennettu_pistemaara), int(tallennettu_vinkkimaara)])
        except FileNotFoundError:
            pass
        return pelaajat
        

            
            