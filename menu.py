#!/usr/bin/env python
# coding :-*-  UTF-8 -*-
from conexionbd import conexion
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
            print("""
                ████████████████████████████████████████████████████████████████████████████████████
                █▄─▀█▀─▄█▄─▄▄─█▄─▀█▄─▄█▄─██─▄███▄─▄▄─█▄─▄▄▀█▄─▄█▄─▀█▄─▄█─▄▄▄─█▄─▄█▄─▄▄─██▀▄─██▄─▄███
                ██─█▄█─███─▄█▀██─█▄▀─███─██─█████─▄▄▄██─▄─▄██─███─█▄▀─██─███▀██─███─▄▄▄██─▀─███─██▀█
                ▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀▀▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀
                """)

            print('---------Operaciones de Alta--------')
            print('  1- Ingresar Propietario')
            print('  2- Ingresar Propiedad')
            print('  3- Ingresar Alquiler')
            print('  4- Ingresar cliente\n\n')  
            print('---------Operaciones de Baja--------')
            print('  5- Eliminar Propietario')
            print('  6- Eliminar Propiedad')
            print('  7- Eliminar Alquiler')
            print('  8- Eliminar Cliente\n\n') 
            print('---------Operaciones de Modificacion--------')
            print('  9- Modificacion de Propietario')
            print(' 10- Modificar una Propiedad')
            print(' 11- Modificar un  Alquiler')
            print(' 12- Modificar un  cliente\n\n')
            print('---------Operaciones de Visualizacion de Datos--------')
            print(' 13- Ver todos los  Propietarios')
            print(' 14- Ver todas las propiedades')
            print(' 15- Ver todos los alquileres')
            print(' 16- Ver todos los clientes\n\n')            
            
            print('--------0-Salir--------')
            opcion =int(input('Seleccione una opcion : '))

            if opcion < 0 or opcion > 16:
                print('Opcion incorrecta, ingrese nuevamente')
            elif opcion == 0:
                continuar = False
                print('Gracias por utilizar el sistemas!!!')

                break
            else:
                opcionCorrecta=True 
                
def ejecutaropcion(opcion):
    conexion = conexion()
    if opcion == 1:
        #visualizacion
        try:
            propiedades = conexion.listarpropiedad()
            if len(propiedades) > 0:
                funciones.listarpropiedad(propiedades)
            else:
                print("no se encontraron registros")    
        except:
            print("Ocurrio un problema")
        
    elif opcion == 2:
        print("Eliminacion")
    elif opcion == 3:
        print("Actualizacion")
    elif opcion == 4:
        print("Visualizacion")
    else: 
        print ("Opcion no Valida")
        
        
menuprincipal()