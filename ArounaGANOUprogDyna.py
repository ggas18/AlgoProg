#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:22:25 2017

@author: arek
"""

"""===========Paramètres du fichier et les arguments d'entrée================"""

#les outils natifs de python à importer.
import sys # pour la reception des arguments en ligne de commandes.
from math import inf # pour l'infini
# fin imports

#quelques fonctions utiles pour les routines de debugages

#début de la fonction affTab
def affTab(L):
    #cette fonction prend une liste de listes et les affiches
    #une à une sur chaque ligne.

    # ENTREE: L la liste de listes à afficher.
    # SORTIE: cette fonction ne retourne rien.

    n=len(L)
    # on parcourt la liste et on affiche la liste qui se trouve
    # à la position où nous sommes
    for i in range(n):
        print(L[i])
    print()
#fin de la fonction affTab

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
"""=================================cours===================================="""

#debut de la fonction nbPieceMin
def nbPieceMin(S,a,debug=False):
    #cette fonction prend une somme S et retourne le nombre minimal
    #de pièces qu'il faut utiliser pour la monnaie de cette pièce.

    #ENTREE: S la somme à rendre
    #        a le vecteur contenant les valeurs des pièces disponibles
    #        debug un bolean pour que la fonction fasse des affichages
    #        des resultats intermédiaires.

    #SORTIE: un tuple contenant le nombre de pièces et la liste de ces
    #        pièces.
    a=[0]+a
    if(debug):
        print()
        print("changer le paramètre debug en False si vous ne voulez",
              "\npas voir tous les affichages")
        print()

    n=len(a)# n est la taille du vecteur contenant la liste des pièces
    #         disponibles.
    Z=creerTableau(n,S+1)# on cree le tableau permettant de memoriser
    #                      les resultats des sous-problèmes.

    # on remet la première colonne et la première ligne etant par défaut
    # à infini à cause de l'utilisation de la fonction creerTab

    for i in range(n):
        Z[i][0]=0
    # on cree un tableau pour memoriser les directions de descentes
    # aboutissant la solution optimale:
    #       h: si on vient du haut
    #       g: si on vient de la gauche

    sol=creerTableau(n,S+1,"")

    # on remplit le tableau en utilisant la rélation de recurrence
    # que nous avons établie.
    for t in range(1,S+1):
        for i in range(1,n):
            # on teste d'abord si la somme qu'on veut rendre est plus
            # grande que la pièce actuelle: c'est uniquement dans ce
            # qu'on s'interresse au min après l'ajout.
            if(t-a[i]>=0):
                # on teste si l'ajout de la pièce diminue le nombre
                # de pièces à rendre et dans ce cas on l'ajoute
                if (Z[i-1][t]>1+Z[i][t-a[i]]):
                    Z[i][t]=1+Z[i][t-a[i]]
                    # dans ce cas on vient de la gauche
                    sol[i][t]='g'
                # sinon on garde la solution précedente
                else:
                   Z[i][t]=Z[i-1][t]
                   # dans ce cas on vient du haut
                   sol[i][t]='h'
            # sinon on garde forcément la solution précedente parce
            # qu'on ne peut pas utiliser cette pièce.
            else:
               Z[i][t]=Z[i-1][t]
               # dans ce cas on vient du haut
               sol[i][t]='h'
            if debug:
                affTab(Z)

    s=[]
    i=n-1
    t=S
    # on par de la fin et on remote jusqu'au debut du tableau
    while(i>=0 and t>=0):
            # on regarde si on vient de la gauche
            if (sol[i][t]=='g'):
               # si c'est le cas, on a utilisé forcément la pièce
               s.append(a[i])
               # on n'oublie pas d'enlever la pièce utilisée de
               # la somme et on recommence la procédure avec la
               # somme actuelle diminuée de a[i]
               t=t-a[i]


            else:
               # sinon du haut et on n'a pas utilisé de pièce.
               # il suffit de remonter vers le haut et on recommence
               # la procedure avec la somme actuelle à l'indice i-1
               i=i-1
    if(debug):
        print()
        print("changer le paramètre debug en False si vous ne voulez",
              "\npas voir tous les affichages")
        print()
    return Z[n-1][S],s
#fin de la fonction nbPieceMin


"""================================TD========================================"""


#debut exercice1

