# Kysyy käyttäjältä arpakuutioiden lukumäärän. 
# Silmäluku saadaan heittämällä arpakuutiot random-moduulin avulla
# Tulostaa silmälukujen summan. 

import random

arpakuutio_lukumaara = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

for i in range(arpakuutio_lukumaara):
    silmaluku = random.randint(1,6)
    print(silmaluku)
    summa = summa + silmaluku
    
print(f"Silmälukujen summa on {summa}")