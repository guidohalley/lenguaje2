import conexionbd
from datetime import date, datetime


#                                                                      PROPIETARIO


def listarpropietario(propietario):
  
  for propiet in propietario:
    datos  =  "|[{0}]--[{1}]--[{2}]--[{3}]--[{4}]--[{5}]|"
    #idpropietario, nombre, apellido, direccion, telefono, email
    print(datos.format(propiet[0], propiet[1], propiet[2], propiet[3], propiet[4], propiet[5]))


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
  
  '''
  nombre =  input("Nombre del Propietario ? ")
  apellido  =  input("Apellido del Propietario ? ")
  direccion =  input("Direccion del Propietario? ")
  telefono  =  float(input("telefono del propietario? "))  
  emailPropietario = input("email del propietario?")  
  propietario  =  (nombre, apellido, direccion, telefono, emailPropietario)
  return propietario

#                                       PROPIEDADES
def listarpropiedades(propiedades):
  
  for prop in propiedades:
    datos  =  "[{0}]--[{1}]--[{2}]--[{3}]--[{4}]--[{5}]--[{6}]--[{7}]--[{8}]--[{9}]"
    #direccionpropiedad, baños, serviciosluz, servicioagua, cochera, mt2, dormitorios, valorpropiedad, propietario_idpropietario
    print(datos.format(prop[0], prop[1], prop[2], prop[3], prop[4], prop[5], prop[6], prop[7],prop[8],prop[9]))
    
    
def pedirDatosPropiedad():  
  
  direccionpropiedad  =  input("Ingrese la direccion de la propiedad: ")
  banios  =  input("ingrese la cantidad de banios: ")
  serviciosluz =  input("tiene servicio de luz? : ")
  servicioagua  =  input("Tiene servicio agua ? : ")  
  cochera =  int(input("ingrese mt2 de cochera: "))  
  mt2 = int(input("ingrese los mt2: "))
  dormitorios = int(input("ingrese la cantidad de dormitorios: "))
  valorpropiedad  =  float(input("ingrese el valor de la propiedad: "))
  propietario_idpropietario = int(input("Ingrese un numero"))  
  propiedad  =  (direccionpropiedad, banios, serviciosluz, servicioagua, cochera, mt2, dormitorios, valorpropiedad,propietario_idpropietario)
  return propiedad




def DatosEliminarPropiedad(propiedad):     
    listarprop(propiedad)  
    existeCodigo = False
    codigoEliminar = input("Ingrese el codigo del propietario que quiere  a eliminar> ")

    #buscamos si esta codigo eliminar en el listado de propiedades y si lo encuentra lo llevamos al menu

    for prop in propiedad:
          
      if prop[0] == codigoEliminar:              
        existeCodigo = True
        break    
      
    if not existeCodigo:
      codigoEliminar = " "
      
    return codigoEliminar
    

# ALQUILERES

def listaralquileres(alquileres):
  
  for alqui in alquileres:
    datos  =  "|[{0}]--[{1}]--[{2}]--[{3}]--[{4}]--[{5}]|"
    #idpropietario, nombre, apellido, direccion, telefono, email
    print(datos.format(alqui[0], alqui[1], alqui[2], alqui[3], alqui[4], alqui[5]))


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
  
  '''
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


 
# CLIENTE

def listarclientes(clientes):
  
  for cli in clientes:
    datos = "|[{0}],[{2}],[{3}],[{4}],[{5}]]|"
    print(datos.format(cli[0], cli[1], cli[2], cli[3], cli[4], cli[5]))


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
  
  '''
  nombreCli =  input("Nombre del Cliente? ")
  apellidoCli  =  input("Apellido del Cliente ? ")
  direccionCli =  input("Direccion del Cliente? ")
  telefonoCli  =  float(input("telefono del cliente? "))  
  garante = input("nombre del garante> ")
  Calquiler_idalquiler = int(input("ingrese el id del alquiler> ")) 
  cliente =  (nombreCli, apellidoCli, direccionCli, telefonoCli, garante,Calquiler_idalquiler)
  return cliente