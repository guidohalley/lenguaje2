# coding :-*-  UTF-8 -*-

import os
import time
import conexionbd
from tabulate import tabulate


#                                      PROPIETARIO


def listarpropietario(propietario):
    

    os.system("cls")
    print(tabulate(propietario, headers=["ID","NOMBRE","APELLIO","DIRECCION","TELEFONO","EMAIL"],tablefmt='fancy_grid',stralign='center',floatfmt='.0f'))


def pedirDatosPropietario():
  
  '''
    Table: propietario
    Columns:
    {0} idpropietario int AI PK 
    {1} nombre varchar(45) 
    {2} apellido varchar(45) 
    {3} direccion varchar(45) 
    {4} telefono float 
    {5} email varchar(45)  
    #Tabla
  '''
  os.system("cls")
  nombre =  input("Nombre del Propietario ? ")
  apellido  =  input("Apellido del Propietario ? ")
  direccion =  input("Direccion del Propietario? ")
  telefono  =  float(input("telefono del propietario? "))  
  emailPropietario = input("email del propietario?")  
  
  propietario  =  (nombre, apellido, direccion, telefono, emailPropietario)
  
  return propietario


def datosEliminarPropietario(propietario):
  

    listarpropietario(propietario)  
    existeCodigo = False
    cPropietarioEliminiar = int(input("Ingrese el codigo del propietario que quiere  a eliminar> "))
    for propi in propietario:         
      
      if propi[0] == cPropietarioEliminiar:      
        
        existeCodigo = True       
        break    
      
    if not existeCodigo:
      cPropietarioEliminiar = " "
      
    return cPropietarioEliminiar
  
  
def datosActualizacionPropietario(propietario):
  
  listarpropietario(propietario)
  eCodigoPropietario = False
  APropietario = int(input("Ingrese el codigo del Propietario a actualizar> "))

  for propis in propietario:         
      
    if propis[0] == APropietario:      
        
        eCodigoPropietario = True       
        break    
      
  if not eCodigoPropietario:
      APropietario = " "
      
  if eCodigoPropietario:
    
      nombre =  input("Nuevo Nombre del Propietario ? ")
      apellido  =  input("Nuevo Apellido del Propietario ? ")
      direccion =  input("Nuevo Direccion del Propietario? ")
      telefono  =  float(input("Nuevo telefono del propietario? "))  
      emailPropietario = input("Nuevo email del propietario?")  
      idpropietario = int(APropietario)
      nuevopropietario  =  (nombre, apellido, direccion, telefono, emailPropietario, idpropietario)
      
      return nuevopropietario

  else:
      propietario = None

      return propietario

#                                       PROPIEDADES
def listarpropiedades(propiedades):
  
  os.system("cls")
  print(tabulate(propiedades, headers=["ID","DIRECCION PROPIEDAD","BAÑOS","LUZ","AGUA","COCHERA","MT2","DORMITORIOS","VALOR PROPIEDAD", "ID DE PROPIETARIO"],tablefmt='fancy_grid',stralign='center',floatfmt='.0f'))
  # respuesta = input("\n\nPresione Enter para volver al menu principal...")
  # if respuesta == "":
  #     time.sleep(1)
  #     os.system("cls") 
      
      
def pedirDatosPropiedad():
  
  
  
  '''
  Table: propiedad
  Columns:
  idpropiedad int AI PK 
  direccionpropiedad varchar(45) 
  baños varchar(45) 
  serviciosluz varchar(45) 
  servicioagua varchar(45) 
  cochera varchar(45) 
  mt2 int 
  dormitorios int 
  valorpropiedad float 
  propietario_idpropietario int
  #Tabla

  '''   
  os.system("cls")
  direccionpropiedad  =  input("Ingrese la direccion de la propiedad: ")
  banios  =  input("ingrese la cantidad de banios: ")
  serviciosluz =  input("tiene servicio de luz? : ")
  servicioagua  =  input("Tiene servicio agua ? : ")  
  cochera =  int(input("ingrese mt2 de cochera: "))  
  mt2 = int(input("ingrese los mt2: "))
  dormitorios = int(input("ingrese la cantidad de dormitorios: "))
  valorpropiedad  =  float(input("ingrese el valor de la propiedad: "))
  propietario_idpropietario = int(input("Ingrese id de propietario"))
  apellidopropeitario = ("Ingrese el apellido del propietario") 
  propiedad  =  (direccionpropiedad, banios, serviciosluz, servicioagua, cochera, mt2, dormitorios, valorpropiedad,propietario_idpropietario)
  
  return propiedad


def datosEliminarPropiedad(propiedad):
  
    listarpropiedades(propiedad)  
    existeCodigo = False
    codigoEliminar = int(input("Ingrese el codigo del propietario que quiere  a eliminar> "))
    #buscamos si esta codigo eliminar en el listado de propiedades y si lo encuentra lo llevamos al menu
    for prop in propiedad:       
      
      if prop[0] == codigoEliminar:
        
        existeCodigo = True        
        break    
      
    if not existeCodigo:
      
      codigoEliminar = " "
            
    return codigoEliminar
  
