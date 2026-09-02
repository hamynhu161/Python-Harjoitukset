# Kysyy käyttäjältä lukuja ja tallentaa ne listaan.
# Ohjelma lopetetaan kun käyttäjä syöttää tyhjän merkkijonon. 
# Tulostaa viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. 

list = []

while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    else:
        list.append(float(luku))
    
list.sort(reverse=True)

for i in range(0,5):
    print(list[i])