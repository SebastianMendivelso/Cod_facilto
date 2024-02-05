def nuevo_usuario():
    nombreusuario = (input("Ingrese su nombre completo\n"))
    apellidosusuario = (input("Ingrese sus apellidos de manera ordenada\n"))
    numerotel = (input("Ingrese su numero de telefono\n"))
    correousuario = (input("Ingrese su correo electronico\n"))
    
    print(f"\nHola {nombreusuario} {apellidosusuario}, en breve te llegara un correo a {correousuario}")
nuevo_usuario()