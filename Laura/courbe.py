#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:23:15 2020

@author: lauraproudhon
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import os
def getXYFromFile(fileNameX, fileNameY):
    lignes_X = []
    lignes_Y = []

    pathX = "%s/%s" % (os.getcwd(), fileNameX)

    fichier_X = open(pathX, "r", encoding='utf-8-sig')
    lignes_X = fichier_X.readlines()

    pathY = "%s/%s" % (os.getcwd(), fileNameY)

    fichier_Y = open(pathY, "r", encoding='utf-8-sig')
    lignes_Y = fichier_Y.readlines()

    X_temp =[]
    Y_temp =[]
    X = []
    Y = []

    #On ajoute les valeurs à des tableaux temporaires. A ce moment, l'utilisation de la fonction strip permet d'enlever les \n du tableau
    #Mais il reste les lignes vides (si il y en a dans le fichier)
    for x in lignes_X:
        print(x.strip())
        X_temp.append(x.strip())

    for y in lignes_Y:
        print(y.strip())
        Y_temp.append(y.strip())

    #Permet de retirer les lignes vides dans les tableaux
    for string in X_temp:
        if(string != ''):
            X.append(string)

    for string in Y_temp:
        if(string != ''):
            Y.append(string)
    return X,Y
X, Y = [], []


X, Y = getXYFromFile("Lxdoigt.txt", "Lydoigt.txt")

print(X)
print(Y)

mpl.use('Tkagg')

fig,ax = plt.subplots(1)

fig.suptitle("Trajectoire du point M")

ax.plot(X,Y, 'ro')
ax.set_ylabel('Abscisse X')
ax.set_xlabel('Ordonnées Y')
ax.set_yticklabels([])
ax.set_xticklabels([])

plt.show()