# määritellään pistemäärä, jonka perusteella pelaajat järjestetään
def piste_lista(tulos):
    return int(tulos[2])

# pelaaja voi nähdä muiden pelaajien pistettä           
def tulostaulukko(tulokset):
    tulokset.sort(key=piste_lista, reverse = True)  
    print("TULOSTAULUKKO\n")
    print(f"{"Pelaaja":<15} {"Teema":<20} {"Piste":<7}")  
    for tulos in tulokset[:5]:
        print(f"{tulos[0]:<15} {tulos[1]:<20} {tulos[2]:<7}")
    