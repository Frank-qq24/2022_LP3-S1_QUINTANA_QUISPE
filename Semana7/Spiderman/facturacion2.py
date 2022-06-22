# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:52:59 2022

@author: Frank
"""
#Dadro el total

#Dado el total, calcular el IGV y el subtotal

import financiero
total = 1000.49
print(f"Subtotal: {financiero.obtenerSubtotalconTotal(total): .2f}")
print(f"IGV: {financiero.obtenerIGVconTotal(total): .2f}")
print(f"Total: {total}" )
