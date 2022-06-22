# -*- coding: utf-8 -*-
"""
Las librerias te permitiran crear librerias de
funcionalidades que puedas utilizar o reutilizar 
en cualquier momento
"""
igv=0.18

def ObtenerIGVSubtotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    return subtotal*(1+igv)

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)
