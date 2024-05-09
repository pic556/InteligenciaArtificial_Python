# -*- coding: utf-8 -*-
import random

from random import randint
from fuzzywuzzy import fuzz

abecedario = "abcdefghtyjklmñnopqrstuvwyxz"

def palabra_4(palabra):
    return (len(palabra)==4)


def palabra_gen():
    pa_1 = ''
    for _ in range(4):
        pa_1 += random.choice(abecedario)
    return pa_1

def armando_opciones(palabras_opcionales):
    pa_op =[]
    for i in range(palabras_opcionales):
        pa_i = palabra_gen()
        pa_op.append(pa_i)
    return pa_op


def seleccionar(pa_op,palabra,seleccion):
    seleccionados=[]
    for j in range(seleccion):
        maximo=0
        for i in pa_op:
            if(fuzz.ratio(palabra,i) >maximo):
                  maximo = fuzz.ratio(palabra,i)
                  indice= pa_op.index(i) 
        seleccionados.append(pa_op[indice])
        pa_op.pop(indice)
 
            
    print("La siguiente generacion de seleccionados es" ,seleccionados)        
    return seleccionados


def heredar(seleccionados,palabras_opcionales):
    nueva=[]
    for i in range(palabras_opcionales):
        p = seleccionados[random.randint(0,1)][0]
        a = seleccionados[random.randint(0,1)][1]
        l = seleccionados[random.randint(0,1)][2]
        a2 = random.choice(abecedario)
        nueva.append(p+a+l+a2)
    print("La siguiente generacion de opciones es" , nueva)
    return nueva







def pala():
        pa = input("Por favor, ingresa una palabra: ")
        palabras_opcionales=5 #crear 5 individuos
        seleccion=2 #selecionar los mejores 2 individuos de la generacion
        generaciones=30 #cantidad de vecexs que se repite 
        if palabra_4(pa):
            opciones_enlistadas = armando_opciones(palabras_opcionales)
            for i in range (generaciones-1):    
                sele = seleccionar(opciones_enlistadas,pa,seleccion)
                here = heredar(sele,opciones_enlistadas)
            seleccionar(opciones_enlistadas,pa,seleccion)
        else:
            pala()

pala()
