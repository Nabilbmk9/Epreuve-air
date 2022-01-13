#Chercher l’intrus

import sys

#Gestion d'erreur
if len(sys.argv) < 2 :
    print("erreur.")
    sys.exit()

    
def intru(argument=sys.argv[1:]):
    for i in range(0, len(argument)):
        compare = argument.pop(0)
        
        if not compare in argument:
            print(compare)

        argument.append(compare)

       

intru()     