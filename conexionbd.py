#!/usr/bin/env python
# coding :-*-  UTF-8 -*-

import mysql.connector
from mysql.connector import Error

# en la pc de escritorio no hay contraseña
# en la laptop la contraseña es incade

class conexion:    
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
            
    def listarpropiedad(self):
        
        if self.inmobiliaria.is_connected():
            try:
                mycursor = self.inmobiliaria.cursor()
                mycursor.execute("SELECT * FROM inmobiliaria.propiedad;")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)                
            except Error as ex:
                print("Error en conexion: {0}".format(ex))
        
    def listarcliente(self):
        
        if self.inmobiliaria.is_connected():
            try:
                mycursor = self.inmobiliaria.cursor()
                mycursor.execute("SELECT * FROM inmobiliaria.cliente;")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)                
            except Error as ex:
                print("Error en conexion: {0}".format(ex))       
        
    def listarpropietario(self):
        
        if self.inmobiliaria.is_connected():
            try:
                mycursor = self.inmobiliaria.cursor()
                mycursor.execute("SELECT * FROM inmobiliaria.propietario;")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)                
            except Error as ex:
                print("Error en conexion: {0}".format(ex))       
          
                       
    def listaralquiler(self):
        
        if self.inmobiliaria.is_connected():
            try:
                mycursor = self.inmobiliaria.cursor()
                mycursor.execute("SELECT * FROM inmobiliaria.alquiler;")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)                
            except Error as ex:
                print("Error en conexion: {0}".format(ex))              
        
    
    

    



