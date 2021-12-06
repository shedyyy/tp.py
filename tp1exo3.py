# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

jours=int(input("Saisir un jour : "))
heures=int(input("Saisir une heure : "))
minutes=int(input("Saisir une minute : "))
temp = minutes + (60 * heures) + (1440 * jours)
print(temp , "minutes écoulées")