#debut de la fonction sacDos
def sacDos(p,v,Pmax,debug=False):
    # cette fonction une liste de poids p, de valeurs v correspondantes
    # et essaie de retourner la valeur optimale sous la contrainte
    # la somme des poids doit inférieure à Pmax.

    # ENTREE: p la liste des poids
    #        v la liste des valeurs dans le même ordre que les poids
    #        Pmax la valeur du poids maximal autorisé
    #        debug un boolean qui permet d'activer ou desactiver les
    #        affichages intermédiaires.

    # SORTIE: val_opt la valeur optimale possible pour ce poids maximal
    #         v_ut les valeurs utilisées
    #         p_ut les poids utilisés
    if(debug):
        print()
        print("changer le paramètre debug en False si vous ne voulez",
              "\npas voir tous les affichages")
        print()
    # on ajoute les poids nuls et valeurs nulles aux listes
    # correspondantes
    p=[0]+p
    v=[0]+v

    # n est le nombre d'objet, c'est également la taille du vecteur poids
    n=len(p)

    # on cree un tableau de n lignes avec Pmax+1 colonnes initialisé à 0
    # pour memoriser les resultats intermediaires
    Z=creerTableau(n,Pmax+1,0)

    # on cree un tableau de n lignes avec Pmax+1 colonnes initialisé à avec la
    # la chaine de caractères vide pour les chemins vers la solution finale
    # dans le tableau. On va remplir ensuite ce tableau comme suit:
    #          h: si on garde la precedente de la ligne precedente
    #          g: si on a amelioré la valeur de la ligne precedente.
    sol=creerTableau(n,Pmax+1,"")

    if debug:
        print("Test du tableau avant les calculs")
        affTab(Z)
    # on remplit progressivement le tableau en partant du debut qui est
    # initialisé à zero par contruction
    for i in range(1,n):
        for j in range(1,Pmax+1):
            # on teste si on peut mettre le poids actuels
            if((j-p[i])>=0):
                # si oui on teste si en l'ajoutant la valeur sera ameliorée
                if((Z[i-1][j-p[i]]+v[i])>Z[i-1][j]):
                    # si oui on l'ajoute et on diminue le poids restant du poids
                    # qu'on vient d'ajouter.
                    Z[i][j]=(Z[i-1][j-p[i]]+v[i])
                    # dans ce cas on a amelioré la valeur donc c'est g qu'on
                    # affecte à la position actuelle dans le tableau sol
                    sol[i][j]='g'
                else:
                    # sinon on garde la valeur de la ligne precedente
                    Z[i][j]=Z[i-1][j]
                    # on n'a rien amelioré donc on vient du haut
                    sol[i][j]='h'
            else:
                # sinon on garde la valeur de la ligne precedente
                Z[i][j]=Z[i-1][j]
                # on n'a rien amelioré donc on vient du haut
                sol[i][j]='h'
    val_opt=Z[n-1][Pmax];
    if debug:
        print("Test du tableau après les calculs")
        affTab(Z)
    if debug:
        print("Test du tableau des chemins après les calculs")
        affTab(sol)
    # on n'initialise les valeurs et poids utilisés
    v_ut=[]
    p_ut=[]
    # on part de la fin du tableau et on essaie de retrouver le chemin que nous
    # avons suivi.
    i=n-1
    j=Pmax
    while(i>0 and j>0):
            # on teste si on vient de la gauche ou du haut
            if (sol[i][j]=='g'):
               # si on vient de la gauche alors on a forcément utilisé l'objet
               # actuel donc donc on ajoute sa valeur à v_ut et son poids à p_ut
               v_ut.append(v[i])
               p_ut.append(p[i])
               # on diminue le poids restant du poids de l'objet courant en
               # en allant à la ligne precedente.
               j=j-p[i]
               i=i-1

            else:
               # sinon a n'a pas utilisé l'objet et il suffit donc d'aller
               # à la ligne précedente.
               i=i-1
    if(debug):
        print()
        print("changer le paramètre debug en False si vous ne voulez",
              "\npas voir tous les affichages")
        print()
    # on retourne le tuple constitué constitué du dernier element du tableau, du
    # la liste des valeurs utilisées et de la liste des poids utilisées.
    return val_opt,v_ut, p_ut
#fin de la fonction sacDos

#fin exercice1

