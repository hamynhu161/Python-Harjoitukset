# # Tehtävä 3_1
# nimi = input("Anna nimesi: ")
# kuvaileva_sana = input("Anna adjektiivi: ")
# print("Hän on " + nimi + ". Hän on " + kuvaileva_sana + " ohjelmointikehittäjä. Hän tykkää karkkia ja kehittää koulutuspelia.")


# # Tehtävä 3_2
# päivä = input("Anna päivien lukumäärä: ")
# päivä_float = float(päivä)
# print(f"Annettu määrä päiviä sekunteina: {päivä_float*24*60*60}")

# # Tehtävä 3_3
# gramma_määrä = int(input("Anna grammamäärä: "))
# print(f"Määrä kiloina ja grammoina: {gramma_määrä//1000} kg {gramma_määrä%1000} g")

# Tehtävä 4_1

# vuosi = int(input("Anna vuosi: "))

# if vuosi % 4 == 0:
#     if vuosi == 2020 or vuosi == 1940:
#         print("Ei ollut olympiavuosi")
#     else:
#         print("Oli olympiavuosi.")
# else:
#     print("Ei ollut olympiavuosi.")
    

# Tehtävä 4_2
# pituus = float(input("Anna sinun pituus: "))

# if pituus >= 140:
#     ikä = int(input("Anna sinun ikä: "))
#     if ikä >= 8:
#         print("Saat mennä kaikkin laitteisiin.")
#     else:
#         print("Saat mennä kaikkin paitsi tulirekeen.")

# elif pituus >= 100:
#     print("Saat mennä lasten laitteisiin.")
    
#Tehtävä 4_3
# nimi = input("Anna sinun nimesi: ")
# adtektiivi = input("Anna joku adtektiivi: ")
# print(f"{nimi} on opiskelija Metropoliassa. Hän on {adtektiivi} tunneilla. Tykkääkö hän fysiikasta tai viestinnästä?")
# kurssi = input("")
# if kurssi == "fysiikasta":
#     print(f"{nimi} on kiinnostunut {kurssi} ja käyttää noin kolme tuntia päivässä siihen liittyviä asioiden lukemiseen.")
# else:
#     print(f"{nimi} ei ole vielä hyvä siinä. Hän ei erityisesti tykänyt {kurssi} mutta ymmärtää sen merkityksen. Siksi hän haluaa opiskella ja kehittää sitä enemmän ammattikorkeakoulun aikana.") 

#Tehtävä 5_1

# Valiko = "Valinta: \n1. plus \n2. miinus \n3. kertolasku \n4. lopetus"

# valinta = input("valitse yksi laskutoimintuksesta tai loputeksen: ")

# while valinta != "lopetus":
#     numero_1 = float(input("Anna numero: "))
#     numero_2 = float(input("Anna numero: "))
    
#     if valinta == "plus":
#         print(f"Laskutoimituksen tulos on: {numero_1 + numero_2}")
#     elif valinta == "miinus":
#         print(f"Laskutoimituksen tulos on: {numero_1 - numero_2}")
#     elif valinta == "kertolasku":
#         print(f"Laskutoimituksen tulos on: {numero_1 * numero_2}")

#     Valiko = "Valinta: \n1. plus. \n2. miinus \n3. kertolasku \n4. lopetus"
#     valinta = input("valitse yksi laskutoimintuksesta tai loputeksen: ")
      
# Using while True

# while True:
#     menu_list = "Select option: \n1. plus \n2. miinus \n3. kertolasku \n0. lopetus"

#     select = input(menu_list)
    
#     if select == "0":
#         break
    
#     numero_1 = float(input("Anna numero: "))
#     numero_2 = float(input("Anna numero: "))
    
#     if select == "1":
#         print(f"Laskutoimituksen tulos on: {numero_1 + numero_2}")
#     elif select == "2":
#         print(f"Laskutoimituksen tulos on: {numero_1 - numero_2}")
#     elif select == "3":
#         print(f"Laskutoimituksen tulos on: {numero_1 * numero_2}")
 
#Tehtävä 6: 
# Tee luoka Lentokone (nimi, bensatankki_maksami, bensatankki_nyky). Tee luokalle lentokonelle metodi tankkaa(), joka täyttää lentokoneen tankin ja tulostaa, paljonko benssa mahtui. 
# Tee lentokoneelle metodi tulosta_tiedot()
# Tee luoka Lentokenttä (nimi ja lista kentälla olevista koneista). Tee luokkalle metodi tulosta_koneet() joka tuolostaa lentokentällä olevien koneiden tiedot. Se käyttää kunkin lentokoneen tulosta_tiedot() - metodia
# class Lentokone:
#     def __init__(self, nimi, bensatankki_maksami, bensatankki_nyky):
#         self.nimi = nimi
#         self.bensa_maksami = bensatankki_maksami
#         self.bensa_nyky = bensatankki_nyky
    
#     def tankkaa(self):
#         tankki = self.bensa_maksami - self.bensa_nyky
#         print(f"Lentokone mahtuu {tankki} litraa bensa.")
        
#     def tulosta_tiedot(self):
#         print(f"Lentokone: {self.nimi}, bensatankin maksimi: {self.bensa_maksami}, bensatankin nykyinen lukema: {self.bensa_nyky}")
#         return
    
