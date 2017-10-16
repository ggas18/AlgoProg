#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:08:39 2017

@author: arek

"""

"""=============================Paramètres du fichier=================="""
debug=False # pour debuguer le code notamment l'activation des fonctions prints

""" Exo 2 TD 2"""
"Matrice A utilisée pour les tests des fonctions"
from math import inf # pour l'infini

"""
================================================================================
================================================================================
================================================================================
================================================================================
"""
"""force brute"""
# debut de la fonction sousMax
def sousMax(L,k):
    """
    Cette fonction trouve le sous tableau connexe de somme maximale
    de taille k et calcule la somme correspondante.

    =====================Entrée================================
    L: une liste contenant le tableau dans lequel on veut extraire
    un sous-tableau connexe

    k: la taille des élements à prendre

    =====================Sortie==============================
    une liste contenant la somme et une liste contenant
    la liste des elements sur lesquels cette somme s'evalue
    """
    """
    Initialisation
    """
    n=len(L)
    Max=-inf
    Ind_Max=0
    """
    on prendre les sous-tableaux connexes de longueur k dont les débuts
    varient de 0 à n-k
    """
    for i in range(n-k+1):
        som_partielle=sum(L[i:i+k])
        """
        on calcule la somme partielle de ce sous-tableau, si la somme des
        élements est meilleure on garde son indice.
        """
        if(Max<som_partielle):
            Max=som_partielle
            Ind_Max=i
    """
    On retourne une liste contenant la somme maximale et une liste contenant
    les éléments sur laquelle nous avons fait cette somme.

    """
    return [Max,L[Ind_Max:Ind_Max+k]]
# fin de la fonction sousMax


# debut de la fonction ssTabConnexMaxBF
def ssTabConnexMaxBF(L):
    """
    Cette fonction permet pour une liste L donnee de réels de trouver
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
         s_k est une liste dont le premier element est la somme et le deuxième
         élément est la sous-liste correspondante.
        """
        s_k=sousMax(L,k)
        """
        on enregistre s_k sous forme de cle:valeur avec cle la somme et valeur
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
# fin de la fonction ssTabConnexMaxBF


"""
================================================================================
================================================================================
================================================================================
================================================================================
"""
"""diviser pour reigner"""


# debut de la fonction ssTabMil
def ssTabMil(A,deb,mil,fin):
    """

    Cette fonction retourne le sous tableau maximal chevauchant
    l'indice mil et contenu entre les indices deb et fin.
    =========================ENTREE===============================
    A: sous liste contenant tous les élements
    deb: debut des indices possibles
    mil: milieu sur lequel on se positionne
    fin: fin des indices possibles
    =========================SORTIE===============================
    bas: indice de debut de la sous-liste
    haut: indice de haut de la sous-liste
    somme: somme de du sous-tableau de debut bas et de fin haut.
    """

    """
    c'est la somme maximale par defaut pour la somme maximale pour le sous tableau
    bas, on l'ininitialise a -∞
    """
    s_bas=-inf
    """
    On cherche d'abord le sous tableau connexe de somme maximale et de plus
    grand indice mil
    """
    for i in range(mil,deb-1,-1):
        som_p=sum(A[i:mil])
        if(s_bas<som_p):
            s_bas=som_p
            bas=i
    """
    c'est la somme maximale par defaut pour la somme maximale pour le sous tableau
    haut, on l'ininitialise à -∞
    """
    s_haut=-inf
    for i in range(mil,fin+1,1):
        som_p=sum(A[mil:i])
        if(s_haut<som_p):
            s_haut=som_p
            haut=i
    """
    On calcule ensuite la somme du sous-tableau entre les indices bas et haut
    """
    somme=sum(A[bas:haut])
    """
    On retourne ensuite le tuple (bas, haut, sommee)
    """
    return bas,haut,somme
# fin de la fonction ssTabMil