# debut exercice 2
def PLSC(X,Y,debug=False):
    # cette fonction prend deux chaines de caractères et recherche la plus
    # longue sous-sequence commune

    # ENTREE: X une chaine de caractères
    #         Y la seconde chaine de caractères
    #         debug un boolean qui permet d'activer les affichages
    #         intermédiaires

    # SORTIE: t_plsc un entier qui correspond à la taille de la plus longue
    #         sous-sequence commune
    #         sd   une chaine de caractère qui est une sous-sequence commune
    #         de X et Y
    if(debug):
        print()
        print("changer le paramètre debug en False si vous ne voulez",
              "\npas voir tous les affichages")
        print()

    # on prend les tailles de X et Y
    I=len(X)
    J=len(Y)
    # on cree un tableau initialisé à zero pour memoriser les tailles des sous-
    # sequences communes intermédiaires
    Z=creerTableau(I+1,J+1,0)

    # on cree un tableau initialisé avec la chaine vide pour memoriser les
    # les directions de descente de l'evolution de la taille de la sous-sequence
    # communine avec la règle suivante:
    #             dia: si on vient de la diagonale i.e les deux caractères
    #                  actuels sont identiques
    #             g: si on vient de la gauche
    #             h: si on vient du haut
    sol=creerTableau(I,J,"")

    # on remplit le tableau à partir du debut
    for i in range(I):
        for j in range(J):
            # on teste si les deux caractères courants sont identiques ou non
            if(X[i]==Y[j]):
                # si ils sont identiques alors on peut ameliorer la solution
                # qu'on avait à la diagonale de 1 à cette position
                Z[i][j]=Z[i-1][j-1]+1
                # on vient de la diagonale donc on n'oublie d'assigner "dia"
                # dans le tableau sol à cette position
                sol[i][j]="dia"
            else:
                # sinon on garde la plus grande valeur les valeurs precedente en
                # colonne et en ligne
                if(Z[i-1][j]>Z[i][j-1]):
                     # si la precedente en ligne est meilleure alors on l'a
                     # garde pour la position actuelle et on vient de la gauche
                     # (deplacement en ligne)
                     Z[i][j]=Z[i-1][j]
                     sol[i][j]="g"
                else:
                    # si la precedente en colonne est meilleure alors on l'a
                    # garde pour la position actuelle et on vient du haut
                    # (deplacement en colonne)
                    Z[i][j]=Z[i][j-1]
                    sol[i][j]="h"

    # la taille de la plus longue sous sequence commune à retourner
    t_plsc=Z[I-1][J-1]
    if debug:
        print("le tableau après le remplissage")
        affTab(Z)
        print("tableau des chemins")
        affTab(sol)
    #la sous sequence commune en diagonale(à retourner)
    sd=""

    # on part de la fin du tableau des solutions intermédiaires jusqu'à son
    # debut et on essaie de voir d'où l'on vient.
    i=I-1
    j=J-1
    while(i>=0 and j>=0):
            # si on vient de la gauche alors il faut decrementer la ligne de 1
            if (sol[i][j]=='g'):
                i=i-1

            # sinon si on vient du haut alors il faut decrementer la colonne de
            # 1
            elif(sol[i][j]=='h'):
                j=j-1

            # sinon on vient de la diagonale, il faut ajouter à gauche le cara-
            # ctère courant dans la chaine X( ou Y).
            # on n'oublie pas de decrementer la ligne et la colonne de 1 pour se
            # retrouver à la position diagonale precedente
            else:
                sd=X[i]+sd
                i=i-1
                j=j-1

    if(debug):
        print()
        print("changer le paramètre debug en False si vous ne voulez",
              "\npas voir tous les affichages")
        print()

    # on retourne donc la taille de la sous-sequence max et une sous-sequence
    return t_plsc,sd
# fin exercice 2



# debut exercice 3

