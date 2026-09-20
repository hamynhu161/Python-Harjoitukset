class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin
   
    def siirry_kerrokseen(self, kerros_numero):
        if self.kerros < kerros_numero:
            self.kerros_ylös(kerros_numero)
        else:
            self.kerros_alas(kerros_numero)
                
    def kerros_ylös(self, kerros_numero):
        for i in range(self.kerros, kerros_numero):
            self.kerros += 1
            print (f"Hissi on kerroksessa {self.kerros}.")
    
    def kerros_alas(self, kerros_numero):
        for i in range(self.kerros, kerros_numero, -1):
            self.kerros -= 1
            print(f"Hissi on kerroksessa {self.kerros}.")

# Talo luokka: talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.      
class Talo:
    def __init__(self, alinkerros, ylinkerros, hissi_maara):
        self.alin = alinkerros
        self.ylin = ylinkerros
        self.hissit = []

        for i in range(hissi_maara):
            hissi = Hissi(alinkerros, ylinkerros)
            self.hissit.append(hissi)
    
    # Luo metodi aja_hissia, joka siirtää valitun hissin kohdekerrokseen.
    def aja_hissia (self,hissi_numero, kohdekerros):
        hissi = self.hissit[hissi_numero-1]
        hissi.siirry_kerrokseen(kohdekerros)
        
            
hissi1 = Hissi(3, 7)
hissi1.siirry_kerrokseen(6)
hissi1.siirry_kerrokseen(0)

talo = Talo(2, 5, 3)
talo.aja_hissia(2, 4)

