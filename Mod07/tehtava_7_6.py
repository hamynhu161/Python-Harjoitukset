# Kirjoitetaan funktio laskea_yksikkohinta, jonka parametrit ovat pyöreän pizzan halkaisija ja pizzan hinta. 
# Käytetään math- kirjastoa pyöreän pizzan pinta-alan laskemiseen. 
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri return-lauseella
# Kysytään käyttäjältä kahden pizzan halkaisijat ja hinnat input-funktion avulla 
# Verrataan molempien pizzojen hintoja if-rakenteen avulla 

import math

def laskea_yksikkohinta(halkaisija, hinta):
    halkaisija_m = halkaisija / 100
    sade = halkaisija_m / 2
    pinta_ala = math.pi * sade ** 2
    yksikkohinta = hinta/pinta_ala
    return yksikkohinta

pizza_1_halkaisija = float(input("Anna ensimmäisen pizzan halkaisija: "))
pizza_1_hinta = float(input("Anna ensimmäisen pizzan hinta: "))
pizza_2_halkaisija= float(input("Anna toisen pizzan halkaisija: "))
pizza_2_hinta = float(input("Anna toisen pizzan hinta: "))

pizza_1 = laskea_yksikkohinta(pizza_1_halkaisija,pizza_1_hinta)
pizza_2 = laskea_yksikkohinta(pizza_2_halkaisija, pizza_2_hinta)

print(f"Ensimmäisen pizzan yksikköhinta on {pizza_1:.2f}")
print(f"Toisen pizzan yksikköhinta on {pizza_2:.2f}")

if pizza_1 < pizza_2:
    print("Ensimmäisella pizzalla on alhaisempi yksikköhinta")
elif pizza_1 > pizza_2:
    print("Toisella pizzalla on alhaisempi yksikköhinta")
else:
    print("Molemmilla pizzoilla on sama yksikköhinta.")
    
