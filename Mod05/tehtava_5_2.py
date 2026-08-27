tuuma_määrä = float(input("Anna tuumamäärä: "))
senttimetri = 2.54

while tuuma_määrä >= 0:
    print(f"{tuuma_määrä} tuumaa =  {tuuma_määrä * senttimetri:.2f} senttimetria")
    tuuma_määrä = float(input("Anna tuumamäärä: "))

print ("Ohjelma lopettaa!")