# Luo tyhjä joukko
# Kysyy käyttäjältä nimiä while-silmukassa
# Tarkistaa, että onko nimi joukossa ja tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi 
# Tulostaa syötetyt nimet yksi kerrallaan.

nimet = set()

while True:
    nimi = input("Anna nimesi: ")
    if nimi == "":
        break
    
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    
    nimet.add(nimi)

for nimi in nimet:
    print(nimi)