class Voiture:
    essence = 100
    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence} litres d'essence")
    def roule(self, kilomètre):
        self.kilomètre = kilomètre
        ratio = (self.kilomètre*5)/100
        self.essence -= ratio
        while (self.essence>10):
            a = print(f"La voiture contient {self.essence}l d'essence")
            return(a)
        while (self.essence<=10 and self.essence>=0):
            b = print(f"Vous n'avez bientot plus d'essence.\n La voiture contient {self.essence}l d'essence")
            return(b)
        while(self.essence <0):
            c = print("Vous n'avez plus d'essence, faites le plein !")
            return (c)
    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir")