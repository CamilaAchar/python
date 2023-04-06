


def pedirDatosDeUsuario(): ##creé una función para pedir los datos de usuario y guardarlos en un diccionario 

  diccionario_datos_de_usuario = {} ##creo el diccionario dentro de la función

  diccionario_datos_de_usuario["USUARIOS"] = input( "Por favor ingresá tu usuario:\n" ) ##le asigno clave-valor 
  diccionario_datos_de_usuario["CONTRASEÑAS"] = input( "Por favor ingresá tu contraseña:\n" )

  doc_en_mydrive = open(ruta + "/Base de USUARIOS para entrega.txt", "a")
  doc_en_mydrive.write("USUARIO:" + diccionario_datos_de_usuario["USUARIOS"] + "\n" + "CONTRASEÑA:"+ diccionario_datos_de_usuario["CONTRASEÑAS"] + "\n" + "____________" + "\n")

  doc_en_mydrive.close() 

  return diccionario_datos_de_usuario

  lista_de_usuarios=[]
for i in range(3): ##VER COMO HACER PARA QUE SEA INFINITO, PARA CADA VEZ QUE ALGUIWN ESCRIBE ALGO 
  lista_de_usuarios.append(pedirDatosDeUsuario()) ##VER SI DESDE ACÁ PUEDO LLAMAR A LOS OBJETISO DEL DIC C
print(lista_de_usuarios)