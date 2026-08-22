
from matplotlib.pylab import f
mi_diccionario = {"nombre": "Ana", "edad": 28, "ciudad": "Madrid"}
#print(mi_diccionario)
#print(mi_diccionario["nombre"]) # Acceso por clave: Ana
mi_diccionario["edad"] = 29     # Modificar valor
mi_diccionario["pais"] = "España" # Añadir nuevo par
#print(mi_diccionario)

mi_diccionario2 = {
    "nombre": ["ana", "pepe" ], 
    "hobby": ["leer", "Escuchar musica"], 
    "cancion_favorita": ["rosas", "el vals del obrero"]
    }

#print("mi_diccionario2")
#print(mi_diccionario2["nombre"][0])

mi_diccionario3 = {
    "diccionario" : { "nombre" : "edad"},
    "array_list" : [1,2]
}

print("mi_diccionario")
for clave, valor in mi_diccionario.items():
    print(f"Campo: {clave} -> Contenido: {valor}")
