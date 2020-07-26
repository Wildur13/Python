import os
import glob
import shutil
from pprint import pprint

"""
mp3, wav : Musique
mp4, mov : Videos
jpg, jpeg, png : Images
pdf : Documents
"""

chemin = "C:/Users/Willy Durand Wakam/Desktop/Uni/Python/Python/tri_fichiers_sources/"
chemin_1 = "C:/Users/Willy Durand Wakam/Desktop/Uni/Python/Python/tri_fichiers_sources/**"
files =glob.glob(chemin_1, recursive=True) 

chemin_dossier_musique = os.path.join(chemin, "Musique")
os.makedirs(chemin_dossier_musique,exist_ok=True)

chemin_dossier_videos = os.path.join(chemin, "Videos")
os.makedirs(chemin_dossier_videos,exist_ok=True)

chemin_dossier_images = os.path.join(chemin, "Images")
os.makedirs(chemin_dossier_images,exist_ok=True)

chemin_dossier_doc = os.path.join(chemin, "Documents")
os.makedirs(chemin_dossier_doc,exist_ok=True)

for fls in files:
    if fls.endswith(".mp3") or fls.endswith(".wav"):
        shutil.move(fls, chemin_dossier_musique)
    elif fls.endswith(".mp4") or fls.endswith(".mov"):
        shutil.move(fls, chemin_dossier_videos)
    elif fls.endswith(".jpg") or fls.endswith(".jpeg") or fls.endswith(".png"):
        shutil.move(fls, chemin_dossier_images)
    elif fls.endswith(".pdf"):
        shutil.move(fls, chemin_dossier_doc)