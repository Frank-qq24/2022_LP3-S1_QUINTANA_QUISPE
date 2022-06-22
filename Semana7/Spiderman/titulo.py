# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:37:48 2022

@author: Frank
"""
#importamos la libreria
import camelcase

nombre = "flor Elizabeth Cerdan Leon"

print(nombre.upper())
print(nombre.title())

#creamos un  objeto llamado campo

cam= camelcase.CamelCase()

print("con Camelcase....")

#imprimimos el nombre en odrmato titulo
# utlizamos camelcase
print(cam.hump(nombre))

# para resolver el problmea creamos otro objeto

cam2 =camelcase.CamelCase('flor', 'leon')
print(cam2.hump(nombre))

