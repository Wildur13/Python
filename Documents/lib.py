import logging
import json
import os

from constants import DATA_DIR

LOGGER = logging.getLogger

class Liste(list):
    def __init__(self, name):
        self.name = name
        
    def ajouter(self, elem):
        if not isinstance(elem, str):
            raise ValueError("Vous ne pouvez ajouter que des chaines de caractères!")
        if elem in self:
            LOGGER.error(f"{elem} est déjà dans la liste")
            return False

        self.append(elem)
        return True


    def enlever(self, elem):
        if(elem in self):
            self.remove(elem)
            return True
        return False

    def afficher(self):
        print(f"Ma liste de {self.name} contient les éléments: ")
        i = 0
        while(i<len(self)):
            print(f" {i+1} - {self[i]} ")
            i += 1

    def save(self):
        chemin = os.path.join(DATA_DIR, f"{self.name}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        with open(chemin, "w") as f:
            json.dump(sorted(self), f, indent=4)

        return True
if __name__ == "__main__" :
     liste = Liste("courses")
     liste.ajouter("Pommes")
     liste.ajouter("Poires")
     liste.ajouter("Bananes")
     liste.save()