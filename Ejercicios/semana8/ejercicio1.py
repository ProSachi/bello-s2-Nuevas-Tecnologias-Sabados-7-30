import pandas as pd
import json

with open("datos.js", "r", encoding="utf-8") as archivo:
	datos_empleados = json.load(archivo)

df_empleados = pd.DataFrame(datos_empleados)

print(df_empleados)