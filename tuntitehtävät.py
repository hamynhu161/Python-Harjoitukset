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

while True:
    menu_list = "Select option: \n1. plus \n2. miinus \n3. kertolasku \n0. lopetus"

    select = input(menu_list)
    
    if select == "0":
        break
    
    numero_1 = float(input("Anna numero: "))
    numero_2 = float(input("Anna numero: "))
    
    if select == "1":
        print(f"Laskutoimituksen tulos on: {numero_1 + numero_2}")
    elif select == "2":
        print(f"Laskutoimituksen tulos on: {numero_1 - numero_2}")
    elif select == "3":
        print(f"Laskutoimituksen tulos on: {numero_1 * numero_2}")
        
    