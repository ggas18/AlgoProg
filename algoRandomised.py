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

# debut de la classe arrete
class arrete(object):
    def __init__(self,p1,p2):
        self.dep=p1
        self.dest=p2
# fin de la classe arrete

# debut centre de gravite
def gravite(ListPoint):
    n=len(ListPoint)
    x_g=0
    y_g=0
    for i in range(n):
        x_g=x_g+ListPoint[i].x
        y_g=y_g+ListPoint[i].y
    return [x_g/n,y_g/n]
# fin centre de gravite
# debut convexHull
def convexHull(listP):
    # cette fonction prend une liste de points et trouve l'enveloppe convex
    # ENTREE: listP list de points
    # SORTIE: list d'arrêtes constituants l'enveloppe convexe

    n=len(listP)
    if( n<3): return listP
    U=[listP[0],listP[1],listP[2]]
    H=[arrete(U[0],U[1]),arrete(U[1],U[2]),arrete(U[2],U[0])]
    T={}
    for i in range(n):
        T[listP[i]]='O'
    # liste de boolean pour memoriser l'état des points
    # si le point a la position i est inclus dans l'enveloppe convexe alors
    # visit[i]=True
    visit=[False]*n
    while(len(U)<n):

# fin convexHull
if __name__=="__main__":
    opt=""
    if len(sys.argv)==2:
        script,opt=sys.argv
    if(opt=="exo1"):
             print("ok")

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
