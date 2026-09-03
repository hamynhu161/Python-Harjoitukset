nimi = input("Anna sinun nimesi: ")
ikä = int(input("Anna sinun ikäsi: "))

asetukset_valitettu = []
pelimaailma = ["Metsäseikkailu", "Meriseikkailu", "Aavikko"]
pisteet = [100,232,554,321,98,666]
pelaajat = ["Anna", "Teemu", "Hanna", "Aatu"]

def asetukset():
    ääni = input("Anna sopiva äänenvoimakkuus: ")
    kirkkaus = input("Ann sopiva kirkkaus: ")
    
    asetukset_valitettu.append(ääni)
    asetukset_valitettu.append(kirkkaus)
    print(asetukset_valitettu)
    

def tulostaulukko(pistee, pelaaja):
    pelaaja_maara = len(pelaaja)
    print(f"Pelilla on {pelaaja_maara} pelaaja.")
        
    pistee.sort(reverse = True)
    paras_piste = pistee[0]
    print(f"Paras piste on: {paras_piste}")
        
def aloitus(teemat):
    print(f"Valitse teema, joka kiinnostaa sinua eniten!")
    for teema in teemat:
        print (" + ", teema)

if ikä < 12:
    print(f"Olet alaikäinen. Peli suljetaan.")
else:
    print(f"Tervetuloa {nimi}!")
    
    while True:
        print("Päävalikko: \n1. Asetukset \n2. Aloitus \n3. Tulostaulukko")
        komento = input("Anna komento: ")
        if komento == "1":
            # print("Tästä asetuksesta voi säätää musiikin ja äänien voimakkuutta.")
            asetukset()
        elif komento == "2":
            # print("Aloitetaan peli ja nautitaan siitä.")
            aloitus(pelimaailma)
        elif komento == "3":
            # print("Tulostaulukosta näkyy oman sijoituksen ja parhaat pisteet.")
            tulostaulukko(pisteet, pelaajat)
        elif komento == "lopeta":
            break          
    