def datosActualizacionPropiedad(propis):
  
  os.system("cls") 
  listarpropiedades(propis)  
   
  eCodigoPropiedad = False
  
  cAPropiedad= int(input("ingrese el codigo de Propiedad a actualizar> "))

  for pro in propis:         
      
    if pro[0] == cAPropiedad:      
        
      eCodigoPropiedad = True       
      break    
      
  if not eCodigoPropiedad:
    cAPropiedad = " "
      
  if eCodigoPropiedad:    
    
    #apellidopropeitario = ("Ingrese el apellido del propietario")
    direccionpropiedad  =  input("Ingrese la nueva direccion de la propiedad: ")
    banios  =  input("ingrese la nueva cantidad de banios: ")
    serviciosluz =  input("Ahora tiene servicio de luz? : ")
    servicioagua  =  input("Ahora Tiene servicio agua ? : ")  
    cochera =  int(input("Vuelva ingrese mt2 de cochera: "))  
    mt2 = int(input("Vuelva ingresar los mt2: "))
    dormitorios = int(input("Vuelva a ingresar la cantidad de dormitorios: "))
    valorpropiedad  =  float(input("Vuelva ingresar el valor de la propiedad: "))
    propietario_idpropietario = int(input("Ingrese id de propietario"))
    idPropiedad = int(cAPropiedad) 
    nuevapropiedad  =  (direccionpropiedad, banios, serviciosluz, servicioagua, cochera, mt2, dormitorios, valorpropiedad,propietario_idpropietario,idPropiedad)
   
    return nuevapropiedad
  else:
      nuevapropiedad = None

      return nuevapropiedad 
    
#                                         ALQUILERES
def listaralquileres(alquileres):
  
    os.system("cls")
    print(tabulate(alquileres, headers=["ID","INICIO EN FECHA","TERMINA EN FECHA","ALQUILADO POR","MONTO","ID PROPIETARIO"],tablefmt='fancy_grid',stralign='center',floatfmt='.0f'))

  #for alqui in alquileres:
    
    # #datos  =  "||_[{0}]|____________|[{1}]|____________|[{2}]|____________|[{3}]|____________|[{4}]|____________|[{5}]|"
    # #idpropietario, nombre, apellido, direccion, telefono, email
    # #print(datos.format(alqui[0], alqui[1], alqui[2], alqui[3], alqui[4], alqui[5]))
    # json ="{0},{1},{2},{3},{4},{5},{6}"
    # print(json)
    

def pedirDatosAlquileres():
  
  '''
    Table: alquiler
    Columns:
    {0} idalquiler int AI PK 
    {1} fechaconini date 
    {2} fechaconfin date 
    {3} empleadoinmo varchar(45) 
    {4} montoalquiler double 
    {5} propiedad_idpropiedad int 
    #Tabla
  '''
  os.system("cls")
  anContrato = int(input("Ingrese Año Inicial del contrato de alquiler: "))
  meContrato = int(input("Ingrese Mes Inicial del contrato de alquiler"))
  dContrato = int(input("Ingrese día Inicial del contrato de alquiler"))
  fechaconini =  date(anContrato,meContrato,dContrato)
  print("la fecha del contrato inicial es> ", fechaconini)
  
  anContratof = int(input("Ingrese Año final del contrato de alquiler: "))
  meContratof = int(input("Ingrese Mes final del contrato de alquiler"))
  dContratof = int(input("Ingrese día final del contrato de alquiler"))
  fechaconfin =  date(anContratof,meContratof,dContratof)
  print("la fecha ingresada es> ", fechaconfin)
  
  empleadoinmo =  input("Ingrese el empleado de la Inmobiliaria> ")
  montoalquile =  float(input("Ingrese el Valor del Alquiler"))  
  propiedad_idpropiedad = int(input("Ingrese el Codigo de propiedad"))
    
  alquiler  =  (fechaconini, fechaconfin, empleadoinmo, montoalquile, propiedad_idpropiedad)
  
  return alquiler


def datosEliminarAlquiler(alquiler):
  
  existeCodAlquiler = False
  listaralquileres(alquiler)  
  cAlquilerEliminar = int(input("Ingrese el ID del alquiler que desea eliminar> "))
    
  for alqui in alquiler:
    
    if alqui[0] == cAlquilerEliminar:
      
      existeCodAlquiler = True
      
  if not existeCodAlquiler:
    
    cAlquilerEliminar = " "    
    
  return cAlquilerEliminar