#debut de la fonction recursive ssTabMax
def ssTabMax(A,bas,haut):

    """
    Cette foncion recursive prend un tableau, un indice bas et un indice haut
    et essaie de retrouver le sous-tableau connexe de somme maximale contenu
    entre ces deux indices.
    =====================================ENTREE=================================
    A: liste contenant tous les elements sur lesquels nous voulons avoir le sous-
    tableau connexe de somme maximale.
    bas: indice bas indiquant le début de la section dont nous voulons extraire
         le sous-tableau de somme maximale
    haut: indice haut indiquant le début de la section dont nous voulons extraire
         le sous-tableau de somme maximale
    ====================================SORTIE==================================
    bas: indice de debut de la sous-liste
    haut: indice de haut de la sous-liste
    somme: somme de du sous-tableau de debut bas et de fin haut.

    """

    mil=(haut+bas)//2
    """
    Pour debuguer le code au besoin, il suffit que la valeur de debug soit True
    """
    if debug:
        print(bas, mil, haut)
    """
    Condition d'arret de la recursion: On arrête quand le bas est exactement le
    milieu ou le haut vaut exactement le milieu.
    """
    if (bas==mil or haut==mil):
        return bas, haut, A[bas]
    # sinon on choisit la partie qui contient la sous-liste de taille maximale
    else:
        som_bas=ssTabMax(A,bas,mil)
        som_haut=ssTabMax(A,mil,haut)
        som_mil=ssTabMil(A,bas,mil,haut)
        # on teste si c'est le bas qui contient la somme maximale et si c'est le
        # cas on applique ssTabMax(A,bas,mil)
        if( som_bas[2]>som_haut[2] and som_bas[2]>som_mil[2]):
            return ssTabMax(A,bas,mil)
        # on teste si c'est le haut qui contient la somme maximale et si c'est le
        # cas on applique ssTabMax(A,mil,haut)
        elif ( som_haut[2]>som_bas[2] and som_haut[2]>som_mil[2]):
            return ssTabMax(A,mil,haut)
        # Si ce n'est ni le haut, ni le bas alors le sous-tableau de somme maxi-
        # male chevauche le milieu.
        else:
            return ssTabMil(A,bas,mil,haut)
# fin de la fonction ssTabMax



# debut de la fonction ssTabConnexMax
def ssTabConnexMax(A):
    """
    une fonction qui utilise la fonction recursive ssTabMax sans prendre les
    paramètres utiles pour la recursion.
    """
    return ssTabMax(A,0,len(A))

# fin de la fonction ssTabConnexMax


"""
================================================================================
================================================================================
================================================================================
================================================================================
"""

# debut de la fonction ssTabLinear
def ssTabLinear(A):
    """
    cette fonction prend une liste A et retourne le sous-tableau de somme maxi-
    male.
    =================================ENTREE=====================================
    A: liste contenant tous les élements sur lesquels nous voulons trouver le
       sous-tableau connexe de somme maximale
    =================================SORTIE=====================================
    deb: le debut du sous-tableau connexe de somme maximale
    fin: la fin du sous-tableau connexe de somme maximale
    somMax: somme du sous-tableau de somme maximale
    """
    n=len(A)

    """
    Initialisations
    """
    somMax=A[0]
    som=0
    deb=0
    fin=0


    """
    On procède comme dans ssTabMil en faisant varier le milieu( mais le milieu
    est le début meme du sous-tableau connexe ici) quand nous avons une somme
    négative et en ne cherchant le sous-tableau maximale dans la partie
    supérieure et en mettant la somme à 0 au cas ou elle est negative car 0 est
    supérieur aux nombres négatifs et on recommence à chercher le sous-tableau
    connexe à partir de l'indice suivant.
    """
    debSsTab=0
    for i in range(n):
        som+=A[i]
        """
        Si la somme est meilleure on la garde
        on garde toujours le même début
        on avance le début
        """
        if(som>somMax):
                somMax=som
                deb=debSsTab
                fin=i
        """
        si la somme est négative alors, la somme est meilleure en ôtant ce
        sous-tableau
        On commence à chercher un sous-tableau de somme maximale commençant par
        l'indice suivant.
        """
        if(som<0):
            som=0
            debSsTab=i+1

    return deb,fin,somMax

# fin de la fonction ssTabLinear


"""
La commande qui suit permet d'isoler du code qui ne sera actif que si on compile
 ce fichier en tant que "main", mais pas si on l'importe.
Cela permet d'avoir une vue de son utilisation sans gêner l'execution d'un code
qui aurait besoin d'importer ce fichier pour trier une liste par exemple.
"""
if __name__=="__main__":
    A=[13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    # test de force brute: o(n²)
    ssTab=ssTabConnexMaxBF(A)
    print("Force brute: ",ssTab,"de somme :",sum(ssTab))

    # test de diviser pour reigner: o(n*log(n))
    res=ssTabConnexMax(A)
    print("Diviser pour reigner",A[res[0]:res[1]],"de somme:",res[2])

    # test de l'algo le plus efficace: o(n)
    res=ssTabLinear(A)
    print("Algo en temps linéaire",A[res[0]:res[1]],"de somme:",res[2])
