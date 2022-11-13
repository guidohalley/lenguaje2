#!/usr/bin/env python
# coding :-*-  UTF-8 -*-
import os

import funciones
from conexionbd import Conexion

os.system("cls")
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
     

            print("---------Operaciones de Propiedad--------")
            print(" 1- Ver ")
            print(" 2- Insertar ")
            #print(" 3- Eliminar Propiedad")
            #print(" 4- Actualizar una Propiedad") 
            
            print("---------Operaciones de Propietario--------")
            print(" 5- Ver ")
            print(" 6- Insertar ")
            # print("  7- Eliminar Propietario")
            # print("  8- Actualizar Propietario")
            
            print("---------Operaciones de Alquiler--------")
            print(" 9- Ver")
            print(" 10- Insertar ")            
            # print("  11- Eliminar Propietario")
            # print("  12- Actualizar Propietario")
            
            print("---------Operaciones de Cliente--------")
            print(" 31- Ver")
            print(" 14- Insertar ")            
            # print("  11- Eliminar Propietario")
            # print("  12- Actualizar Propietario")
                       
            print("--------0-Salir--------")
            opcion = int(input("Seleccione una opcion : "))

            if opcion < 0 or opcion > 16:
                print("Opcion incorrecta, ingrese nuevamente")
                
            elif opcion == 0:
                continuar = False
                print("Sistema Cerrado")
                break
            else:
                opcionCorrecta=True
                ejecutaropcion(opcion)
                
def ejecutaropcion(opcion):

    conexion = Conexion()
#                     PROPIEDADES     
    if opcion == 1: #Listar
        #print('🚩')        
        try:
            propiedades = conexion.listarPropiedades() #🔵 va a conexionesbd
            if len(propiedades) > 0:
                funciones.listarpropiedades(propiedades) #🟢 va a funciones
            else:
                print("no se encontraron registros")
        except:            
            print("Ocurrio un problema")     
    elif opcion == 2:  #Registrar Propiedades
              
        #propiedad = conexion.elminarPropiedad()
        #este viene de funciones
        propiedades = funciones.pedirDatosPropiedad()        
        try:            
            print('🚩')
            conexion.registrarPropiedad(propiedades)
        except:
            print("Ocurrio un problema")              
    elif opcion == 3:   #Eliminar Propieades     
        try:
            propiedad = conexion.listarPropiedades()
            
            if len(propiedad) > 0:
                codigoEliminar = funciones.DatosEliminarPropiedad(propiedad)
                
                if (codigoEliminar == " "):                      
                    conexion.elminarPropiedad(codigoEliminar)                  
                else:
                    print("No se encontro el codigo de propiedad")
                    
        except:
            print("👽 No entro al if")               
    elif opcion == 4:#Actualizar Propieades
        
        
        
        
        try:
           print("Proyecto no listo")
        except:
            print("A ocurrido un problema")

#                     PROPIETARIO            
    elif opcion == 5:#Listar Propietarios
        #print('🚩')        
        try:
            propietarios = conexion.listarPropietarios() #🔵 va a conexionesbd
            if len(propietarios) > 0:
                funciones.listarprop(propietarios) #🟢 va a funciones
            else:
                print("no se encontraron registros")
        except:            
            print("Ocurrio un problema")                             
    elif opcion == 6:  #Registrar Propietario      

        propietario = funciones.pedirDatosPropietario()#va a funciones    
        try:
            print("🚩menu") 
            conexion.registrarPropietario(propietario)# aca va a la conexion
        except:
            print("Ocurrio un problema")      
    elif opcion == 7:  #Eliminar Propietario      

        propietario = funciones.pedirDatosPropietario()#va a funciones    
        try:
            print("🚩menu") 
            conexion.registrarPropietario(propietario)# aca va a la conexion
        except:
            print("Ocurrio un problema")            
    elif opcion == 8:  #Actualizar Propietario  
        try:
          print(x)
        except:
          print('An exception occurred')


#                     ALQUILERES
    elif opcion == 9:  #Mostrar  Alquileres
        #print('🚩')        
        try:
            alquileres = conexion.listarAlquileres() #🔵 va a conexionesbd
            if len(alquileres) > 0:
                funciones.listaralquileres(alquileres) #🟢 va a funciones
            else:
                print("no se encontraron registros")
        except:            
            print("Ocurrio un problema")   
    elif opcion == 10:  #Registrar Alquileres
        alquileres = funciones.pedirDatosAlquileres()        
        try:            
            conexion.registrarAlquileres(alquileres)
            print('🚩menu')
        except:
            print("Ocurrio un problema")
    elif opcion == 11:  #Eliminar  Alquileres
        try:
          print(x)
        except:
          print('An exception occurred')
    elif opcion == 12:  #Actualizar Alquileres
        try:
          print(x)
        except:
          print('An exception occurred')
        
#                     CLIENTE
    elif opcion == 11:  #Mostrar Clientes
        try:
          print(x)
        except:
          print('An exception occurred')
    elif opcion == 12:  #Registrar Clientes
        try:
          print(x)
        except:
          print('An exception occurred')
          
    elif opcion == 13:  #Eliminar Clientes
        try:
          print("No funciona >:(")
        except:
          print('An exception occurred')
    elif opcion == 14:  #Actualizar Clientes
        try:
          print(x)
        except:
          print('An exception occurred')
    else: 
        print ("Opcion no Valida")
               
menuprincipal() 