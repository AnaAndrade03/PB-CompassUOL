Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som.
Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir.
Imprima no console exatamente assim:

Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu

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
