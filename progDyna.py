#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:22:25 2017

@author: arek
"""

"""=============================Paramètres du fichier=================="""
debug=True # pour debuguer le code notamment l'activation des fonctions prints


def affTab(L):
    n=len(L)
    for i in range(n):
        print(L[i])
    print()

from math import inf
def creerTableau(ligne,colonne, sym=inf):
    Li=[]
    for i in range(ligne):
        Li.append([sym]*colonne)

    return Li


"""======================fin données pour les test==================="""
def nbPieceMin(S,a):
    n=len(a)
    #Z=[[inf]*n]*S;
    Z=creerTableau(n,S+1)

    for t in range(S+1):
        Z[0][t]=inf

    for i in range(n):
        Z[i][0]=0
    sol=creerTableau(n,S+1,"")
    for t in range(S+1):
        for i in range(n):
            if debug:
                affTab(Z)
            if(t-a[i]>=0):
                if (Z[i-1][t]>1+Z[i][t-a[i]]):
                    Z[i][t]=1+Z[i][t-a[i]]
                    sol[i][t]='g'

            else:
                Z[i][t]=Z[i-1][t]
                sol[i][t]='h'

            #Z[i][t]=min(Z[i-1][t],    1+Z[i][t-a[i]])
    s=[]
    i=n-1
    t=S
    while(i>=0 and t>=0):
            if (sol[i][t]=='g'):
               t=t-a[i]
               s.append(a[i])

            else:
               i=i-1

    return Z[n-1][S],sol,s

"""===================== pour les tests ============================"""

if __name__=="__main__":
    #a=[1, 2, 5, 10]
    a=[2, 4]
    S=7
    nb=nbPieceMin(S,a)
    affTab(nb[1])
    print(nb[2])
