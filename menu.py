#!/usr/bin/env python
# coding :-*-  UTF-8 -*-
import os
from conexionbd import Conexion
import funciones

 
print(" _                                                _            ___   ___    ") 
print(" | |       ___   _ __     __ _   _   _    __ _    (_)   ___    |_ _| |_ _|  ")  
print(" | |      / _ \ | '_ \   / _` | | | | |  / _` |   | |  / _ \    | |   | |   ")  
print(" | |___  |  __/ | | | | | (_| | | |_| | | (_| |   | | |  __/    | |   | |   ")  
print(" |_____|  \___| |_| |_|  \__, |  \__,_|  \__,_|  _/ |  \___|   |___| |___|  ")  
print("                         |___/                  |__/                        ")   

print("  _   _           _   _                     ____           _       _         ")
print(" | | | |   __ _  | | | |   ___   _   _     / ___|  _   _  (_)   __| |   ___  ")
print(" | |_| |  / _` | | | | |  / _ \ | | | |   | |  _  | | | | | |  / _` |  / _ \ ")
print(" |  _  | | (_| | | | | | |  __/ | |_| |   | |_| | | |_| | | | | (_| | | (_) |")
print(" |_| |_|  \__,_| |_| |_|  \___|  \__, |    \____|  \__,_| |_|  \__,_|  \___/ ")
print("                                 |___/                                       ")

def menuprincipal():
    continuar = True
    while(continuar):
        
        opcionCorrecta=False
        
        while(not opcionCorrecta):          
            # print("""
            #     ████████████████████████████████████████████████████████████████████████████████████
            #     █▄─▀█▀─▄█▄─▄▄─█▄─▀█▄─▄█▄─██─▄███▄─▄▄─█▄─▄▄▀█▄─▄█▄─▀█▄─▄█─▄▄▄─█▄─▄█▄─▄▄─██▀▄─██▄─▄███
            #     ██─█▄█─███─▄█▀██─█▄▀─███─██─█████─▄▄▄██─▄─▄██─███─█▄▀─██─███▀██─███─▄▄▄██─▀─███─██▀█
            #     ▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀▀▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀
            #     """)

            print("---------Operaciones de Propiedad--------")
            print(" 1- Ver todas las propiedades")
            print(" 2- Ingresar Propiedad")
            print(" 3- Eliminar Propiedad")
            # print("  1- Ingresar Propietario")
            # print("  3- Ingresar Alquiler")
            # print("  4- Ingresar cliente\n\n")  
            
            # print("---------Operaciones de Baja--------")
            # print("  5- Eliminar Propietario")
            # print("  7- Eliminar Alquiler")
            # print("  8- Eliminar Cliente\n\n") 
            
            # print("---------Operaciones de Modificacion--------")
            # print("  9- Modificacion de Propietario")
            # print(" 10- Modificar una Propiedad")
            # print(" 11- Modificar un  Alquiler")
            # print(" 12- Modificar un  cliente\n\n")
            
            # print("---------Operaciones de Visualizacion de Datos--------")
            # print(" 13- Ver todos los  Propietarios")
            # print(" 15- Ver todos los alquileres")
            # print(" 16- Ver todos los clientes\n\n")
            
            
            print("--------0-Salir--------")
            opcion = int(input("Seleccione una opcion : "))            

            if opcion < 0 or opcion > 16:
                print("Opcion incorrecta, ingrese nuevamente")
                os.cls()
            elif opcion == 0:
                continuar = False
                print("Sistema Cerrado")

                break
            else:
                opcionCorrecta=True 
                ejecutaropcion(opcion)
                
def ejecutaropcion(opcion):

    conexion = Conexion()
    
    if opcion == 1:
        print("Visualizacion de Propiedades")
        try:
            propiedades = conexion.listarPropiedades()
            if len(propiedades) > 0:
                funciones.listarPropiedades(propiedades)                            
            else:
                print("no se encontraron registros")    
        except:
            print("Ocurrio un problema")
        
    elif opcion == 2:
        
        #este viene de funciones
        hola = funciones.pedirDatosPropiedad()
        print("Lleuge hasta aca ")
        try:
            #trae todo propiedad y inserta en conexionbd.py
            #NOSE POR QUE NO ANDA
            conexion.registrarPropiedad(hola)
        except:
            print("Ocurrio un problema")
            
    elif opcion == 3:
        try:
            propiedades = conexion.listarPropiedades()
            if len(propiedades) > 0:
                codigoEliminar = funciones.DatosEliminarPropiedad(propiedades)
                if not(codigoEliminar == ""):  
                    print("***LLEGUE ACA***")
                    conexion.elminarPropiedad(codigoEliminar)
                else:
                    print("No se encontro el codigo de propiedad")
                    menuprincipal()
        except:
            print("No entro al if")
    elif opcion == 4:
        print("Visualizacion")
    else: 
        print ("Opcion no Valida")
        menuprincipal()        
