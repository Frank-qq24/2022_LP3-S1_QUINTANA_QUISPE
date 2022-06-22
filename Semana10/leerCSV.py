# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 09:18:00 2022

@author: Frank
"""

import csv 
# Abrimos el archivo indicanco el PATH y el enconding = utf para leer caracteres 

# Abrimos el archivo indicando el PATH y el encoding=utf para leer carateres especiales

with open('Global_Mobility_Report.csv', encoding="utf8") as f:
    datos = csv.reader(f, delimiter=',')
    for fila in datos:
        if fila[0]=="PE" and fila[2]=="Puno":
            print(f"{fila[0]}\t{fila[1]}\t{fila[2]}\t{fila[3]}\t{fila[4]}\t{fila[5]}\t{fila[6]}\t{fila[7]}\t{fila[8]}\t{fila[9]}\t{fila[10]}")