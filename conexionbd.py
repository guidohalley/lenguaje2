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
        
            if self.inmobiliaria.is_connected():
                
                try:
                    mycursor = self.inmobiliaria.cursor()
                    mycursor.execute("SELECT * FROM inmobiliaria.propietario;")
                    lista = mycursor.fetchall()                
                    # for x in lista:
                    #     print(x) 
                except Error as ex:
                    
                    print("Error en conexion: {0}".format(ex)) 
                                   
            return lista

    def registrarPropietario(self, propietario):       
        
        if self.inmobiliaria.is_connected():
            
            try:
                
                mycursor=self.inmobiliaria.cursor()               
                #siempre fijarse bien aca que los enteros esten sin '' y los varchar entre ''
                sql = "insert into propietario (nombre, apellido, direccion, telefono, email) values ('{0}','{1}', '{2}', {3}, '{4}');"
                mycursor.execute(sql.format(propietario[0],propietario[1], propietario[2], propietario[3], propietario[4]))
                self.inmobiliaria.commit()
            except Error as ex:
                
                print("Error en conexion: {0}".format(ex))
                
                
    def elminarPropietario(self, cPropietarioEliminiar):
           
        if self.inmobiliaria.is_connected():
            try:        
                                
                mycursor=self.inmobiliaria.cursor()
                sql = "DELETE FROM propietario WHERE idpropietario = '{0}'; "
                mycursor.execute(sql.format(cPropietarioEliminiar)) 
                self.inmobiliaria.commit()               
                
            except Error as ex: 
                               
                print("Error en conexion: {0}".format(ex))
                
    def actualizarPropietario(self, cAPropietario):        

        if self.inmobiliaria.is_connected():               
            
            try:
                
                mycursor=self.inmobiliaria.cursor()               
                #siempre fijarse bien aca que los enteros esten sin '' y los varchar entre ''
                sql = "UPDATE inmobiliaria.propietario SET nombre = '{0}', apellido = '{1}', direccion = '{2}', telefono = {3}, email = '{4}' WHERE (idpropietario = '{5}');"
                mycursor.execute(sql.format(cAPropietario[0],cAPropietario[1], cAPropietario[2], cAPropietario[3], cAPropietario[4], cAPropietario[5]))
                self.inmobiliaria.commit()
                print("Propietario Actualizado")
            except Error as ex:
                
                print("Error en conexion: {0}".format(ex))
    #                                                                           PROPIEDADES 
       
    def listarPropiedades(self):

        if self.inmobiliaria.is_connected():
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
                              
                print("Propiedad Ingresado correctamente\n")
                                
            except Error as ex:
                
                print("Error en conexion: {0}".format(ex))
                
                
    def elminarPropiedad(self, codigoEliminar):

        
        if self.inmobiliaria.is_connected():         
                
            try:               
                                
                mycursor=self.inmobiliaria.cursor()
                sql = "DELETE FROM propiedad WHERE idpropiedad = '{0}'; "              
                mycursor.execute(sql.format(codigoEliminar))              
                self.inmobiliaria.commit()
                # Error en conexion: 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`inmobiliaria`.`alquiler`, CONSTRAINT `fk_alquiler_propiedad1` FOREIGN KEY (`propiedad_idpropiedad`) REFERENCES `propiedad` (`idpropiedad`))
                # Funciona, pero primiero hay que borrar alquiler. 
            except Error as ex:
                                
                print("Error en conexion: {0}".format(ex))
                print("No se puede Eliminar una propiedad en Alquiler")
                time.sleep(5)
                os.system("cls") 
                
    def actualizarPropiedad(self, cAPropiedades):        

        if self.inmobiliaria.is_connected():               
            
            try:
                
                mycursor=self.inmobiliaria.cursor()               
                #siempre fijarse bien aca que los enteros esten sin '' y los varchar entre ''
                sql = "UPDATE inmobiliaria.propiedad SET direccionpropiedad = '{0}', baños = '{1}', serviciosluz = '{2}', servicioagua = '{3}', cochera = '{4}', mt2 = {5}, dormitorios = {6}, valorpropiedad = {7}, propietario_idpropietario = '{8}' WHERE (idpropiedad = '{9}');"
                
                mycursor.execute(sql.format(cAPropiedades[0],cAPropiedades[1], cAPropiedades[2], cAPropiedades[3], cAPropiedades[4], cAPropiedades[5], cAPropiedades[6], cAPropiedades[7], cAPropiedades[8], cAPropiedades[9]))
                self.inmobiliaria.commit()
                print("Propietario Actualizado")
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

            try:
                
                mycursor=self.inmobiliaria.cursor()
                print('🚩cursor')
                sql = "insert into alquiler (fechaconini, fechaconfin, empleadoinmo, montoalquiler, propiedad_idpropiedad) values ('{0}', '{1}', '{2}', {3}, {4});"
                mycursor.execute(sql.format(alquiler[0], alquiler[1], alquiler[2], alquiler[3], alquiler[4]))                
                self.inmobiliaria.commit() 
                print("Propiedad Ingresado correctamente\n")
                
            except Error as ex:
                
                print("Error en conexion: {0}".format(ex))
    
    def eliminarAlquileres(self,cAlquilerEliminar):
        
        if self.inmobiliaria.is_connected():            
            try:       
                        
                mycursor=self.inmobiliaria.cursor()
                sql="DELETE FROM alquiler WHERE idalquiler = {0}"
                mycursor.execute(sql.format(cAlquilerEliminar))
                self.inmobiliaria.commit()            
                
            except Error as ex:     
                           
                print("Error en conexion: {0}".format(ex))
                
                
    def actualizarAlquiler(self, cAAlquiler):        

            if self.inmobiliaria.is_connected():               
                
                try:
                    
                    mycursor=self.inmobiliaria.cursor()               
                    #siempre fijarse bien aca que los enteros esten sin '' y los varchar entre ''
                    sql ="UPDATE inmobiliaria.alquiler SET fechaconini = '{0}', fechaconfin = '{1}', empleadoinmo = '{2}', montoalquiler = '{3}', propiedad_idpropiedad = '{4}' WHERE (idalquiler = '{5}');" 
                    mycursor.execute(sql.format(cAAlquiler[0],cAAlquiler[1], cAAlquiler[2], cAAlquiler[3], cAAlquiler[4],cAAlquiler[5]))
                    self.inmobiliaria.commit()
                    print("Alquiler Actualizado")
                    
                except Error as ex:
                    
                    print("Error en conexion: {0}".format(ex)) 
                    print("A lo mejor debe borrar otra tabla primero")
                
