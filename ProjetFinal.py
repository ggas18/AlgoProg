#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:27:24 2017

@author: arek
"""
#les outils natifs de python à importer.
import sys # pour la reception des arguments en ligne de commandes.

# fin imports


# debut frequence
def frequence(text):
    # cette fonction extraire à l'alphabet et à le ponderer dans un texte avec
    # les frequences d'apparitions
    # ENTREE text: une chaine de caracteres

    # SORTIE freq: un dictionnaire de cles les lettres et de valeurs les
    #         frequences
     freq={}
     n=len(text)
     for i in range(n):
         # on teste si la lettre est deja dans le dictionnaire ou non
         f_lettre=freq.get(text[i])
         if(f_lettre==None):
             # si la lettre n'est pas dans le dictionnaire, on le met avec la
             # frequence 1 comme valeur
             freq[text[i]]=1
         else:
             # si la lettre est deja dans le dictionnaire on remet la frequence
             # a jour
             freq[text[i]]=f_lettre+1
     return freq
# fin frequence

# debut Node
class Node:
    def __init__(self,lettreAlphabet,freq,filsG,filsD):
        self.cle=lettreAlphabet
        self.filsG=filsG
        self.filsD=filsD
        self.freq=freq
    def __repr__(self):
        #return "Node: lettre: {} freq: {}".format(self.cle,self.freq)
        return " {} freq: {}".format(self.cle,self.freq)

    def __str__(self):
        #return "Node: lettre: {} freq: {}".format(self.cle,self.freq)
        return " {} freq: {}".format(self.cle,self.freq)

    def __lt__(self, other):
        return self.freq<other.freq

# fin Node

# construction de l'arbre
def arbre(Alphabet):
    # cette fonction l'alphabet avec frequences et construits l'arbre

    # ENTREE: listAlphabet dictionnaire des caracteres avec les frequences
    #         correspondantes

    # SORTIE: arbre: l'arbre de Huffman qui est de type Node
    taille_alpha=len(Alphabet)
    list_chaine=list(Alphabet.keys())
    l_noeud=[]
    for i in range(taille_alpha):
       l_noeud.append(Node(list_chaine[i],Alphabet.get(list_chaine[i]),None,None))
    l_noeud=sorted(l_noeud)
    while(len(l_noeud)>1):
        noeud=Node(l_noeud[0].cle+l_noeud[1].cle,l_noeud[0].freq+l_noeud[1].freq,l_noeud[0],l_noeud[1])
        #print(l_noeud)
        for j in range(len(l_noeud)):
            if(l_noeud[j]<noeud): continue
            else: break
        l_noeud=l_noeud[:j+1]+[noeud]+l_noeud[j+1:]
        l_noeud.remove(l_noeud[0])
        l_noeud.remove(l_noeud[0])
    return l_noeud[0]
# fin construction de l'arbe

# debut codage
def codage(arbreHuffman,c,codeDict):
    if(arbreHuffman.filsG==None and arbreHuffman.filsD==None):
        codeDict[arbreHuffman.cle]=c
    if(arbreHuffman.filsG!=None):
        c=c+"0"
        codage(arbreHuffman.filsG,c,codeDict)
        c=c[:len(c)-1]
    if(arbreHuffman.filsD!=None):
        c=c+"1"
        codage(arbreHuffman.filsD,c,codeDict)
        c=c[:len(c)-1]


# fin codage
# debut compression
def compression(text):
    freq=frequence(text)
    arbreHuffman=arbre(freq)
    T=len(text)
    textCompr=""
    codeDict={}
    c=""
    codage(arbreHuffman,c,codeDict)
    for t in range(T):
        ch=codeDict.get(text[t])
        textCompr=textCompr+ch
    return textCompr
# fin compression
if __name__=="__main__":
    opt=""
    if len(sys.argv)==2:
        script,opt=sys.argv
    if(opt=="Huffman" or opt=="huffman"):
             text="abrakadabra"
             print(compression(text))

    else:
        print("Choisissez une option avec la commande:")

        print("        run ", sys.argv[0],
              "[options= Huffman](CONSOLE IPYTHON)")

        print("        ou")
        print("        python3 ", sys.argv[0],
              "[options= Huffman](TERMINAL UNIX)")

    # on saute des lignes pour differencier les sorties
    print()
    print()