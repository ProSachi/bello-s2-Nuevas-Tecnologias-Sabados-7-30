from enum import nonmember


valor_texto = input("Escribe un número: ")
doble = valor_texto * 2
print("El doble es:", doble)


nombre = input("Dame tu nombre")
altura = input("Dame tu altura")
edad = input("Dame tu edad")
print(type(nombre))
print(type(altura))
print(type(edad))
altura = float(altura)
edad = int(edad)
print(type(nombre))
print(type(altura))
print(type(edad))