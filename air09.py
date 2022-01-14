#Rotation vers la gauche

import sys

#Fonction
def rotation_gauche(liste=sys.argv[1:]):
    elem = liste.pop(0)
    liste.append(elem)
    tour = 0

    for i in liste:
        tour+=1
        if tour == len(liste):
            print(i, end=".")
            return
        
        print(i, end=", ")


rotation_gauche()