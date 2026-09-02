# Kirjoita funktio parametrin kanssa ja palauttaa paluuarvonaan vastaavan litramäärän return-lauseella. 
# Kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi gallonat_litraksi-funktion avulla. 
# Jos käyttäjä syöttää negatiivisen gallonamäärän, break lopettaa silmukan

def gallonat_litraksi (määrä):
    määrä_litra = määrä*3.785
    return määrä_litra

while True:
    gallon_maara = float(input("Anna gallonamäärä: "))
    
    if gallon_maara < 0:
        break
        
    litra = gallonat_litraksi(gallon_maara)
    
    print(f"{gallon_maara} gallonaa on {litra:.2f} litraa.")

