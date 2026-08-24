
leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

grammat = ((leiviskät*20 + naulat)*32 + luodit)*13.3
kg = grammat // 1000
vain_grammat = grammat % 1000

print(f"Massa nykymittojen mukaan: {kg:.0f} kg ja {vain_grammat:.2f} g")