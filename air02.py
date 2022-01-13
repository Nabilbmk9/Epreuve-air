#Concat

import sys

#Gestion d'erreur
if len(sys.argv) < 2 :
    print("erreur.")
    sys.exit()

#Fonction
def concat(chaine=sys.argv[1:-1], joindre=sys.argv[-1]):
    for i in chaine:
        print(i, end=joindre)

concat()