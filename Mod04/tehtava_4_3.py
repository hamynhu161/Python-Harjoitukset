sukupuoli = input("Anna biologinen sukupuolesi (Nainen/Mies): ")
hemoglobiiniarvon = int(input("Anna hemoglobiiniarvon (g/l): "))

if sukupuoli == "Nainen":
    if hemoglobiiniarvon < 117:
        print("hemoglobiiniarvo on alhainen.")
    elif 117 <= hemoglobiiniarvon <= 175:
        print("hemoglobiiniarvo on normaali.")
    else: 
        print("hemoglobiiniarvo on korkea.")
elif sukupuoli == "Mies":
    if hemoglobiiniarvon < 134:
        print("hemoglobiiniarvo on alhainen.")
    elif 134 <= hemoglobiiniarvon <= 195:
        print("hemoglobiiniarvo on normaali.")
    else:
        print("hemoglobiiniarvo on korkea.")
else:
    print("Virheellinen syöte")