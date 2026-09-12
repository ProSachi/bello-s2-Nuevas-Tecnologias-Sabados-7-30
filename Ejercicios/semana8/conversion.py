
# pipeline_local.py
ruta_in = "data/sucios/crudo.txt"
ruta_out = "data/limpio/procesado.txt"

# 1. Extraer
with open(ruta_in, "r") as f:
    contenido = f.read()

# 2. Transformar
contenido_transformado = contenido.upper()

# 3. Cargar
with open(ruta_out, "w") as f:
    f.write(contenido_transformado)
print("Pipeline local finalizado.")
