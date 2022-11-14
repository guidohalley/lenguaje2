#!/usr/bin/env python
# coding :-*-  UTF-8 -*-
import os
import time

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
            print("1 - Ver ")
            print("2 - Insertar ")
            print("3 - Eliminar ")
            #print(" 4- Actualizar una Propiedad") 
            
            print("---------Operaciones de Propietario--------")
            print("5 - Ver ")
            print("6 - Insertar ")
            print("7 - Eliminar ")
            print("8 - Actualizar Propietario")
            
            print("---------Operaciones de Alquiler--------")
            print("9 - Ver")
            print("10- Insertar ")            
            print("11- Eliminar ")
            # print("  12- Actualizar Propietario")
            
            print("---------Operaciones de Cliente--------")
            print(" 13- Ver")
            print(" 14- Insertar ")            
            print(" 15- Eliminar ")
            # print("  16- Actualizar Propietario")
            print(" ________________________________________")        
            print("|_______________ 0 - Salir_______________|")
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
    if opcion ==   1:       #Listar
              
        try:
            propiedades = conexion.listarPropiedades() 
            if len(propiedades) > 0:
                funciones.listarpropiedades(propiedades) 
            else:
                print("no se encontraron registros")
        except:            
            print("Ocurrio un problema")
                 
    elif opcion == 2:       #Registrar Propiedades
              
        #viene de funciones
        propiedades = funciones.pedirDatosPropiedad()        
        try:            
            print('🚩')
            conexion.registrarPropiedad(propiedades)
        except:
            print("Ocurrio un problema")
            
                          
    elif opcion == 3:       #Eliminar Propieades     
        
        try:            
            
            propiedad = conexion.listarPropiedades()                          
            
            if len(propiedad) > 0:              
                
                codigoEliminar = funciones.datosEliminarPropiedad(propiedad) 
                
                if not(codigoEliminar == ' '):
                    conexion.elminarPropiedad(codigoEliminar)
                else:
                    print ("Codigo de propiedad inexistente")
        except:
            print(" Ocurrio un problema")
            
                             
    elif opcion == 4:       #Actualizar Propieades
        try:
          print(x)
        except:
          print('An exception occurred')
        
        
        
        try:
           print("Proyecto no listo")
        except:
            print("A ocurrido un problema")

#                     PROPIETARIO            
    elif opcion == 5:   #Listar Propietarios
       
        try:
            propietario = conexion.listarPropietarios() 
            if len(propietario) > 0:
                funciones.listarpropietario(propietario) 
            else:
                print("no se encontraron registros")
        except:            
            print("🤔Ocurrio un problema")   
            
            
                                      
    elif opcion == 6:    #Registrar Propietarios    

        propietario = funciones.pedirDatosPropietario() 
        try:
            
            conexion.registrarPropietario(propietario)
        except:
            print("Ocurrio un problema") 
            
            
                 
    elif opcion == 7:   #Eliminar Propietario
        
        try:            

            propietario= conexion.listarPropietarios()

            if len(propietario) > 0: 

                cPropietarioEliminiar = funciones.datosEliminarPropietario(propietario) # es para pedir los datos que tenemos que eliminar.
                if not(cPropietarioEliminiar == ' '):
                    
                    conexion.elminarPropietario(cPropietarioEliminiar)                    
                else:
                    
                    print ("Codigo de propietario inexistente")
        except:
            
            print("Ocurrio un problema")    
            
                    
    elif opcion == 8: #Actualizar Propietario  
        try:          
            
            propietario = conexion.listarPropietarios()                          
            
            if len(propietario) > 0:              
                
                cAPropietario = funciones.datosActualizacionPropietario(propietario)
                print(cAPropietario)
                
                if cAPropietario :
                    print("pasando if")
                    
                    conexion.actualizarPropietario(cAPropietario)
                     
                else:
                    print ("Codigo de propietario inexistente")
        except:
            print(" Menu> Ocurrio un problema ")


#                     ALQUILERES
    elif opcion == 9:   #Mostrar  Alquileres
        os.system("cls")
        try:
            alquileres = conexion.listarAlquileres() 
            if len(alquileres) > 0:
                funciones.listaralquileres(alquileres) 
            else:
                print("no se encontraron registros")
        except:            
            print("Ocurrio un problema")
            
               
    elif opcion == 10:  #Registrar Alquileres11
        
        alquileres = funciones.pedirDatosAlquileres()        
        try:            
            conexion.registrarAlquileres(alquileres)
            print('🚩menu')
        except:
            print("Ocurrio un problema volviendo al menu")
            time.sleep(5)
            
    elif opcion == 11:  #Eliminar  Alquileres
        try:
          alquiler = conexion.listarAlquileres()
          if len(alquiler) > 0:
              
            cAlquilerEliminar = funciones.datosEliminarAlquiler(alquiler)
              
            if not(cAlquilerEliminar == ' '):
                  conexion.eliminarAlquileres(cAlquilerEliminar)
            else:
                print(" el codigo de Alquiler no fue encontrado...")
        except:
          print('Ha ocurrido un problema')
    
    
    elif opcion == 12:  #Actualizar Alquileres
        try:
          print(x)
        except:
          print('An exception occurred')
        
#                     CLIENTE
    elif opcion == 13:  #Mostrar Clientes
        
        try:
            clientes = conexion.listarClientes()
            if len(clientes) > 0:
                
                funciones.listarclientes(clientes)              
            else:
                
              print("Ocurrio un problema ...")
        except:
            
          print('An exception occurred')
          
                    
    elif opcion == 14:  #Registrar Clientes
        
        clientes = funciones.pedirDatosClientes()
        try:
            
            conexion.registrarClientes(clientes)
            
        except:
            
          print('Ocurrio un Problema...')  
              
    elif opcion == 15:  #Eliminar Clientes
        
        try:
            
            cliente  = conexion.listarClientes()
            if len(cliente) > 0:
                
                cClienteEliminar = funciones.datosEliminarCliente(cliente)
                if not(cClienteEliminar == ' '): 
                                       
                    
                    conexion.eliminarClientes(cClienteEliminar)
                else:
                    
                    print("el Codigo de Cliente no fue encontrado.. \n")                    
        except:
            
          print('Ha ocurrido un problema')
    elif opcion == 16:  #Actualizar Clientes
        try:
          print(x)
        except:
          print('An exception occurred')
          
          
          
    
    else: 
        print ("Opcion no Valida")
        
        
time.sleep(2)              
menuprincipal()
