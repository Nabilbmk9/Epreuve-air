import sys

#Gestion erreur
for x in sys.argv[1:]:
    if not x.isnumeric():
        print("erreur.")

 #Fonction       
def trirapide(L=sys.argv[1:]):
    """trirapide(L): tri rapide (quicksort) de la liste L"""
    def trirap(L, g, d):
        pivot = L[(g+d)//2]
        i = g
        j = d
        while True:
            while L[i]<pivot:
                i+=1
            while L[j]>pivot:
                j-=1
            if i>j:
                break
            if i<j:
                L[i], L[j] = L[j], L[i]
            i+=1
            j-=1
        if g<j:
            trirap(L,g,j)
        if i<d:
            trirap(L,i,d)
 
    g=0
    d=len(L)-1
    trirap(L,g,d)
    for i in L:
        print(i, end=" ")

trirapide()
