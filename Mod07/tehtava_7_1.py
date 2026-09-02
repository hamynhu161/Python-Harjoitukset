# Funktio palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6 random- moduulin avulla
# Heittää noppaa niin kauan kunnes tulee kuutonen: käytetään While True ja kun luku on 6, break lopettaa silmukan.

import random

def heitto_noppa():
    silmäluku = random.randint(1,6)
    return silmäluku

while True:
    luku = heitto_noppa()
    print(f"Nopan silmäluku on : {luku}")
    
    if luku == 6:
        print("Ohjelma suljettu.")
        break

    