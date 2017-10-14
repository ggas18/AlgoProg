#Algos de tri
##########################################


#tri par insertion

def triInsertion(li):
    #Entrée: Liste li de nombres
    #Sortie: Permutation triée de li
    for j in range(len(li)):
        cle=li[j]#nombre à placer
        i=j-1
        while (i>=0 and li[i]>cle):
            #Tant que la clé est plus petite que l'élément de gauche on les permute.
            li[i+1]=li[i]
            i-=1
        li[i+1]=cle

#L'algorithme agit directement sur la liste en argument et la modifie, comme list n'est pas un objet immutable, il est donc inutile de renvoyer la liste triée en sortie



#Tri fusion

def fusion(gauche,droite):
    #Entrée: deux listes triées
    #Sortie: la liste triée composées des éléments des listes en entrée
    if gauche==[]: return droite
    elif droite==[]: return gauche
    elif gauche[0]<=droite[0]: #Compare les premiers éléments des listes et place le plus petit devant la fusion des listes restantes
        return [gauche[0]]+fusion(gauche[1:],droite)
    else :
        return [droite[0]]+fusion(gauche,droite[1:])

def triFusion(li):
    #Entrée: Liste li de nombres
    #Sortie: Permutation triée de li
    n=len(li)
    if n==1: return li #Initialisation
    else:
        #Si la liste est de taille>2, on trie recursivement chacune des moitiés puis on les fusionnne
        liG=triFusion(li[:n//2])
        liD=triFusion(li[n//2:])
        return fusion(liG,liD)



#La commande qui suit permet d'isoler du code qui ne sera actif que si on compile ce fichier en tant que "main", mais pas si on l'importe.
#Cela permet d'avoir une vue de son utilisation sans gêner l'execution d'un code qui aurait besoin d'importer ce fichier pour trier une liste par exemple.
if __name__=="__main__":
    
    liste=[5,4,3,2,1]
    triInsertion(liste)
    print(liste)

    liste2=[5,4,3,2,1,10,4,7,-1,0]
    print(triFusion(liste2))
