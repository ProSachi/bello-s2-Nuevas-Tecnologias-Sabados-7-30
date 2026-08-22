
import validacion


# def suma(a, b):
#     resultado = a + b
#     print("El resultado es", resultado)
# def suma2(a, b):
#     resultado = a + b
#     return resultado
# resultado = suma2(4, 5)
# print("El resultado es", resultado)

usuario = input("Ingresa el usuario")
contrasena = input("Ingresa la contraseña")
Islogin = validacion.login(usuario, contrasena)

if Islogin:
    print("Usuario logeado")
else:
    print("Usuario no logeado")

