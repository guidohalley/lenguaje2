#!/usr/bin/env python
# coding :-*-  UTF-8 -*-

import os
import time

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
                password = '',
                host = 'localhost',
                database = 'inmobiliaria',
                port = 3306
                
            )        
        except Error as ex:
            print("Error en conexion: {0}".format(ex))
#                                                                           PROPIETARIO
            
    def listarPropietarios(self):

            if self.inmobiliaria.is_connected():# vemos si esta conectado
                try:
                    mycursor = self.inmobiliaria.cursor()
                    mycursor.execute("SELECT * FROM inmobiliaria.propietario;")
                    lista = mycursor.fetchall()                
                    for x in lista:
                        print(x) 
                except Error as ex:
                    print("Error en conexion: {0}".format(ex))                
            return lista
        
    
    def registrarPropietario(self, propietario):       
        
        if self.inmobiliaria.is_connected():
            try:
                mycursor=self.inmobiliaria.cursor()
                print("🚩conexion")
                #siempre fijarse bien aca que los enteros esten sin '' y los varchar entre ''
                sql = "insert into propietario (nombre, apellido, direccion, telefono, email) values ('{0}','{1}', '{2}', {3}, '{4}');"
                mycursor.execute(sql.format(propietario[0],propietario[1], propietario[2], propietario[3], propietario[4]))
                print("🚩execute")
                self.inmobiliaria.commit()
                print('🚩 Propietario Registrado\n')             
                
            except Error as ex:
                print("Error en conexion: {0}".format(ex))

            
#                                                                           PROPIEDADES 
    # visualizacion       
    def listarPropiedades(self):

        if self.inmobiliaria.is_connected():# vemos si esta conectado
            try:
                mycursor = self.inmobiliaria.cursor()
                mycursor.execute("SELECT * FROM inmobiliaria.propiedad;")
                lista = mycursor.fetchall()                
                # for x in lista:
                #     print(x) 
            except Error as ex:
                print("Error en conexion: {0}".format(ex))                
        return lista

    
    def registrarPropiedad(self, propiedad):
        
        
        if self.inmobiliaria.is_connected():
            
            try:
                mycursor=self.inmobiliaria.cursor()
                
                sql = "insert into propiedad (direccionpropiedad, baños, serviciosluz, servicioagua, cochera, mt2, dormitorios, valorpropiedad, propietario_idpropietario) values ('{0}', '{1}', '{2}', '{3}', '{4}', {5}, {6}, {7},{8});"
                mycursor.execute(sql.format(propiedad[0], propiedad[1], propiedad[2], propiedad[3], propiedad[4], propiedad[5], propiedad[6], propiedad[7],propiedad[8]))
                self.inmobiliaria.commit()
                print('🚩 Propiedad Registrada')
               
                print("Propiedad Ingresado correctamente\n")
            except Error as ex:
                print("Error en conexion: {0}".format(ex))
                
                

    def elminarPropiedad(self, codigoEliminar):
        #trae codigo eliminar del menu y ...
        
        if self.inmobiliaria.is_connected():
            print("Hay conexion")   
                
            try:                
                mycursor=self.inmobiliaria.cursor()
                print("🤔tenemos cursor")
                #pongo la consulta dentro deuna var para poder darle format despues. 
                sql = "DELETE FROM propiedad WHERE idpropiedad = '{0}'; "
                print("🤔guardamos la consulta en sql")
                #la mando por aca  y en al consola supuestamente ya elimina. 
                mycursor.execute(sql.format(codigoEliminar))#execute(sql.format(codigoEliminar))
                print("🤔ejecutamos la consulta")
                self.inmobiliaria.commit()
                print("🤔mando el commit supuestamente")
                #una vez que pasa aca voy a la BD y todavia no hace la eliminacion . y controle muchisimas veces
                print("Propiedad Eliminada correctamente\n")
   
                         
            except Error as ex:
                
                print("Error en conexion: {0}".format(ex))   
  
  
#                                                                          ALQUILERES

    def listarAlquileres(self):

        if self.inmobiliaria.is_connected():# vemos si esta conectado
            try:
                mycursor = self.inmobiliaria.cursor()
                mycursor.execute("SELECT * FROM inmobiliaria.alquiler;")
                lista = mycursor.fetchall()                
                # for x in lista:
                #     print(x) 
            except Error as ex:
                print("Error en conexion: {0}".format(ex))                
        return lista

    
    def registrarAlquileres(self, alquiler):
        
        if self.inmobiliaria.is_connected():
            print('🚩conexion')
            try:
                mycursor=self.inmobiliaria.cursor()
                print('🚩cursor')
                sql = "insert into alquiler (fechaconini, fechaconfin, empleadoinmo, montoalquiler, propiedad_idpropiedad) values ('{0}', '{1}', '{2}', {3}, {4});"
                
                mycursor.execute(sql.format(alquiler[0], alquiler[1], alquiler[2], alquiler[3], alquiler[4]))                
                self.inmobiliaria.commit()         
              
               
                print("Propiedad Ingresado correctamente\n")
            except Error as ex:
                print("Error en conexion: {0}".format(ex))