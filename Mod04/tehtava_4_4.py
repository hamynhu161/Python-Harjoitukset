vuosiluku = int(input("Anna vuosiluku: "))

if vuosiluku % 4 == 0:
    if vuosiluku % 100 == 0 and vuosiluku % 400 == 0:
        print(f"{vuosiluku} on karkausvuosi")
    else:
        print("Ei ole karkausvuosi.")