# class Lentokenttä():
#     def __init__(self, nimi):
#         self.nimi = nimi
#         self.koneet = []
    
#     def listakoneet(self, kone):
#         self.koneet.append(kone)
#         # return
        
#     def tulosta_koneet(self):
#         for kone in self.koneet:
#             kone.tulosta_tiedot()
            
# kone1 = Lentokone("Boeing737", 243400, 200000)
# kone2 = Lentokone("AirbusA350", 323500, 300000)   
# lentokenttä = Lentokenttä("Helsinki")         
# kone1.tankkaa()
# kone2.tankkaa()
# lentokenttä.listakoneet(kone1)
# lentokenttä.listakoneet(kone2)
# lentokenttä.tulosta_koneet()

#Tehtävä 7
# 1. Lue koodi läpi, suorita se, varmista että ymmärrät, miten se toimii nyt.
# 2. Luo luokat Hirvio ja Pelaajahahmo. Ne molemmat perivät luokan Hahmo.
# 3. Muokkaa koodia niin, että lisäät Pelaajahahmo-luokalle ominaisuuden tavaralista. 
# Kun pelaajahahmo-olio luodaan, se saa parametrinä listan tavaroita, jotka tallennetaan olion listaan.
# 4. Ylikirjoita Hahmo-luokan tulosta-metodi Pelaajahahmolle niin, että se tulostaa mukaan myös tavaralistan.
# 5. Muokkaa niin, että vain hirviöillä on repliikki, ei kaikilla Hahmo-olioilla.
# 6. Ylikirjoita Hirvio-luokan tulosta-metodi niin, että se tulostaa myös repliikin.
# 7. Jos ehdit: Luo peliin useampi hirviö, ja laita pelaajahahmo taistelemaan myös niiden kanssa. 
# Taistelu-metodia ei tarvita sekä hahmolle että hirviölle. 
# Siirrä se sille luokalle, jossa se on sinusta looginen. 
# Testaa, että peli toimii järkevästi.

# class Hahmo:
#     def __init__(self, nimi, repliikki):
#         self.nimi = nimi
#         self.repliikki = repliikki
#         self.hp = 100

#     def tulosta_tiedot(self):
#         print(f"Hahmon nimi: {self.nimi}")
#         print(f"Hahmon hp: {self.hp}")

#     def taistelu(self, vastustaja):
#         print("Tulee suuri taistelu.")
#         input()
#         if vastustaja.hp > self.hp:
#             print(f"{self.nimi} hävisi taistelun :<")
#             self.hp = 0
#         else:
#             print(f"{self.nimi} voitti taistelun!")
#             self.tulosta_tiedot()

# merihirvio = Hahmo("Merihirviö", "Lits läts, aion syödä sinut!")
# pelaajahahmo = Hahmo(input("Anna hahmon nimi: "), "Olen sankari ja voitan kaikki!")

# print("Peli alkaa.")
# pelaajahahmo.tulosta_tiedot()
# input()

# print(f"{pelaajahahmo.nimi} kohtaa ensimmäiseksi kauhean hirviön. Hirviö huutaa:")
# print(merihirvio.repliikki)
# merihirvio.tulosta_tiedot()

# input()
# pelaajahahmo.taistelu(merihirvio)
# input()
# print(f"Peli ohi.")

class Hahmo:
    def __init__(self, nimi):
        self.nimi = nimi
        self.hp = 100

    def tulosta_tiedot(self):
        print(f"Hahmon nimi: {self.nimi}")
        print(f"Hahmon hp: {self.hp}")
            
class Hirvio (Hahmo):
    def __init__(self, nimi, repliikki):
        super().__init__(nimi)
        self.repliikki = repliikki
        
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(self.repliikki)

class Pelaajahahmo(Hahmo):
    def __init__(self, nimi, tavarat):
        super().__init__(nimi)
        self.tavarat = tavarat
    
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Tavarat ovat: {self.tavarat}")
        
    def taistelu(self, vastustaja):
        print("Tulee suuri taistelu.")
        input()
        if vastustaja.hp > self.hp:
            print(f"{self.nimi} hävisi taistelun :<")
            self.hp = 0
        else:
            print(f"{self.nimi} voitti taistelun!")
            self.tulosta_tiedot()
        
class Peli:
    def __init__(self, pelaajahahmo, hirviöt):
        self.pelaajahahmo = pelaajahahmo
        self.hirviöt = hirviöt
    
    def alkaa(self):
        print("Pelo alkaa")
        self.pelaajahahmo.tulosta_tiedot()
        
        for hirviö in hirviöt:
            print(f"{self.pelaajahahmo.nimi} kohtaa hirviön. Hirviö huutaa:")
            hirviö.tulosta_tiedot()
            self.pelaajahahmo.taistelu(hirviö)
            
        print("Peli ohi!")
    
merihirvio = Hirvio("Merihirviö", "Lits läts, aion syödä sinut!")
vuorihirvio = Hirvio("Vuorihirviö", "Syödä sinut!")
hirviöt = [merihirvio, vuorihirvio]
pelaajahahmo = Pelaajahahmo(input("Anna hahmon nimi: "), ["ase", "miekka"])
peli = Peli(pelaajahahmo, hirviöt)
peli.alkaa()