import conexionbd

def listarpropiedad(propiedades):
  print("Propiedades.. ")
  for prop in propiedades:
    datos = "{0}. Direccion: {1}"
    print(datos.format(c,prop[0],prop[1],prop[2]))
    c = c+1
 


