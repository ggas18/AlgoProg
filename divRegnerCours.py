#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:08:39 2017

@author: arek
"""
""" Tri insertion"""
def triInsertion(L):
    #entrée: liste L à trier
    #sortie: Liste Res triée

    n=len(L)

    for j in range(1,n):
        cle=L[j]
        i=j-1
        while i>=0 and L[i]>cle:
            L[i+1]=L[i]
            i=i-1
        L[i+1]=cle
    return L

""" Tri fusion"""
def fusion(G,D):
    #entrees: deux listes triées à fusionner
    #sorties: une liste fusionnées des deux listes entrées
    if(len(G)==0): return D
    if(len(D)==0): return G
    else:
        if(G[0]<D[0]):
            return [G[0]]+fusion(G[1:],D)
        else: return [D[0]]+fusion(G,D[1:])

def triFusion(L):
    # entrée: une liste triée L
    # sortie: la liste triée ayant les données de l'entrée L
    if(len(L)==1): return L
    else: return fusion(triFusion(L[:len(L)//2]),triFusion(L[len(L)//2:]))

""" Exo 2 TD 2"""

"""force brute"""
def sousListe(L,k):
    #
    #
    n=len(L)
    res=[]
    for i in range(n-k+1):
        res.append(L[i:i+k])
    return res


"""diviser pour reigner"""

def ssTabMil(A,deb,mil,fin):
    #
    #
    somme=0
    bas=mil
    haut=mil
    M=0
    for i in range(mil,deb,-1):
        som_p=sum(A[i:mil])
        if(M<som_p):
            M=som_p
            bas=i
    som_p=0
    M=0
    for i in range(mil,fin,1):
        som_p=sum(A[mil:i])
        if(M<som_p):
            M=som_p
            haut=i
    return bas,haut,somme