#Split en fonction

import sys


#Gestion d'erreur
if len(sys.argv) !=3 :
    print("Erreur.")
    sys.exit()

#Fonction
def split_en_fonction(chaine=sys.argv[1], separateur=sys.argv[2]):
    
    chaine=[chaine]
    separateur=[separateur]
    liste_separer = []
    string = ""
    avant =[]
    apres = []
    for i in chaine[0]:
        if (i == " ") or (i == "\t") or (i == "\n"):
            liste_separer.append(string)
            string = ""

        else:
            string += i
    liste_separer.append(string)
    
    
    if separateur[0] in liste_separer:
        for i in liste_separer:
            if liste_separer.index(i) < liste_separer.index(separateur[0]):
                avant.append(i)
            
            elif liste_separer.index(i)> liste_separer.index(separateur[0]):
                apres.append(i)
    
    else:
        print("erreur.")
        sys.exit()
        
    #Affichage
    for i in avant:
        print(i, end=" ")
    print()
    for j in apres:
        print(j, end=" ")



split_en_fonction()