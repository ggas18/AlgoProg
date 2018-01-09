import random

def quickSort(l):
    #Entree: Liste li de nombres
    #Sortie: Permutation triee de li
    if len(l)<2: return l
    else:
        # choix du pivot
        pivot=random.choice(l)
        return quickSort([i for i in l if i<pivot])+[i for i in l if i==pivot]+quickSort([i for i in l if i>pivot])

#if __name__=="__main__":
li=[5,4,3,2,1,10,7,-1,0,2,3,8,3,6,7,3]
print(li)
print(quickSort(li))
