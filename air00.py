#Split

import sys

#Gestion d'erreur
if len(sys.argv) != 2:
    print("erreur.")
    sys.exit()


#Fonction
def spliter(chaine=sys.argv[1:]):
    tour = 0
    for i in chaine[tour]:
        if (i == " ") or (i == "\n") or (i == "\t"):
            print()

        else :
            print(i, end="")
        tour += 1

    
spliter()