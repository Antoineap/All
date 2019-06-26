import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
			
			
v=[1,2,3]
v.max()
sort(v)
v.sort()
v.last()
v[-1]
mean(v)	

txt = "welcome to the jungle"

x = txt.split()

print(x)


factoriel de n python


#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt		# Importation de la fonction racine carré
from random import random	# Importation de la fonction aléatoire

NombreHistoires = 10000000	# Nombre de réalisations d'histoires
Compteur= 0			# Nombre de fois que l'on se trouve dans le cercle

for i in range(NombreHistoires):
	x = random()		# Composante sur x aléatoire
	y = random()		# Composante sur y aléatoire
	r = sqrt(x**2+y**2)	# Calcul de la distance entre le centre et le point
	if r <= 1:		# Vérification que le point se trouve dans le cercle
		Compteur = Compteur + 1

Pi = 4 * Compteur / NombreHistoires

print("Pi = %f" % Pi)	
