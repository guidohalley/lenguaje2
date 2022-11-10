import conexionbd

def listarprop(propiedades):
  
  for prop in propiedades:
    datos  =  "[{0}][{1}][{2}][{3}][{4}][{5}][{6}][{7}][{8}][{9}]"
    #direccionpropiedad, baños, serviciosluz, servicioagua, cochera, mt2, dormitorios, valorpropiedad, propietario_idpropietario
    print(datos.format(prop[0], prop[1], prop[2], prop[3], prop[4], prop[5], prop[6], prop[7],prop[8],prop[9]))
    

    
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
  
  '''
  
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




def DatosEliminarPropiedad(propis):     
  listarprop(propis)  
  
  existeCodigo = False
  codigoEliminar = input("Ingrese el codigo del propietario que quiere  a eliminar> ")

  for x in propis:    
    if x[9] == codigoEliminar:
      print("🤔")
      existeCodigo = True
      break    
    
  if not existeCodigo:
    codigoEliminar = " "
    
  return codigoEliminar



 


