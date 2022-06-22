# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:43:34 2022

@author: Frank
"""
import sqlite3
conexion =  sqlite3.connect("bdbiblioteca.db")

consulta = """
                INSERT INTO
                    PAIS(NOMBRE, ESTADO)
                    VALUES('BRASIL','A')
            """ 
curso =  conexion.curso()
curso.execute(consulta)

# el commit
conexion.commit()
conexion.close()