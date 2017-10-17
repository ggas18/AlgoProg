#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:22:25 2017

@author: arek
"""

"""===========Paramètres du fichier et les arguments d'entrée================"""

import sys

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
def nbPieceMin(S,a,debug=False):
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

            else:
               Z[i][t]=Z[i-1][t]
               sol[i][t]='h'

    s=[]
    i=n-1
    t=S
    while(i>=0 and t>=0):
            if (sol[i][t]=='g'):
               t=t-a[i]
               s.append(a[i])

            else:
               i=i-1

    return Z[n-1][S],s

"""================================TD========================================"""


#debut exercice1

def sacDos(p,v,Pmax,debug=False):
    p=[0]+p
    v=[0]+v
    n=len(p)
    Z=creerTableau(n,Pmax+1,0)
    sol=creerTableau(n,Pmax+1,0)
    if debug:
        print("Test du tableau avant les calculs")
        affTab(Z)
    for i in range(1,n):
        for j in range(1,Pmax+1):
            if((j-p[i])>=0):
                if((Z[i-1][j-p[i]]+v[i])>Z[i-1][j]):
                    Z[i][j]=(Z[i-1][j-p[i]]+v[i])
                    sol[i][j]='g'
                else:
                    Z[i][j]=Z[i-1][j]
                    sol[i][j]='h'
            else:
                Z[i][j]=Z[i-1][j]
                sol[i][j]='h'
    if debug:
        print("Test du tableau après les calculs")
        affTab(Z)

    v_ut=[]
    p_ut=[]
    i=n-1
    j=Pmax
    while(i>0 and j>0):
            if (sol[i][j]=='g'):
               j=j-p[i]
               i=i-1
               v_ut.append(v[i])
               p_ut.append(p[i])

            else:
               i=i-1

    return Z[n-1][Pmax],v_ut, p_ut

#fin exercice1

if __name__=="__main__":
    opt=""
    if len(sys.argv)==2:
        scipt,opt=sys.argv

    if(opt=="cours"):
        a=[1, 2, 5, 10]
        a=[2, 4]
        S=7
        nb=nbPieceMin(S,a)
        if(len(nb[1])==0):
            print("On ne peut pas rendre cette monnaie avec les pièces actuelles")
        else:
            print("nombre de pièces",nb[0],"avec les pièces",nb[1])

    elif(opt=="exo1"):
        v=[3,7,4,2]
        p=[4,7,5,2]
        Pmax=15
        solution=sacDos(p,v,Pmax)
        print("Valeur optimale:",solution[0],
              "avec les valeurs",solution[1],
              "de poids",solution[2])
    else:
        print("Choisissez une option avec la commande:")
        print("        run _nomDuFichierScript_ options(CONSOLE IPYTHON)")
        print("        ou")
        print("        python3 _nomDuFichierScript_ options (TERMINAL UNIX)")
        print("        options peut être: cours, exo1,exo2,...")
