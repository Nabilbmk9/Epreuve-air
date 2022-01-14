#Contrôle de pass sanitaire
import sys


#Fonction
def controle_pass(liste=sys.argv[1:-1], separateur=sys.argv[-1]):

    elem_a_sup = []
    for i in range(0, len(liste)):
        if separateur.upper() in liste[i]:
            continue

        elif separateur.lower() in liste[i]:
            continue

        else:
            elem_a_sup.append(liste[i])
    
    for j in elem_a_sup:
        print(j, end=" ")
        

controle_pass()