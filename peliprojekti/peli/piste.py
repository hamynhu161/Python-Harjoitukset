class Piste:
    def __init__(self):
        self.piste = 0
    
    def lisaa_piste(self, numero):
        self.piste += numero
        print(f"Sait jo + {numero} pistettä.")
        
    def vahenna_piste(self, numero):
        self.piste -= numero
        print(f"Menetit jo -{numero} pistettä.")
        
    def nollaa_piste(self):
        self.piste = 0