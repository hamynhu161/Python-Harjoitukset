# Luo Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. 
# Uusi hissi on aina alimmassa kerroksessa. 
class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin
    
    # Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. 
    def siirry_kerrokseen(self, kerros_numero):
        if self.kerros < kerros_numero:
            self.kerros_ylös(kerros_numero)
        else:
            self.kerros_alas(kerros_numero)
                
    def kerros_ylös(self, kerros_numero):
        for i in range(self.kerros, kerros_numero+1):
            self.kerros += 1
            print (f"Hissi on kerroksessa {self.kerros}.")
    
    def kerros_alas(self, kerros_numero):
        for i in range(self.kerros, kerros_numero, -1):
            self.kerros -= 1
            print(f"Hissi on kerroksessa {self.kerros}.")

# Luo hissin ja käsket sen siirtymään kuuteen kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.       
hissi = Hissi(3, 7)
hissi.siirry_kerrokseen(6)
hissi.siirry_kerrokseen(3)

    
    