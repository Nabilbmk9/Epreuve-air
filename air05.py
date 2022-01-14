#Sur chacun d’entre eux

import sys

#Gestion d'erreurs
for x in sys.argv[1:-1]:
    if not x.isnumeric():
        print("erreur.")
        sys.exit()

#Fonction
def sur_chacun(liste=sys.argv[1:-1], operation=sys.argv[-1]):

    liste = [int(i) for i in liste]
    operation = [j for j in operation]
    calculateur = ""

    #Recupere le chiffre final
    for y in operation[1:]:
        if not y.isnumeric():
            print("erreur.")
            sys.exit()
        calculateur += y

    #Erreur si lettre pour le dernier argument
    if not operation[1].isnumeric():
        print("erreur.")
        sys.exit()
    
    #Calcule
    for h in liste:
        if operation[0] == "-":
            print(h - int(calculateur), end=" ")
        
        elif operation[0] == "+":
            print(h + int(calculateur), end=" ")
        
        #Erreur si pas de + ou de -
        else :
            print("erreur.")
            sys.exit()

sur_chacun()