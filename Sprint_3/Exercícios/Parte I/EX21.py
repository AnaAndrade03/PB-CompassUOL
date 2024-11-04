class Passaro:
    def __init__(self):
        pass

    def voar(self):
        print('Voando...')

    def emitir_som(self):
        print('Emitindo som')
      
class Pato(Passaro):
    def __init__(self):
        super().__init__()

    def emitir_som(self):
        print("Pato emitindo som...")
        print("Quack Quack")

class Pardal(Passaro):
    def __init__(self):
        super().__init__()

    def emitir_som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")

pato = Pato()
print("Pato")
pato.voar()
pato.emitir_som()

print()  

pardal = Pardal()
print("Pardal")
pardal.voar()
pardal.emitir_som()
