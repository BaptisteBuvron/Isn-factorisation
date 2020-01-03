#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  second_degre_sans_fonction.py

from math import sqrt   #  Depuis le module math importer la fonction sqrt


# Fonction saisie sur le programme avec fonction 
print("Donner les trois coefficients réels \ndu trinome du second degré ax²+bx+c")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))


# Fonction verification_a sur le programme avec fonction
while a==0 :
	print("******************************")
	print("attention, a doit etre non nul")
	a=float(input("a="))


	print("******************************")



# Fonction calcul_delta sur le programme avec fonction

DELTA=b**2-4*a*c #Delta prend la valeur de b**2-4*a*c
print("La valeur du discriminant est : " , DELTA)


# Fonction verification_delta sur le programme avec fonction

if DELTA < 0 : #  Si delta est égale à 0
	print("Ce trinome n'est pas factorisable")


elif DELTA == 0 : #  Si delta est égale à 0
	x_0=-b/(2*a)  #  x_0 prend la valeur de : -b/(2*a)
	print("La forme factorisée de ce trinome est : " , a , "(x-",x_0,")²")


else :  #  Sinon
	x_1=(-1*b + sqrt(DELTA))/(2*a)  #  x_1 prend la valeur de : (-1*b + sqrt(DELTA))/(2*a)
	x_2=(-1*b - sqrt(DELTA))/(2*a)  #  x_2 prend la valeur de : (-1*b - sqrt(DELTA))/(2*a)
	print("La forme factorisée de ce trinome est : "  , a , "(x-",x_1,")(x-" , x_2, ")")



