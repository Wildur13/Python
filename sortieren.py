chemin = "C:/Users/Willy Durand Wakam/Desktop/Uni/Python/Python/python.txt"

with open(chemin, "r") as f:
    lines = f.read().splitlines()

name = []
for l in lines :
    name.extend(l.split())

surname = [s.strip(",.; ") for s in name]

with open(chemin, "w") as w:
    w.write("\n".join(sorted(surname)))
