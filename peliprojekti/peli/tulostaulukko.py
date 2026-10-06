# tallenna tiedot
def tallenna_tulos(tulokset):
    with open ("tallennetut_tulos.txt", "w") as tiedosto:
        for tulos in tulokset:
            nimi = tulos[0]
            sijainti = tulos[1]
            piste = tulos[2]          
            tiedosto.write(f"{nimi},{sijainti},{piste}\n")

# lataa aiemmin tallennetut tiedot
def ladaa_tulos():
    tulokset = []
    # avataan olemassa oleva tiedosto, jos se ei ole, peli jatkaa eteenpäin
    try:
        with open("tallennetut_tulos.txt", "r") as tiedosto:
            for rivi in tiedosto:
                nimi, teema, piste = rivi.strip().split(",")
                tulokset.append([nimi, teema, int(piste)])
    except FileNotFoundError:
        pass
    
    return tulokset

# määritellään pistemäärä, jonka perusteella pelaajat järjestetään
def piste_lista(pelaajat):
    return pelaajat[2]

# pelaaja voi nähdä muiden pelaajien pistettä           
def tulostaulukko(tulokset):
    tulokset.sort(key=piste_lista, reverse = True)
    
    print("TULOSTAULUKKO\n")
    print(f"{"Pelaaja":<15} {"Teema":<20} {"Piste":<7}")
    
    for tulos in tulokset[:5]:
        nimi = tulos[0]
        sijainti = tulos[1]
        piste = tulos[2]
        print(f"{nimi:<15} {sijainti:<20} {piste:<7}")
    
    tallenna_tulos(tulokset)