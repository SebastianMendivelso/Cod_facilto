def imprimir_texto_centralizado(texto, ancho_consola=80):
    texto_centralizado = texto.center(ancho_consola)
    return texto_centralizado
personas=[]
def validar_entrada(mensaje, longitud_min, longitud_max=None):
    '''en esta funcion que coloco son para las validaciones, agrego coomo lo que es la longitud minima y lo que es la maxima,
    y ese none esta para que sea un valor por defecto'''
    while True:
        entrada = input(mensaje + "\n")
        if not entrada:
            print("Por favor, ingrese un valor.")
        if longitud_max is not None and not (longitud_min <= len(entrada) <= longitud_max):
            print(f"La entrada debe tener entre {longitud_min} y {longitud_max} caracteres.")
        return entrada
def new_user():
    n = int(input("Ingrese el numero de personas que desea ingresar dentro del programa:\n"))
    for i in range(1, n + 1):
        print(f"Ingresando los datos de la persona {i}:")
        nombreusuario = validar_entrada("Ingrese su nombre completo:", 5, 50)
        apellidosusuario = validar_entrada(f"Ingrese los apellidos de la persona {i} de manera ordenada:", 5, 50)
        numerotel = validar_entrada(f"Ingrese el numero de telefono de la persona {i} (10 digitos):", 10, 10, lambda x: x.isdigit())#lambda la utilizo para realizar cosas simples como lo son las funciones en anonimo
        correousuario = validar_entrada(f"Ingrese el correo electronico de la persona {i}:", 5, 50, lambda x: "@" in x)
        contador = len(personas) + 1
        dict_nuevo = {
            "ID de la persona": contador,
            "Nombre": nombreusuario,
            "Apellidos": apellidosusuario,
            "Numero de telefono": numerotel,
            "Correo electronico": correousuario
        }
        personas.append(dict_nuevo)
        print("Usuario registrado exitosamente.\n")
def edit_user(id_usuario):
    usuario_encontrado = False
    for usuario in personas:
        if usuario["ID de la persona"] == id_usuario:
            usuario_encontrado = True
            print("Usuario encontrado. Ingrese los nuevos datos:")
            usuario["Nombre"] = validar_entrada("Ingrese el nuevo nombre completo:", 5, 50)
            usuario["Apellidos"] = validar_entrada("Ingrese los nuevos apellidos de manera ordenada:", 5, 50)
            usuario["Numero de telefono"] = validar_entrada("Ingrese el nuevo numero de telefono (10 digitos):", 10, 10, lambda x: x.isdigit())
            usuario["Correo electronico"] = validar_entrada("Ingrese el nuevo correo electronico:", 5, 50, lambda x: "@" in x)
            print("Informacion actualizada exitosamente.")
            break
    if not usuario_encontrado:
        print("No se encontro ningun usuario con ese ID.")
def delete_user(id_usuario):
    usuario = next((u for u in personas if u["ID de la persona"] == id_usuario), None)
    if usuario:
        personas.remove(usuario)
        print("Usuario eliminado exitosamente.")
    else:
        print("No se encontro ningun usuario con ese ID.")
def list_user():
    if personas:
        print("-" * 60)
        print(imprimir_texto_centralizado("\nListado de usuarios registrados:"))
        print("-" * 60)
        for usuario in personas:
            print("-" * 60)
            for dato, ingreso in usuario.items():
                print(f"{dato}: {ingreso}")
    else:
        print("No hay usuarios registrados.")
def opp():
    opcion = 0
    while opcion != 6:
        print("-" * 90)
        print(imprimir_texto_centralizado("BIENVENIDO A EL PROGRAMA"))
        print("-" * 90)
        print("1.  Registrar nuevos usuarios")
        print("2.  Consultar usuarios")
        print("3.  Editar informacion de un usuario por ID")
        print("4.  Eliminar usuarios")
        print("5.  Listar usuarios")
        print("6.  Salir")
        opcion = input("DIGITE LA OPCION QUE DESEE EJECUTAR\n")
        if opcion == "1":
            new_user()
        elif opcion == "2":
            list_user()
        elif opcion == "3":
            id_usuario = int(input("Ingrese el ID del usuario que desea editar:\n"))
            edit_user(id_usuario)
        elif opcion == "4":
            id_usuario = int(input("Ingrese el ID del usuario que desea eliminar:\n"))
            delete_user(id_usuario)
        elif opcion == "5":
            list_user()
        elif opcion == "6":
            print("Gracias por usar el programa. Hasta luego!")
        else:
            print("Opcion no valida.")
if __name__ == "__main__":
    opp()