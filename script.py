class Voiture:
    compte = 0
    def __init__(self,marque):
        Voiture.compte += 1
        self.marque = marque

voiture_01 = Voiture("Peugeot")
voiture_02 = Voiture("Lamborghini")

print(Voiture.compte)