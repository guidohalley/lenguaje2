import conexionbd

def listarpropiedad(propiedades):

  
  for prop in propiedades:
    datos  =  "[{0}][{1}][{2}][{3}][{4}][{5}][{6}][{7}]"
    #direccionpropiedad, baños, serviciosluz, servicioagua, cochera, mt2, dormitorios, valorpropiedad, propietario_idpropietario
    print(datos.format(prop[0],"--\t",prop[1],"--\t",prop[2],"--\t",prop[3],"--\t",prop[4],"--\t",prop[5],"--\t",prop[6],"--\t",prop[7],"|"))
    c  =  c+1
    print (" ")

    
def pedirDatosPropiedad():

  print ("Entre a pedir datos")
  direccionpropiedad  =  input("Ingrese la direccion de la propiedad: ")

  banios  =  input("ingrese la cantidad de banios: ")

  serviciosluz =  input("tiene servicio de luz? : ")

  servicioagua  =  input("Tiene servicio agua ? : ")

  cochera =  int(input("ingrese mt2 de cochera: "))

  mt2 = int(input("ingrese la cantidad de banios: "))

  dormitorios = int(input("ingrese la cantidad de dormitorios: "))

  valorpropiedad  =  float(input("ingrese el valor de la propiedad: "))

  #propietario_idpropietario = input("ingrese el numero de propietario: ")
 
  propiedad  =  (direccionpropiedad, banios, serviciosluz, servicioagua, cochera, mt2, dormitorios, valorpropiedad)
  return propiedad

def DatosEliminarPropiedad(self, propiedades):
  
  print("entre aca en funciones")
  listarpropiedad() 
  codigoEliminar = input("Ingrese el codigo de la propiedad a eliminar")
  existeCodigo = False

  for listp in listarpropiedad:    
    if listp[0] == codigoEliminar:
      existeCodigo = True
      break
    
  if not existeCodigo:
    codigoEliminar = ""
    
  return codigoEliminar



 


