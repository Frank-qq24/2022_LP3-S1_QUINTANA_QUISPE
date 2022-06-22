# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:03:00 2022

@author: Frank
"""

archivo = open("noticia.txt", "at")
#\n es para agregar el contenido en una línea final 
contenido = "\nFuente: RPP Noticias"

archivo.write(contenido)
archivo.close()