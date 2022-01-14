#Afficher le contenu
import sys

from pathlib import Path


#Chemin de fichier
dossier_utilisateur = Path.cwd()
fichier_a_lire = dossier_utilisateur / sys.argv[1]

#Erreur si le fichier n'existe pas
if fichier_a_lire.exists():
    print(fichier_a_lire.read_text())

#Afficher si le fichier existe
else: 
    print("erreur.")