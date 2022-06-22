# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:56:17 2022

@author: Frank
"""

# Necesitamos mostrar los nombres de una cadena
# prestando las primeras letras en mayuscula
# en word se conoce como formato titulo

#import la libreria

import camelcase

nombre = "frank raul quintana quispe"

print(nombre.upper())
print(nombre.title())

cam = camelcase.CamelCase()
print("Con camelcase ......")

#Imprimimos el nombre en formato titulo
# Utilizamos camecase
print(cam.hump(nombre))

# para resolver el problema 
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos

cam2 = camelcase.CamelCase("frank","quintana")
print(cam2.hump(nombre))