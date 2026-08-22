nombre_usuario = input("Ingresa tu nombre: \n")
#hobbie = []
#hobbie.append(input("Ingresa un hobbie: \n"))
#hobbie.append(input("Ingresa un hobbie: \n"))
#hobbie.append(input("Ingresa un hobbie: \n"))

hobbie = input("Ingresa 3 hobbies separados por comas: \n").split(",")

diccionario_usuarios = {
    "nombre_usuario": nombre_usuario,
    "hobbies":hobbie
}


print(diccionario_usuarios)