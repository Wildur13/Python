a = input("Entrez la source du fichier à ouvrir: ")

try:
    lire = open (a, "r")
    print(lire.read())
except FileNotFoundError as g:
    print("Error: ", g)

except UnicodeDecodeError as n:
    print("Error: ", n)

else:
    lire.close()