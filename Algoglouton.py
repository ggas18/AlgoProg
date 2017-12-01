#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:47:30 2017

@author: arek
"""

#les outils natifs de python à importer.
import sys # pour la reception des arguments en ligne de commandes.

import matplotlib.pyplot as plt# pour les figures

from math import sqrt, inf# pour la distance, l'infini

from random import random# la generation de nombre aleatoire entre 0 et 1
# fin imports

# debut exo1
# class evenement
class Evenement(object):
    # une classe qui represente un evenement.
    def __init__(self,deb,fin):
        self.debut=deb
        self.fin=fin

    def __str__(self):
        chaine1=self.debut*"   "+"|"+"---"*(self.fin-self.debut)+"|\n"
        chaine2=self.debut*"   "+"("+ str(self.debut)+","+str(self.fin)+")"
        chaine=chaine1+chaine2
        return chaine

    def __repr__(self):
         return "Evenement: debut:{},fin:{}".format(self.debut,self.fin)

    def __lt__(self,other):
        return self.fin<other.fin

# fin class evenement

# debut gymnase
def maxEvent(L):
    # ENTREE: une liste d'evenement
    # SORTIE: une liste contenant le maximum des evenements compatibles
    n=len(L)
    t=[L[0]]
    for i in range(1,n):
        # on verifie si la tache est compatible avec la derniere tache.
        if(L[i].debut>t[-1].fin):
            t.append(L[i])
    return t
# fin gymnase

# fin exo1

# debut exo2

# debut class arrete
class arrete(object):
    def __init__(self,som1,som2,poids):
        self.som2=som2;
        self.som1=som1;
        self.poids=poids
    def __str__(self):
        return "arete:(dep: {}, dest: {}, pds: {})".format(self.som1,
                      self.som2,self.poids)
    def __repr__(self):
        return "arete:(dep: {}, dest: {}, pds: {})".format(self.som1,
                      self.som2,self.poids)

    def __lt__(self,other):
        return self.poids<other.poids
# fin de class arrete

# debut DisjointSet
class DisjointSet(object):
    # structure de donnee rudimentaire de DisjointSet avec technique de compre-
    # ssion de l'arbre.
    def __init__(self, parent, rank):
        self.rank=rank
        self.parent=parent
# fin disjointSet

# debut de la fonction fin
def find(listDisjSet,som):
    # on recherche le representant de som dans l'ensemble listDisjSet
    # ENTREE: listDisjSet:  un objet de type union-find( DisjointSet)
    #         som: un nombre
    # SORTIE: le representant de l'ensemble dans lequel se trouve l'element som

    # on recherche du representant de som
    if(listDisjSet[som].parent!=som):
        listDisjSet[som].parent = find(listDisjSet, listDisjSet[som].parent)
    return listDisjSet[som].parent
# fin de la fonction find

# debut de la fonction union
def union(listDisjSet,som1, som2):
    # cette fonction ajoute les deux sommets d'une arrete dans l'objet du type
    # union-find
    # ENTREE: listDisjSet: une struture du type union-find
    #         som1: le prmeier sommet de l'arrete
    #         som2: le second sommet de l'arrete
    # SORTIE: rien

    # on recherche les representants des deux sommets dans l'objet listDisjSet
    som1Rac=find(listDisjSet,som1)
    som2Rac=find(listDisjSet,som2)
    # si l'un des representants a une hauteur plus petite, on ajoute à ce sous-
    # ensemble de sorte que les hauteurs s'equilibrent
    if(listDisjSet[som1Rac].rank<listDisjSet[som2Rac].rank):
        listDisjSet[som1Rac].parent=som2Rac
    elif(listDisjSet[som1Rac].rank>listDisjSet[som2Rac].rank):
        listDisjSet[som2Rac].parent=som1Rac

    else:
        listDisjSet[som2Rac].parent=som1Rac
        listDisjSet[som1Rac].rank+=1
# fin de la fonction union

# debut de la fonction
def yaCycle(listDisjSet,arete):
    # cette fonction cherche dans listDisj si les deux sommets on le même repre-
    # sentant. Si oui il ya un cycle, sinon on fait une fusion avec listDisjSet
    # des deux sommets.

    # ENTREE: listDisjSet: la struture du type union-find
    #         arete: une arrete avec les deux sommets et le poids
    # SORTIE: booleen vrai s'il ya cycle, et faux sinon.

    # on recherche les representants
     s1=find(listDisjSet,arete.som1)
     s2=find(listDisjSet,arete.som2)
    # on teste s'ils sont les mêmes representants.
     if(s1==s2):
         return True
     else:
         union(listDisjSet,arete.som1,arete.som2)
         return False
# fin de la fonction  yaCycle

# debut de fonction ACM
def ACM(A):
    n=len(A)
    LiArre=[]
    listDisjSet=[]
    for i in range(n):
        listDisjSet.append(DisjointSet(i,0))
        for j in range(n):
               LiArre.append(arrete(i,j,A[i][j]))

    LiArre.sort()
    arbCouvrant=[]
    nb_ar=len(LiArre)
    for i in range(nb_ar):
        if(not yaCycle(listDisjSet,LiArre[i])):
            arbCouvrant.append(LiArre[i])

    return arbCouvrant
# fin de fonction ACM

# fin exo2

# debut de l'exo3
class tache(object):
    def __init__(self,num,deadline,pena):
        self.n=num
        self.d=deadline
        self.w=pena

    def __str_(self):
        return "tache:num {}, deadline{} pena {}".format()

    def __lt__(self,other):
        return self.w<other.w

def OT(listTache):
    n=len(listTache)
    print(n,"à faire")
# fin de l'exo3

# debut exo4

#debut de la fonction creerTableau
def creerTableau(ligne,colonne, sym=inf):
    # cette fonction un nombre de lignes colonnes et un symbole et
    # creer un tableau qui est basiquement une liste de liste. Cette
    # liste de listes est alors initialisé à sym. sym est par défaut
    # à inf.

    # ENTREE: ligne le nombre de ligne dans le tableau
    #         colone le nombre de colonne dans le tableau
    #         sym l'element qu'on va utilisé pour initialisé la liste.

    # SORTIE: Li le tableau que l'on veut creer qui est à la base une
    #           une liste de listes
    Li=[]
    # on commence avec une liste vide et on rempli à chaque fois avec
    # une liste de taille colonne dont tous les éléments sont "sym"
    for i in range(ligne):
        Li.append([sym]*colonne)

    return Li
#fin de la fonction creertableau

# debut de la classe Point
class Point(object):

     def __init__(self,x,y):
         self.x=x
         self.y=y

     def __repr__(self):
         return "Point: abscisse:{},ordonné:{}".format(self.x,self.y)

     def __str__(self):
         return "({},{})".format(self.x,self.y)

     def affichePoint(self,type='bo'):
         plt.plot(self.x,self.y,type)

     def dist(self,other):
         return sqrt((self.x-other.x)**2+(self.y-other.y)**2)

     def afficheSeg(self,other):
         plt.plot([self.x,other.x],[self.y,other.y])

     def nearest(self,liPoint):
         n=len(liPoint)
         d_Min=inf
         near=0;
         for i in range(n):
             d=self.dist(liPoint[i])
             if(d!=0 and d<d_Min):
                 near=i
                 d_Min=d
         return liPoint[near]

     def __lt__(self,other):
        return self.x<other.x

     def __gt__(self,other):
         return self.x>other.x

     def __eq__(self,other):
         return self.x==other.x
# fin Point

# debut de la fonction arbreGraphique
def arbreGraphique(N):
    # cette fonction prend en entree un entier N, genere des points aléatoires
    # sur la pavé (0 1)², cherche l'arbre couvrant de poids minimal et fait
    # enfin la figure de ces points sur le pavé.

    # ENTREE: N un entier qui represente le nombre de points aléatoires
    # SORTIE: rien

    # liste des sommets qui sont des points. Nous allons utiliser les in-
    # dices des points lorsque nous allons travailler avec des arrêtes. Par exem-
    # ple l'arrête joignant le point 0 et le point 1 sera reprenté par une arrête
    # ayant pour sommet 0 et 1. Lorsqu'on aura besoin de travailler avec le point
    # nous allons utiliser les indices.
    listSommet=[]

    # matrcice d'ajence A
    A=creerTableau(N,N,inf)
    # la matrice d'ajacence va utiliser les indices 0 à N-1 comme sommet
    for i in range(N):
        p=Point(random(),random())
        listSommet.append(p)
        for i in range(N):
             for j in range(N):
                 A[i][j]=listSommet[i].dist(listSommet[j])
    # liste des arrêtes de l'arbre couvrant de point minimal
    arbreCouvrantMin=ACM(A)
    tailleACM=len(arbreCouvrantMin)
    # on parcours la liste des arrêtes et les affiches, en utilisant l'equivalence
    # entre indice et point dans liste des points.
    for i in  range(tailleACM):
        listSommet[arbreCouvrantMin[i].som1].afficheSeg(listSommet[arbreCouvrantMin[i].som2])
    plt.show()
# fin de la fonction arbreGraphique

# fin exo4



# debut exo dijkstra

# debut fonction indexDistMin
def indexDistMin(listDist, listVisit):
    # cette fonction prend une liste de distante et retourne l'indice de la plus
    # petite distance et qui n'a pas encore ete visitee en utilisant la listVisit
    N=len(listDist)
    distMin=inf
    for i in range(N):
        if(listVisit[i]==False and listDist[i]<=distMin):
            distMin=listDist[i]
            index=i
    return index
# fin fonction indexDistMin

# debut fonction dijkstra
def dijkstra(A,source):
    # cette fonction prend une matrice d'adjacence et un sommet source et essaie
    # de trouver les chemins minimaux entre ce sommet les autres sommets.
    #ENTREE: A la matrice d'ajacance
    #        source le sommet source
    #SORTIE: listDist la liste des distances au sommet, les sommets etant les
    # indices
    N=len(A)
    listDist=[inf]*N# liste des distance// listDist[i] est la distance entre
    # le sommet source et le sommet i
    listVisit=[False]*N# liste des etats des sommets// listVisit[i] est True si
    #le sommet i est deja visite

    # on met la distance a la source a zero
    listDist[source]=0

    # recherche de la plus petite distance à chaque sommet
    for j in range(N):
        # on cherche le sommet de plus petite distance le plus proche
        index=indexDistMin(listDist,listVisit)
        # on le marque comme deja visitee
        listVisit[index]=True
        # on met a jour les distances pour les sommets adjacants non encore visites
        for k in range(N):
            # on met a jour si seulement la distance en passant par le sommet
            # de distance minimale est plus petite
            if(not listVisit[k] and listDist[index]+A[index][k]<=listDist[k]):
                listDist[k]=listDist[index]+A[index][k]

    return listDist

# fin fonction dijksta

# fin exo dijkstra

if __name__=="__main__":
    opt=""
    if len(sys.argv)==2:
        script,opt=sys.argv
    if(opt=="exo1"):
        # on cree une liste d'evenements
       L1=[Evenement(0,6), Evenement(1,4),Evenement(2,13),Evenement(3,5),Evenement(3,8)]
       L2=[Evenement(5,7), Evenement(5,9),Evenement(6,10),Evenement(8,11),Evenement(9,12)]
       L3=[Evenement(12,14)]
       L=L1+L2+L3
       # on les tries dans l'ordre croissant de leurs dates de fin
       L.sort()
       # on cherche l'ensemble maximal d'événements compatibles.
       t=maxEvent(L)
       print("Les taches compatibles")
       print()
       for i in range(len(t)):
           print(t[i])
    elif(opt=="exo2"):
        ar1=arrete(1,2,5)
        A=[[0,900,4,inf,inf],[900,0,1,42,inf],[4,1,0,10,12],[inf,42,10,0,3],[inf,inf,12,3,0]]
        arbCouvrant=ACM(A)
    elif(opt=="exo3"):
         print("exo 3 à faire")

    elif(opt=="exo4"):
         N=50
         listSommet=[]
         # matrcice d'ajence A
         A=creerTableau(N,N,inf)
         for i in range(N):
             p=Point(random(),random())
             listSommet.append(p)
         for i in range(N):
             for j in range(N):
                 A[i][j]=listSommet[i].dist(listSommet[j])
         # l'arbre couvrant de point minimal
         arbreCouvrantMin=ACM(A)
         tailleACM=len(arbreCouvrantMin)
         for i in  range(tailleACM):
             listSommet[arbreCouvrantMin[i].som1].afficheSeg(listSommet[arbreCouvrantMin[i].som2])
         plt.show()
    elif(opt=="dijkstra"):
         A=[[0,7,9,inf,inf,14],
            [7,0,10,15,inf,inf],
            [9,10,0,11,inf,2],
            [inf,15,11,0,6,inf],
            [inf,inf,inf,6,0,9],
            [14,inf,2,inf,9,0]]
         source=0
         listDist=dijkstra(A,source)
         print("Distance de ",source," à ")
         for i in range(len(A)):
             print(i," de distance ",listDist[i])
    else:
        print("Choisissez une option avec la commande:")

        print("        run ", sys.argv[0],
              "[options= exo1, exo2, exo4 ou dijkstra](CONSOLE IPYTHON)")

        print("        ou")
        print("        python3 ", sys.argv[0],
              "[options= exo1, exo2, exo4 ou dijkstra](TERMINAL UNIX)")

    # on saute des lignes pour differencier les sorties
    print()
    print()