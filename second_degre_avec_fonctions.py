#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  second_degre_avec_fonction.py

from math import sqrt   #  Depuis le module math importer la fonction sqrt

#        fonctions        #
########################### 

def saisie(): 
    print("Donner les trois coefficients réels \ndu trinome du second degré ax²+bx+c")
    a=float(input("a=")) # saisie de la valeur de a
    b=float(input("b=")) # saisie de la valeur de b
    c=float(input("c=")) # saisie de la valeur de c
    return a,b,c #Retourner les valeurs de a, b et c

def verification_a(a):
    while a==0: #Tant que a est égale à 0
        print("******************************")
        print("attention, a doit etre non nul")
        a=float(input("a=")) # saisie de la valeur de a
        print("******************************")
    return a #Retourner la valeur de a

def calcul_delta(a,b,c):
    DELTA = b**2-4*a*c #Delta prend la valeur de b**2-4*a*c
    print("La valeur du discriminant est : ", DELTA)
    return DELTA #Retourner la valeur de DELTA

def verification_delta(a,b,c,DELTA):
    if DELTA < 0: #  Si delta est égale à 0
        print("Ce trinome n'est pas factorisable")

    elif DELTA == 0: #  Si delta est égale à 0
        x_0 = -b/(2*a) #  x_0 prend la valeur de : -b/(2*a)
        print("La forme factorisée de ce trinome est : " , a , "(x-",x_0,")²")

    else: #  Sinon
        x_1 = (-1*b + sqrt(DELTA))/(2*a) #  x_1 prend la valeur de : (-1*b + sqrt(DELTA))/(2*a)
        x_2 = (-1*b - sqrt(DELTA))/(2*a) #  x_2 prend la valeur de : (-1*b - sqrt(DELTA))/(2*a)
        if x_1 >= 0:
            x_1 = "+"+str(x_1)
        if x_2 >= 0:
            x_2 = "+"+str(x_2)


        print("La forme factorisée de ce trinome est : "  , a , "(x",x_1,")(x" , x_2, ")")

def second_degre():
    a,b,c = saisie() #la variable a prend la valeur de la variable a de la fonction saisie, de même pour b et c
    a = verification_a(a) #la variable a prend la valeur de la variable a de la fonction verification_a avec comme paramètre a 
    DELTA = calcul_delta(a,b,c) #la variable a prend la valeur de la variable a de la fonction calcul_delta avec comme paramètres a,b et c 
    verification_delta(a,b,c,DELTA) # Appel de la verification_delta avec comme paramètres a,b,c et DELTA



########################### 
#   Programme principal   #
########################### 

reponse = "oui"
while reponse == "oui" :
	print("*********************************************************************************")
	print("voulez-vous connaître la factorisation éventuelle d’un trinôme du second degré ? ")
	reponse = input() # la variable reponse prend la valeur de la saisie de l'utilisateur
	print("\n")
	if reponse == "oui" : # Si reponse est égale à "oui"
		second_degre() # Appeler la fonction second_degre
	else : 
		print("au revoir")