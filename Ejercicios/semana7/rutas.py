# prueba_rutas.py
ruta_origen = "data/raw/mensaje.txt"
ruta_destino = "data/processed/mensaje_copiado.txt"

# 1. Extraer (Leer crudo)
# Solo leemos el texto completo como un bloque, sin ciclos.
with open(ruta_origen, "r") as archivo_crudo:
    contenido = archivo_crudo.read()

print("Dato leído:", contenido)

# 2. Cargar (Guardar procesado)
with open(ruta_destino, "w") as archivo_final:
    archivo_final.write(contenido + " -> Validado por Python.")

print("Archivo guardado exitosamente en data/processed/")
