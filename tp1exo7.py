# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:29:39 2021

@author: e2101592
"""

import random

nombrealeatoire = random.randint(1, 3)
if  nombrealeatoire < 2:
    print("Face!")
else:
    print ("Pile!")
