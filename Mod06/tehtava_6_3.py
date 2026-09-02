# Kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. 
# Jos löytyy yksi numero (paitsi 1 ja luku), jolla luku on jaollinen, jotta se ei ole alkuluku

luku = int(input("Anna kokonaisluku: "))

on_alkuluku = True

if luku < 2:
    print(f"{luku} ei ole alkuluku.")
else:
    for i in range(2, luku):
        if luku % i == 0:
            on_alkuluku = False
            break

if on_alkuluku:
    print(f"{luku} on alkuluku.")
else:
    print(f"{luku} ei ole alkuluku.")
    
