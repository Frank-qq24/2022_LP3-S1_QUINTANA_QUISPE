# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:33:47 2022

@author: Frank
"""

noticia = open("noticia.txt","rt",encoding='utf8')
datos_noticia = noticia.read()
print(datos_noticia)