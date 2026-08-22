mi_lista = [1, "Hola", 3.14, True]
print(mi_lista[0])      # Acceso por índice: 1
mi_lista.append("nuevo") # Añadir elemento
print(mi_lista)         # Salida: [1, 'Hola', 3.14, True, 'nuevo']

mi_lista.append(3)
print(mi_lista)   
mi_lista2=[2, "adios", "ok"]
print(mi_lista2)   

mi_lista3 = mi_lista.extend(mi_lista2)
print(mi_lista)  

mi_lista4 = [mi_lista, mi_lista2, mi_lista3]
print(mi_lista4)  
