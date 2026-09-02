# Kysytään käyttäjältä nopan tahkojen määrästä 
# Funktio palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä (1, noppa_tahkot) random- moduulin avulla
# Funktio saa parametrinaan nopan tahkojen määrän. 

import random

noppa_tahkot = int(input("Anna nopan tahkojen määrä: "))

def heitto_noppa(tahkot):
    silmäluku = random.randint(1,tahkot)
    return silmäluku

while True:
    luku = heitto_noppa(noppa_tahkot)
    print(f"Nopan silmäluku on : {luku}")
    
    if luku == noppa_tahkot:
        print("Sai nopan maksimisilmäluku.")
        break
