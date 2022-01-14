#Afficher une pyramide

import sys


#Gestion d'erreurs
if len(sys.argv) < 3 :
    print("Erreur.")
    sys.exit()

for x in sys.argv[2:]:
    if not x.isnumeric():
        print("Erreur.")
        sys.exit()

#Fonction
def pyramide(caractere=sys.argv[1], etage=sys.argv[2:]):
    etage = [int(i) for i in etage]
    addition =0

    for i in range(1, etage[0]+1):

        print(" "*(etage[0]-addition), caractere*(i+addition))
        addition += 1      

pyramide()

