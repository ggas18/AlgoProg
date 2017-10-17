import math


def afficheTab(T):
    #fonction qui ligne par ligne une liste de liste T
    n=len(T) #nombre de lignes
    for i in range(n):
        print(T[i])
    print() #Cree un espace à la fin


def minPieces(P,S):
    #Entrees: Liste P des piece disponibles, Somme S a atteindre
    #Sortie: Nombre nMin de pieces necessaires, Liste Q des pièces utilisées
    
    #Initialisation
    n=len(P)
    P=[0]+P #Ajout au début d'une piece de valeur 0.
    z=[]
    for i in range(n+1):
        z.append([math.inf]*(S+1))#Creation d'un tableau initialisé a 'infini'.
    for i in range(n+1):
        z[i][0]=0 #Initialisation de la première colonne a 0.
    F=[] #Tableau des indiquant l'origine de la valeur (fleche)
    for i in range(n+1):
        F.append(['o']*(S+1)) #Initialisé a 'o'.

    #print("Tableau initial:")
    #afficheTab(z)
    
    #Construction du tableau
    for i in range(1,n+1):
        for j in range(1,S+1):
            #Distinction des cas si la pièce a ajouter est plus grande que la somme a atteindre
            zh=z[i-1][j] #valeur au dessus
            zg=z[i][j-P[i]]+1 #valeur a gauche
            if (j>=P[i] and zg<zh):
                z[i][j]=zg
                F[i][j]='g'
            else:
                z[i][j]=zh
                F[i][j]='h'
    nMin=z[n][S]

    #print("Tableau final:")
    #afficheTab(z)

    #print("Tableau des fleches:")
    #afficheTab(F)

    #Reconstruction de la solution
    (i,j)=(n,S) #On part des indices de fin
    Q=[] #Contiendra les pieces utilisees

    while(i!=0 and j!=0):
        if F[i][j]=='g':
            Q+=[P[i]]
            j-=P[i]
        else:
            i-=1

    return (nMin,Q)


def affRes(P,S):
    #Fonction qui affiche le resultat sous forme de phrase
    (nMin,Q)=minPieces(P,S)
    if nMin==math.inf: print("On ne peut pas atteindre {0} avec les pieces {1}.".format(S,P))
    else: print("Pour atteindre {0} avec les pieces {1}, on utilise les {2} pieces {3}.".format(S,P,nMin,Q))


P=[1,2,5,10,20]
S=67

affRes(P,S)


P=[6,4,1]
S=8

affRes(P,S)
