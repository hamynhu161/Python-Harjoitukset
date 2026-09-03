# Luo sanakirjan
# While- silmukalla kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. 
# Jos käyttäjä valitsee: uusi, kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. 
# Jos käyttäjä valitsee: haku, kysyy ICAO-koodin ja tulostaa lentoaseman nimen sanakirjan tiedon avulla. 
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. 

lentoasema_tiedot = {"EFHK":"Helsinki-Vantaa lentoasema", "EFOU":"Oulu lentoasema", "EFTU":"Turku lentoasema", "EFVA":"Vaasa lentoasema"}

while True:
    tieto = input("Haluaako tämä syöttää uuden lentoaseman, hakea lentoaseman tiedot (Uusi/Haku/lopeta): ")
    
    if tieto == "Uusi":
        koodi = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna nimesi: ")
        lentoasema_tiedot[koodi] = nimi     
    elif tieto == "Haku":
        koodi = input("Anna lentoaseman ICAO-koodi: ")
        if koodi in lentoasema_tiedot:
            print(lentoasema_tiedot[koodi])
        else:
            print("Lentoasemaa ei löytynyt.")   
    elif tieto == "lopeta":
        print("Ohjelma päättyy.")
        break
    else:
        print("Vihreellinen syöte.")
