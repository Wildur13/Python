import glob
import json

chemin = "C:/Users/Willy Durand Wakam/Desktop/Uni/Python/Python/dossier_exemple/administratif/**"
files = glob.glob(chemin, recursive=True)

compte = ""
sociale = ""

for fls in files:
    if fls.endswith(".json"):
        with open(fls, "r") as f:
            contenu = json.load(f)
            if "Credit Mutuel" in contenu:
                compte = contenu["Credit Mutuel"]["Numero de compte"]
    elif fls.endswith(".txt"):
        with open(fls, "r") as f:
            contenu = f.read()
            if "Numéro de sécurité sociale " in contenu:
                sociale = contenu.split(":")[-1]


print(compte)          
print(sociale)