# debut fonction distEd
def distEd(Source,Target,debug=False):

    # cette fonction prend une chaine Source et une liste Target et retourne
    # le nombre minimal de modifications pour retrouver la chaine Target

    # ENTREE: Source : la liste source
    #         Target : la liste cible
    #         debug: un boolean qui active les affichages intermédiaires.

    # SORTIE: les affichages des types modifications( rien faire,
    #                                           substitution, suppresion, ajout)
    #         nb_mod : le nombre minimal de modifications

    if(debug):
        print()
        print("changer le paramètre debug en False si vous ne voulez",
              "\npas voir tous les affichages")
        print()
    # on ajoute le caractère vide au debut de chaque chaine
    Source=" "+Source
    Target=" "+Target

    # on prend leurs longeurs
    I=len(Source)
    J=len(Target)

    # on cree le tableau contenant les solutions intermédiaires.
    Z=creerTableau(I,J,0)

    # on initialize la première ligne et la première colonne comme decrit
    # dans la relation de la recursion

    for i in range(I):
        Z[i][0]=i
    for j in range(J):
        Z[0][j]=j
    for i in range(1,I):
        for j in range(1,J):
            # on teste d'abord si les deux caractères actuels sont identiques
            # on utilise c pour la valeur de l'ajout
            # si les deux caractères sont identiques alors l'ajout est nul
            # sinon l'ajout vaut bien entendu 1
            if(Source[i]==Target[j]):
                c=0
            else:
                c=1

            # on affecte à la possition actuelle le minimum entre la valeur en
            # diagonal precedent +c; la valeur de la colone precedente+ 1 et la
            # la valeur de la ligne precedente +1.
            Z[i][j]=min(Z[i-1][j-1]+c, Z[i][j-1]+1, Z[i-1][j]+1)

    # nb_mod est le nombre de modifications minimum pour atteindre la cible
    nb_mod=Z[I-1][J-1]


    if debug:
        print()
        print("Tableau après le remplissage")
        affTab(Z)

    print(source,"------->",target)

    # on va afficher la liste des modifications pour aller de source et target
    # à partir de la fin jusqu'au début mais on n'oublie pas qu'on ajouté le
    # caractere vide au début
    i=I-1
    j=J-1
    t=target
    s=source
    while(i>=1 and j>=1):
      # on cherche le minimum entre le nombre de modifications dans les
      # positions les plus proches devant nous( nous venons de la fin du
      # tableau)
      tmp=min(Z[i-1][j-1], Z[i][j-1], Z[i-1][j])

      # si ce minimum est dans la colonne actuelle alors il s'agit d'une
      # insertion
      if(tmp==Z[i-1][j]):
          i=i-1
          # on fait la transformation str<-->list pour pouvoir modifier un
          # un caractere a une position precise car les chaines sont
          # immuables donc on ne peut pas les modifier directement.
          l_t=list(t)
          l_t=list(t[:j])+[s[i].upper()]+list(t[j:])
          t=''.join(l_t)
          print("insertion",s,"------->",t)

      # sinon si ce minimum est sur le diagonal davant nous alors il y a deux
      # cas
      elif(tmp==Z[i-1][j-1]):
         # on teste si la valeur sur ce diagonal devant nous est la meme chose
         # que le nombre de modifications à la position actuelle. Si c'est le
         # cas alors on a fait aucune modification
         if(Z[i-1][j-1]==Z[i][j]):
             i=i-1
             j=j-1
             print("sansModif",s,"------->",t)

         # sinon on a fait une substitution
         else:
             i=i-1
             j=j-1
             # on fait la transformation str<-->list pour pouvoir modifier un
             # un caractere a une position precise car les chaines sont
             # immuables donc on ne peut pas les modifier directement.
             l_t=list(t)
             l_t[j:j+1]=s[i:i+1].upper()
             t=''.join(l_t)
             print("substitution",s,"------->",t)

      # si ce minimum est dans la ligne actuelle alors il s'agit d'une
      # suppression
      elif(tmp==Z[i][j-1]):
          j=j-1
          # on fait la transformation str<-->list pour pouvoir modifier un
          # un caractere a une position precise car les chaines sont
          # immuables donc on ne peut pas les modifier directement.
          l_t=list(t)
          l_t.pop(j)
          t=''.join(l_t)
          print("suppression",s,"------->",t)

    if(debug):
        print()
        print("changer le paramètre debug en False si vous ne voulez",
              "\npas voir tous les affichages")
        print()

    return nb_mod
# fin de la fonction distEd

# fin exercice 3


# pour tester les fonctions implementées: Pour afficher les resultats intermé-
# diaires il suffit de mettre debug à True
if __name__=="__main__":
    opt=""
    if len(sys.argv)==2:
        script,opt=sys.argv

    if(opt=="cours"):
        print()
        print("test de l'exemple du cours")
        a=[1, 2, 5, 10]
        S=12
        nb=nbPieceMin(S,a,debug=True)
        if(len(nb[1])==0):
            print("On ne peut pas rendre cette monnaie avec les pièces ",
                  "actuelles")
        else:
            print("nombre de pièces",nb[0],"avec les pièces",nb[1])


    elif(opt=="exo1"):
        print()
        print("test de l'exercice 1")
        v=[3,7,4,2]
        p=[4,7,5,2]
        Pmax=15
        solution=sacDos(p,v,Pmax,debug=True)
        print("Valeur optimale:",solution[0],
              "avec les valeurs",solution[1],
              "de poids",solution[2])


    elif(opt=="exo2"):
        print()
        print("test de l'exercice 2")
        X="abcbdab"
        Y="bdcaba"
        solution=PLSC(X,Y,debug=True)
        print("Taille de la plus longue sous sequence:",solution[0],
              "\nUn exemple de sous sequences max commune:",solution[1].upper())


    elif(opt=="exo3"):
        print()
        print("test de l'exercice 3")
        source="tests"
        target="twist"
        solution=distEd(source,target,debug=True)
        print()
        print("Nombre d'édition entre",source, target,solution)

    else:
        print("Choisissez une option avec la commande:")

        print("        run ", sys.argv[0],
              "[options= cours, exo1, exo2 ou exo3](CONSOLE IPYTHON)")

        print("        ou")
        print("        python3 ", sys.argv[0],
              "[options= cours, exo1, exo2 ou exo3](TERMINAL UNIX)")

    # on saute des lignes pour differencier les sorties
    print()
    print()
