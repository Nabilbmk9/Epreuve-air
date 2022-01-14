#Mélanger deux tableaux triés

import sys


#Fonction
def deux_tab_tri(liste=sys.argv[1:]):
    tableau1=[]
    tableau2=[]

    for i in liste:
        #Ajoute les éléments après le "fusion"
        if i.isalpha():
            for j in liste[liste.index(i)+1:]:
                tableau2.append(j)
            tableau1.extend(tableau2)
            tableau1.sort()

            #Affichage
            for k in tableau1:
                print(k, end=" ")
            return

        #Ajoute les éléments avant le "fusion"
        else:
            tableau1.append(i)

deux_tab_tri()