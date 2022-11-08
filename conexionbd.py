#!/usr/bin/env python
# coding :-*-  UTF-8 -*-

import sqlite3
import mysql.connector
from mysql.connector import Error

# en la pc de escritorio no hay contraseña
# en la laptop la contraseña es incade

class Conexion:
    #conexion    
    def __init__(self):      
        try:
            self.inmobiliaria = mysql.connector.connect(
                user = 'root',
                password = 'incade',
                host = 'localhost',
                database = 'inmobiliaria',
                port = 3306
            )        
        except Error as ex:
            print("Error en conexion: {0}".format(ex))

    # visualizacion       
    def listarPropiedades(self):

        if self.inmobiliaria.is_connected():

            try:

                mycursor = self.inmobiliaria.cursor()
                mycursor.execute("SELECT * FROM inmobiliaria.propiedad;")
                lista = mycursor.fetchall()                
                for x in lista:
                    print(x) 

            except Error as ex:
                print("Error en conexion: {0}".format(ex))
        return lista

    #insercion
    def registrarPropiedad(self, propiedad):
        if self.inmobiliaria.is_connected():
            try:
                mycursor=self.inmobiliaria.cursor()
                sql = "insert into inmobiliaria.propiedad (direccionpropiedad, baños, serviciosluz, servicioagua, cochera, mt2, dormitorios, valorpropiedad, propietario_idpropietario) values ('{0}', {1}, {2}, {3}, {4}, {5}, {6}, {7});"
                mycursor.execute(sql.format(propiedad[0], propiedad[1], propiedad[2], propiedad[3], propiedad[4], propiedad[5], propiedad[6], propiedad[7]))
                self.inmobiliaria.commit()
               
                print("Propiedad Ingresado correctamente\n")
            except Error as ex:
                print("Error en conexion: {0}".format(ex))

    def elminarPropiedad(self, codigoEliminar):
        if self.inmobiliaria.is_connected():       
            try:
                mycursor=self.inmobiliaria.cursor()
                sql = "DELETE FROM inmobiliaria.propiedad WHERE idpropietario = {0};"
                mycursor.execute(sql.format(codigoEliminar))
                self.inmobiliaria.commit()
                print("Propiedad Eliminada correctamente\n")             
            except Error as ex:
                print("Error en conexion: {0}".format(ex))
            




    



