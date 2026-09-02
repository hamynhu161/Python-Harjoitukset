# Kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan ja tallentaa ne listarakenteeseen. 
# Tulostaa kaupunkien nimet yksi kerrallaan

list = []

for i in range (5):
    kaupunki_nimi = input("Anna kaupungin nimi: ")
    list.append(kaupunki_nimi)
    
for nimi in list:
    print(nimi)
    