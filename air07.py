#Insertion dans un tableau trié

import sys

def insertion_tri(liste=sys.argv[1:]):
    liste.sort()
    for i in liste:
        print(i, end=" ")

insertion_tri()

