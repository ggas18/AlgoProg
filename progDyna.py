#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:22:25 2017

@author: arek
"""
def affTab(L):
    n=len(L)
    for i in range(n):
        print(L[i])
    return

"""===================== pour les tests ============================"""
a=[1, 2, 5, 10]
S=12
"""======================fin données pour les test==================="""
def nbPieceMin(S,a):
    n=len(a)
    Z=[[0]*n]*S;
    for i in range(n):
        Z[0][i]=0
    for t in range(0,S):
        Z[t][0]=t
    for t in range(1,S):
        for i in range(n):
            Z[t][i]=min(Z[t][i],1+Z[t-a[i]][i])

    return Z[S-1][n-1]