# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 09:10:39 2022

@author: Frank
"""

import sqlite3

# Con el comando connect buscará la base de datos
# que tenga ese nombre, de lo contrario lo creará.
conexion = sqlite3.connect("bdbiblioteca.db")

# En una cadena guardaremos el script de creacion de la tabla pais
#tabla_pais = """CREATE TABLE pais(
#                    idpais INTEGER PRIMARY KEY AUTOINCREMENT,
#                    nombre TEXT UNIQUE,
#                    estado TEXT
#                    )
#            """
tabla_editorial = """ CREATE TABLE editorial(
                        ideditorial INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        estado TEXT
                    )
            """

tabla_autor = """ CREATE TABLE autor(
                    idautor INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    f_nacimiento TEXT
                    )
            """
tabla_libro = """ CREATE TABLE libro(
                    idlibro INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    cantidad INTEGER,
                    anio INTEGER,
                    precio REAL,
                    estado TEXT,
                    idpais INTEGER REFERENCES pais,
                    ideditorial INTEGER REFERENCES editorial,
                    idautor INTEGER REFERENCES pais
                    )
            """

cursor = conexion.cursor()

#cursor.execute(tabla_pais)
cursor.execute(tabla_editorial)
cursor.execute(tabla_autor)
cursor.execute(tabla_libro)

conexion.close()
