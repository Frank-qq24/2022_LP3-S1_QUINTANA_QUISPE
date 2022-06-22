# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:26:06 2022

@author: Frank
"""

import sqlite3

#con el comando connect buscará la base de datos
# que tenga ese nombre, de lo contrario lo creará

conexion=sqlite3.connect("bdbiblioteca.db")
conexion.close()