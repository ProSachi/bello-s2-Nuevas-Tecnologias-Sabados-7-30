datos_crudos = [
    {"nombre": "  ana torres ", "edad": "28"}, #0
    {"nombre": "Luis   ", "edad": "150"}, # Edad inválida
    {"nombre": " Carlos", "edad": "error"},
    {"nombre": "  Tania  ", "edad": "110"} # Tipo inválido
]
#Validar la edad y limpiar los nombres a sin espacios y upper case.
# Que sea entero, que sea un numero y no letras, y mayor a cero y menor a 90
# No este vacio, quitar espacio adicionales .strip() .title()
usuarios_limpios = []
for registro in datos_crudos:
    nombre_limpio = registro["nombre"].strip().title()
    try:
        edad_num = int(registro["edad"])
        if 0 < edad_num <= 90:
            edad_valida = edad_num
        else:
            edad_valida = None
    except (ValueError, TypeError):
        edad_valida = None
    
    if edad_valida is not None:
            usuarios_limpios.append({
                "nombre": nombre_limpio,
                "edad": edad_valida
            })

print("Datos listos para análisis:", usuarios_limpios)
