import random

random_luku = random.randint(1, 10)
arvaus_luku = input("Anna luku: ")

while arvaus_luku != "":
    luku_int = int(arvaus_luku)
    if random_luku == luku_int:
        print("Oikein")
        break
    elif luku_int < random_luku:
        print("Liian pieni arvaus")
    else:
        print("Liian suori arvaus")
    arvaus_luku = input("Anna luku: ")


    