def datosActualizacionAlquileres(alquiler):
  
  listaralquileres(alquiler)  
  eCodigoAlquier = False
  
  AAlquiler = int(input("ingrese el Codiog de Alquiler a actualizar> "))

  for act in alquiler:         
      
    if act[0] == AAlquiler:      
        
      eCodigoAlquier = True       
      break    
      
  if not eCodigoAlquier:
    AAlquiler = " "
      
  if eCodigoAlquier:
    
    anContrato = int(input("Ingrese Nuevo Año Inicial del contrato de alquiler: "))
    meContrato = int(input("Ingrese Nuevo Mes Inicial del contrato de alquiler"))
    dContrato = int(input("Ingrese Nuevo día Inicial del contrato de alquiler"))
    fechaconini =  date(anContrato,meContrato,dContrato)
    print("la fecha del contrato inicial es> ", fechaconini)
    
    anContratof = int(input("Ingrese Nuevo Año final del contrato de alquiler: "))
    meContratof = int(input("Ingrese Nuevo Mes final del contrato de alquiler"))
    dContratof = int(input("Ingrese Nuevo día final del contrato de alquiler"))
    fechaconfin =  date(anContratof,meContratof,dContratof)
    print("la fecha ingresada es> ", fechaconfin)
    
    
    empleadoinmo =  input("Ingrese Nuevo el empleado de la Inmobiliaria> ")
    montoalquile =  float(input("Ingrese Nuevo el Valor del Alquiler"))  
    propiedad_idpropiedad = int(input("Ingrese Nuevo el Codigo de propiedad"))
    idalquiler=int(AAlquiler)  
    nuevoalquiler  =  (fechaconini, fechaconfin, empleadoinmo, montoalquile, propiedad_idpropiedad,idalquiler)
                      #  '{0}','{1}','{2}',{3},'{4}','{5}'
                      #   nuevoalquiler[0],nuevoalquiler[1],nuevoalquiler[2],nuevoalquiler[3],nuevoalquiler[4],nuevoalquiler[5]
    print(nuevoalquiler)
    return nuevoalquiler

  else:
      propietario = None

      return propietario
    
    
    

#                                          CLIENTE

def listarclientes(clientes):  
  
    os.system("cls")
    print(tabulate(clientes, headers=["ID","NOMBRE","APELLIO","DIRECCION","MONTO","ASIGNADO","ID ALQUILER"],tablefmt='fancy_grid',stralign='center',floatfmt='.0f'))
        
    # for cli in clientes:      
    #   datos  = [[cli[0], cli[1], cli[2], cli[3], cli[4], cli[5]]]   
    
    # respuesta = input("\n\nPresione Enter para volver al menu principal...")
    # if respuesta == "":
    #     time.sleep(1)    
    
      
      
    
      

    
def pedirDatosClientes():
  
  '''
  Table: cliente
  Columns:
  idcliente int AI PK 
  nombre varchar(45) 
  apellido varchar(45) 
  direccion varchar(45) 
  telefono int 
  nombregarante varchar(45) 
  alquiler_idalquiler int
  
  #Tabla
  '''
  nombreCli =  input("Nombre del Cliente? ")
  apellidoCli  =  input("Apellido del Cliente ? ")
  direccionCli =  input("Direccion del Cliente? ")
  telefonoCli  =  float(input("telefono del cliente? "))  
  garante = input("nombre del garante> ")
  Calquiler_idalquiler = int(input("ingrese el id del alquiler> "))
   
  cliente =  (nombreCli, apellidoCli, direccionCli, telefonoCli, garante,Calquiler_idalquiler)
  
  return cliente

def datosEliminarCliente(cliente):
  
  existeCodCliente = False  
  listarclientes(cliente)  
  cClienteEliminar = int(input("Ingrese el ID del cliente que desea eliminar> "))
   
  for clien in cliente:  
      
    if clien[0] == cClienteEliminar:
      
      existeCodCliente = True            
      break
      
  if not existeCodCliente:
    
      cClienteEliminar = " "  

  return cClienteEliminar

def datosActualizacionCliente(cliente):
  
  os.system("cls")
  listarclientes(cliente)  
  eCodigoCliente = False
  
  ACliente= int(input("ingrese el Codiog de Cliente a actualizar> "))

  for client in cliente:         
      
    if client[0] == ACliente:      
        
      eCodigoCliente = True       
      break    
      
  if not eCodigoCliente:
    ACliente = " "
      
  if eCodigoCliente:
    
    nombreCli =  input("Nuevo Nombre del Cliente? ")
    apellidoCli  =  input("Nuevo Apellido del Cliente ? ")
    direccionCli =  input("Nuevo Direccion del Cliente? ")
    telefonoCli  =  float(input("telefono del cliente? "))  
    garante = input("Nuevo Nombre del garante> ")
    Calquiler_idalquiler = int(input("ingrese el id del alquiler> "))
    idcliente = int(ACliente)
    nuevocliente =  (nombreCli, apellidoCli, direccionCli, telefonoCli, garante, Calquiler_idalquiler, idcliente)
                    #'{0}',        '{1}',       '{2}',        {3},      '{4}',          {5},            '{6}'
                    #nuevocliente[0], nuevocliente[1], nuevocliente[2], nuevocliente[3], nuevocliente[4], nuevocliente[5], nuevocliente[6]     
    return nuevocliente