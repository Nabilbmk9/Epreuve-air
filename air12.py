Liste = [7, 4, 2, 5, 1, 3, 8]

def tri_rapide(L):
    pivot = L[(len(L)-1)//2]

    for i in range(0, L[((len(L)-1)//2)]-1):       
        for j in range(L[(len(L)-1)//2]-1, len(L)):
            print(f"i : {i}")
            print(f"j : {j}")
        
            if L[i] > pivot:
                if L[j] < pivot:
                    L[i], L[j] = L[j], L[i]
            
            if L[i] > pivot:
                if L[j] < pivot:
                    L[j], L[(len(L)-1)//2] = L[(len(L)-1)//2], L[j] 
            
            
            
    print(L)
    

tri_rapide(Liste)

