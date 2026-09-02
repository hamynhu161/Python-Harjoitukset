# Kirjoitetaan funktio, joka saa parametrinaan listan kokonaislukuja. 
# Käytetään if-rakennetta parillisten lukujen löytämiseen ja lisätään ne toiseen listaan.
# Luotaan lista kokonaislukuja, kutsutaan funktiota ja tulostetaan alkuperäinen ja karsitun lista.

def karsi_parittomat(kokonais_luvut):
    karsittu_lista = []
    for luku in kokonais_luvut:
        if luku % 2 == 0:
            karsittu_lista.append(luku)
    return karsittu_lista

alkuperainen_lista = [2,6,7,1,8,9,44,55]
karsittu_lista = karsi_parittomat(alkuperainen_lista)

print("Alkuperäinen lista: ",alkuperainen_lista)
print("Karsitun lista on: ",karsittu_lista)

