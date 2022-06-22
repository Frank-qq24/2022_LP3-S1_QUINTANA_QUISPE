# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:17:01 2022

@author: Frank
"""

try:
    numerador = float(input("Numerador: "))
    denominador = float(input("Denominador: "))
    resultado = numerador/denominador
    print(f"Resultado = {resultado}")

except ZeroDivisionError:
    print("No puedes dividir entre cero...")

except:
    print("hubo un error")
else:
    print("la division se realizao correctamente")
finally:
    print("La operacion termino")