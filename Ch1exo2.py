#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 09:18:13 2017

@author: arek
"""

from time import clock #pour mesurer les temps

def minMax1(L):
    """
    entrée: liste L
    sortie:(m,M) le min et le max de la liste"""

    start=clock()
    n=len(L)
    m=L[0]
    M=m
    for i in range(n):
        if(L[i]<m): m=L[i]
        if(L[i]>M): M=L[i]
    elapsed=clock()
    print("Temps minMax1", elapsed-start)
    return [m,M]

def minMax2(L):
    """
    entrée: liste L de taille paire
    sortie:(m,M) le min et le max de la liste"""

    n=len(L)
    m=L[0]
    M=m
    start=clock()
    for i in range(0,n,2):
        if(L[i]<L[i+1]):
            if(L[i]<m): m=L[i]
            if(L[i]>M): M=L[i]
        else:
            if(L[i+1]<m ):  m=L[i+1]
            if( L[i]>M  ):  M=L[i]
    elapsed=clock()
    print("Temps minMax2", elapsed-start)
    return [m,M]

""" Cette partie est pour tester le code"""
from random import random # pour générer les nombres aléatoires
n=100000
L=[]
for i in range(n):
    L.append(random())

minMax1(L)
minMax2(L)

