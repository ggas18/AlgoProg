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
"Matrice A utilisée pour les tests de l'élement connexe"
A=[13, -3, -25, 20, 3, 16, 23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
"""force brute"""
def sousListe(L,k):
    #
    #
    n=len(L)
    res=[]
    for i in range(n-k+1):
        res.append(L[i:i+k])
    return res

from math import inf # pour l'infini
def sousMax(L,k):
    """
    Cette fonction trouve le sous tableau connexe de somme maximale
    de taille k et calcule la somme correspondante.

    =====================Entrée================================
    L: une liste contenant le tableau dans lequel on veut extraire
    un élement connexe

    k: la taille des élements à prendre

    =====================Sortie==============================
    une liste contenant la somme et une liste contenant
    la liste des éléments sur lesquels nous avons trouvé cette somme
    """
    n=len(L)
    Max=-inf
    Ind_Max=0
    for i in range(n-k+1):
        som_partielle=sum(L[i:i+k])
        if(Max<som_partielle):
            Max=som_partielle
            Ind_Max=i
    return [Max,L[Ind_Max:Ind_Max+k]]

def sousTabConnexe(L):
    """

    """
    n=len(L)
    dic_list=dict()
    list_sum=[]
    for k in range(n):
        s_k=sousMax(L,k)
        dic_list[s_k[0]]=s_k[1]
        list_sum=list_sum+[s_k[0]]
    return dic_list[max(list_sum)]


"""diviser pour reigner"""
def ssTabMil(A,deb,mil,fin):
    somme=0
    bas=mil
    haut=mil

    M=-inf
    for i in range(mil,deb-1,-1):
        som_p=sum(A[i:mil])
        if(M<som_p):
            M=som_p
            bas=i

    M=-inf
    for i in range(mil,fin+1,1):
        som_p=sum(A[mil:i])
        if(M<som_p):
            M=som_p
            haut=i
    somme=sum(A[bas:haut+1])

    return bas,haut,somme

def ssTab(L):

    return max()




