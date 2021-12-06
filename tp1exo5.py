# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:29:39 2021

@author: e2101592
"""

import random

nombrealeatoire = random.randint(0, 100)
print(nombrealeatoire)
if  nombrealeatoire < 50:
    print("Pile!")
else:
    print ("Face!")