#                                                                          CLIENTES
    def listarClientes(self):
        
        if self.inmobiliaria.is_connected():# vemos si esta conectado
            try:
                
                mycursor = self.inmobiliaria.cursor()
                mycursor.execute("SELECT * FROM inmobiliaria.cliente;")
                lista = mycursor.fetchall()                
                # for x in lista:
                #     print(x) 
                
            except Error as ex:
                print("Error en conexion: {0}".format(ex))                
        return lista

    def registrarClientes(self, cliente):
        
        if self.inmobiliaria.is_connected():
            try:
                
              mycursor=self.inmobiliaria.cursor()
              sql = "insert into cliente (nombre, apellido, direccion, telefono, nombregarante,alquiler_idalquiler) values ('{0}','{1}','{2}',{3},'{4}',{5})"
              mycursor.execute(sql.format(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4],cliente[5]))              
              self.inmobiliaria.commit()           
              
            except Error as ex:
                
                print("Error en conexion: {0}".format(ex))
              
              
    def eliminarClientes(self, cClienteEliminar):
        
        if self.inmobiliaria.is_connected():

            try:
                       
                mycursor=self.inmobiliaria.cursor()                
                sql="DELETE FROM cliente WHERE idcliente = {0}"
                mycursor.execute(sql.format(cClienteEliminar))
                self.inmobiliaria.commit()              
                
            except Error as ex:  
                              
                print("Error en conexion: {0}".format(ex))
                
    def actualizarCliente(self, cACliente):

        if self.inmobiliaria.is_connected():               
                
                try:

                    mycursor=self.inmobiliaria.cursor() 
                    sql ="UPDATE inmobiliaria.cliente SET nombre = '{0}', apellido = '{1}', direccion = '{2}', telefono = '{3}', nombregarante = '{4}', alquiler_idalquiler = '{5}' WHERE (idcliente = '{6}');" 
                    mycursor.execute(sql.format(cACliente[0],cACliente[1], cACliente[2], cACliente[3], cACliente[4],cACliente[5],cACliente[6]))
                    self.inmobiliaria.commit()  
                    print("Cliente Actualizado")
                    
                except Error as ex:                    
                    print("Error en conexion: {0}".format(ex)) 
                    print("No se Actualizo Cliente")
          
     