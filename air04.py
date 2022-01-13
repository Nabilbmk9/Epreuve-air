#Un seul à la fois

import sys


#Gestion d'erreurs
if len(sys.argv) != 2:
    print("erreur.")
    sys.exit()

#Fonction
def un_seul_a_la_fois(argument=[sys.argv[1]]):
    argument_to_liste=[]
    liste_final=[]
    for i in argument[0]:
        argument_to_liste.append(i)
    
    for j in range(0, len(argument_to_liste)-1):
        if argument_to_liste[j] == argument_to_liste[j+1]:
            if j == len(argument_to_liste)-2:           
                    liste_final.append(argument_to_liste[j])
            continue

        else:
            liste_final.append(argument_to_liste[j])
            if j == len(argument_to_liste)-2:           
                    liste_final.append(argument_to_liste[j+1])
    
    for h in liste_final:
        print(h, end="")


un_seul_a_la_fois()

