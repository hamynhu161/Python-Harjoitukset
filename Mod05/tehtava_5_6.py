arvottava_piste_maara = int(input("Anna arvottavan pisteen määrä: "))

k = 0
n = 0 #ympyrän sisälle jäävien pisteiden kokonaismäärä

while k < arvottava_piste_maara:
    x = float(input("Anna arvottava piste x (-1,1): "))
    y = float(input("Anna arvottava piste y (-1,1): "))
    
    if (x ** 2 + y ** 2) < 1:
        n = n + 1
    
    k = k + 1

pii = 4 * n / arvottava_piste_maara
 
print(f"Piin likiarvo on: {pii}")
    


