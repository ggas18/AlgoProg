#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 09:03:10 2017

@author: arek
"""

# programmation orientee objet

#les outils natifs de python à importer.
import sys # pour la reception des arguments en ligne de commandes.

import matplotlib.pyplot as plt# pour les figures

from math import sqrt, inf# pour la distance, l'infini

from divRegnerCours import triFusion# pour le tri
# fin imports


#debut exemple
class New_Class(object):
    att_0="Attribut propre à chaque objet de cette classe"# facultatif
    def __init__(self,att_1,att_2):
        # initialisation des attibuts de l'objet
        self.att_1=att_1
        self.att_2=att_2

    def new_Method(self,arg):
        #une methode de la classe
        print(arg)
#fin exemple

#debut class Person
class Person(object):
    nom=""
    prenom=""
    amis=[]
    def __init__(self,nom,prenom):
        self.nom=nom
        self.prenom=prenom
        self.amis=[]

    def presentation(self):
        print("Nom: ",self.nom,"\nPrenom",self.prenom)
    def ajoutAmi(self,other):
        self.amis.append(other)

    def affAmi(self):
        n=len(self.amis)
        for i in range(n):
            self.amis[i].presentation()

#fin Person
# debut de la classe Point
class Point(object):

     def __init__(self,x,y):
         self.x=x
         self.y=y

     def __repr__(self):
         return "Point: abscisse:{},ordonné:{}".format(self.x,self.y)

     def __str__(self):
         return "({},{})".format(self.x,self.y)

     def affichePoint(self,type=' bo'):
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


# debut closestPairBF
def closestBruteForce(L):
    n=len(L)
    I=0
    J=0
    d_min=inf
    for i in range(n):
        for j in range(n):
            d=L[i].dist(L[j])
            if(d_min>d and d!=0):
                d=d_min
                I=i
                J=j
    return L[I],L[J]

# fin closestPairBF

if __name__=="__main__":
    opt=""
    if len(sys.argv)==2:
        script,opt=sys.argv
    if(opt=="exemple"):
        objtest=New_Class("Bonjour","Hello")
        print(objtest.att_0)
        print(objtest.att_1)
        print(objtest.att_2)
        objtest.new_Method("Au revoir")
    elif(opt=="pMain"):
        pers1=Person("Ggas18","Arouna")
        pers2=Person("GANOU","Arouna")
        print()
        print("Presentation de la personne 1")
        pers1.presentation()
        print()
        print("Presentation de la personne 2",)
        pers2.presentation()

        print("test ajout ami")
        pers2.ajoutAmi(pers1)

    elif(opt=="point"):
        p1=Point(4.0,7.0)
        p2=Point(8.0,-7.0)
        p3=Point(-4.0,5.0)
        p4=Point(2.0,3.0)
        p5=Point(-5.0,1.0)
        L=[p1,p2,p3,p4,p5]
        print("test de __str__")
        print(p1)
        p1.affichePoint()
        print("test de distance");
        print("distance à l'origine de p1",p1.dist(Point(0,0)))
        print("distance de p1 à p1",p1.dist(p1))
        print("le plus proche point",p1.nearest(L))
        print("Closest pair Brute force")
        s=closestBruteForce(L)
        n=len(L)
        for i in range(n):
            L[i].affichePoint()

        s[0].afficheSeg(s[1])

        plt.show()