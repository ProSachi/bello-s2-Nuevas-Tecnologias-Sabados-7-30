# Importación específica del módulo creado
from reglas_calidad import limpiar_cadena, validar_edad

datos_crudos = [
    {"nombre": "  Ana ", "edad": "28"},
    {"nombre": "Luis", "edad": "110"}, # Edad inválida
    {"nombre": " Carlos", "edad": "error"} # Tipo inválido
]

usuarios_limpios = []

for registro in datos_crudos:
    nombre_limpio = limpiar_cadena(registro["nombre"])
    edad_valida = validar_edad(registro["edad"])
    
    # Solo agregamos si la edad superó la regla de calidad (no es None)
    if edad_valida is not None:
        usuarios_limpios.append({
            "nombre": nombre_limpio,
            "edad": edad_valida
        })

print("Datos listos para análisis:", usuarios_limpios)
