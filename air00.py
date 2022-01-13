#Split

from ast import literal_eval
import sys

#Gestion d'erreur
if len(sys.argv) != 2:
    print("erreur.")
    sys.exit()


#Fonction
def spliter(chaine=sys.argv[1:]):
    liste_separer = []
    string = ""
    for i in chaine[0]:
        if (i == " ") or (i == "\t") or (i == "\n"):
            liste_separer.append(string)
            string = ""

        else:
            string += i
    liste_separer.append(string)

    for j in liste_separer:
        print(j)

    
spliter()