# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
# Summa lasketaan for-rankenteen avulla ja palautetaan return-lauseella. 
# Kutsutetaan funktiota ja tulostetaan sen palauttaman summan.

def laske_summa(lista):
    luku_summa = 0
    for luku in lista:
        luku_summa = luku_summa + luku
    return luku_summa

lista_luku = [1,4,6,8]
summa = laske_summa(lista_luku)

print(f"Lukujen summa on {summa}")


