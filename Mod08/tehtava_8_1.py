# Kysyy käyttäjältä kuukauden numeron
# Vuodenajat- monikkotietorakenne sisältää: kevät, kesä, syksy, talvi. 
# Tulosta kuukausia vastaavat vuodenajat

kuukausi_numero = int(input("Anna kuukauden numero: "))
vuodenajat = ("talvi", "kevät", "kesä", "syksy")

# if kuukausi_numero in (12, 1, 2):
#     print(f"Nyt on {vuodenajat[0]}")
# elif kuukausi_numero in range (3,6): 
#     print(f"Nyt on {vuodenajat[1]}")
# elif kuukausi_numero in range(6,9): 
#     print(f"Nyt on {vuodenajat[2]}")
# elif kuukausi_numero in range(9,12): 
#     print(f"Nyt on {vuodenajat[3]}")
# else:
#     print("Vihreellinen kuukauden numero.")

arvaa = kuukausi_numero // 3
if arvaa in range (1,2):
    print(f"Nyt on {vuodenajat[1]}")
elif arvaa in range(2,3): 
    print(f"Nyt on {vuodenajat[2]}")
elif arvaa in range(3,4):
    print(f"Nyt on {vuodenajat[3]}")
else: 
    print(f"Nyt on {vuodenajat[0]}")