luku = input("Anna luku: ")
max_luku = int(luku)
min_luku = int(luku)

while luku != "":
    luku_int = int(luku)
    if luku_int > max_luku:
        max_luku = luku_int
    if luku_int < min_luku:
        min_luku = luku_int
   
    luku = input("Anna luku: ")
    
print(f"Saaduista luvuista suurin on {max_luku}")
print(f"Saaduista luvuista pienin on {min_luku}")