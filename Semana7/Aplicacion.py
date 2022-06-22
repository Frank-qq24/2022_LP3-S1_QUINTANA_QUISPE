# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:43:00 2022

@author: Frank
"""
import Gestion_de_archivo

def menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Agregar Contenido")
    print("4. Mostrar contenido de Archivo")
    print("5. Salir")
    
def crear():
    print("** CREAR ARCHIVO **")
    archivo = input("crear archivo")
    contenido = input("contenido del archivo: ")
    Gestion_de_archivo.crear_archivo(archivo, contenido)
    
def eliminar():
    print("** ELIMINAR ARCHIVO **")
    archivo = input("Quirro eliminar el archivo: ")
    Gestion_de_archivo.eliminar_archivo(archivo)
    
def agregar():
    print("*** AGREGAR CONTENIDO A UN ARCHIVO ***")
    archivo = input("Quiero Agregar contenido al archivo: ")
    contenido = input("El contedio adicional del archivo es: ")
    Gestion_de_archivo.agregar_contenido_archivo(archivo, contenido)
    
def listar():
    print("*** MOSTRAR CONTDIO DE ARCHIVO ***")
    archivo = input("Quiero listar el contenido del archivo archivo: ")
    return Gestion_de_archivo.leer_archivo(archivo)
    
def error(): 
    print("Opcion incorrecta")
    
def salir():
    print("Gracias... Vuelva pronto")
    
# La lógica para el menu de opciones
opcion = 1
while opcion!=5:
    menu()
    opcion = int(input("Seleccione una opción [1-5]: "))
    if opcion ==1:
        crear()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        listar()
    elif opcion == 5:
        salir()
    else:
        error()
    