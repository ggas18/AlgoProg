#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:08:39 2017

@author: arek

"""

"""=============================Paramètres du fichier=================="""
debug=False # pour debuguer le code notamment l'activation des fonctions prints
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
A=[13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
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
    Cette fonction permet pour une liste L donnée de réels de trouver
    le sous-tableau connexe de taille maximale.
    ======================ENTREE=======================
    L: une liste

    =====================SORTIE========================
    L_connexMaxi: le sous-tableau connexe de somme maximale

    """
    n=len(L)
    """
     on utilise un dictionnaire pour avoir un accès direct avec la somme
     calculée comme clé et la sous-liste correspondante comme valeur du
     associée
    """
    dic_list=dict()
    list_sum=[] # la liste des sommes
    """
    On recherche le sous-tableau de somme maximale de taille k et ceci pour
    toutes les tailles k de 1 à n
    """
    for k in range(1,n+1):
        """
         s_k est liste dont le premier element est la somme et le deuxième
         élément est la sous-liste correspondante.
        """
        s_k=sousMax(L,k)
        """
        en enregistre s_k sous forme de cle:valeur avec cle la somme et valeur
        la liste.
        """
        dic_list[s_k[0]]=s_k[1]
        """
        on ajoute la somme actuelle à liste des sommes"""
        list_sum=list_sum+[s_k[0]]
    """
    On cherche la somme maximale dans la liste de toute les sommes
    """
    somMax=max(list_sum)
    """
    On utilise ensuite le dictionnaire pour retrouver la liste correspondante à
    cette somme somMax
    """
    L_connexMaxi=dic_list[somMax]
    """
    On retourne cette sous-liste: c'est la sous-liste connexe de somme maximale
    """
    return L_connexMaxi


"""diviser pour reigner"""
def ssTabMil(A,deb,mil,fin):
    """
    Cette fonction retourne le sous tableau maximal chevauchant
    l'indice mil et contenu entre les indices deb et fin.
    =========================ENTREE===============================
    A: sous liste contenant tous les élements
    deb: debut des indices possibles
    mil: milieu sur lequel on se positionne
    fin: fin des indices possibles
    """

    """
    initialisation
    """
    somme=0
    S=-inf # c'est la somme maximale par defaut pour
    """
    On cherche d'abord le sous tableau connexe de somme maximale et de plus
    grand indice mil
    """
    for i in range(mil,deb-1,-1):
        som_p=sum(A[i:mil])
        if(S<som_p):
            S=som_p
            bas=i

    S=-inf
    for i in range(mil,fin+1,1):
        som_p=sum(A[mil:i])
        if(S<som_p):
            S=som_p
            haut=i
    somme=sum(A[bas:haut])

    return bas,haut,somme

def ssTabMax(A,bas,haut):
    """
    """
    mil=(haut+bas)//2
    if debug:
        print(bas, mil, haut)

    if bas==mil:
        return bas, haut, A[bas]
    else:

        som_bas=ssTabMax(A,bas,mil)
        som_haut=ssTabMax(A,mil,haut)
        som_mil=ssTabMil(A,bas,mil,haut)
        if( som_bas[2]>som_haut[2] and som_bas[2]>som_mil[2]):
            return ssTabMax(A,bas,mil)
        elif ( som_haut[2]>som_bas[2] and som_haut[2]>som_mil[2]):
            return ssTabMax(A,mil,haut)
        else:
            return ssTabMil(A,bas,mil,haut)

def ssTabConnexMax(A):
    return ssTabMax(A,0,len(A))




