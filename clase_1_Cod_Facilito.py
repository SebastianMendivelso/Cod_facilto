def nuevo_usuario():
    n=(int(input("Ingrese el numero de personas que desea ingresar dentro de el programa\n")))
    usuarios=[]
    for _ in range(n):
        nombreusuario = (input("Ingrese su nombre completo\n"))
        apellidosusuario = (input("Ingrese sus apellidos de manera ordenada\n"))
        numerotel = (input("Ingrese su numero de telefono\n"))
        correousuario = (input("Ingrese su correo electronico\n"))
        print("-"*60)
        dict={
            "nombre":nombreusuario,
            "apellidos":apellidosusuario,
            "Numero de telefono":numerotel, 
            "Correo de el usuario":correousuario
        }
        usuarios.append(dict)
    numero_persona = 1
    for dict in usuarios:
        print(f"\nPersona {numero_persona}:")
        for dato, ingreso in dict.items():
            print(f"{dato}:{ingreso}")
        numero_persona += 1
nuevo_usuario()