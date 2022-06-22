# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:50:01 2022

@author: Frank
"""
import financiero
subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV: {financiero.ObtenerIGVSubtotal(subtotal): .2f}")
print(f"Total: {financiero.obtenerTotalconSubtotal(subtotal): .2f}")


