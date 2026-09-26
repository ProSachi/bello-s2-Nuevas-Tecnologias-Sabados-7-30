import pandas as pd
# ==========================================
# 0. INSUMO SUCIO (Desde un Diccionario Python)
# ==========================================
diccionario_clientes = {
    'id_cliente': [101, 102, 103, 102, 104],
    'nombre': ['  Ana Gomez  ', 'carlos Ruiz', ' LUIS perez ', 'carlos Ruiz', 'maria Lopez'],
    'correo': ['ana@mail.com', None, 'luis@mail.com', None, 'maria@mail.com'],
    'ciudad': ['bogota', '  MEDELLIN  ', None, '  MEDELLIN  ', ' bogota ']
}
# ==========================================
# 1. INGESTA (De Diccionario a DataFrame)
# ==========================================
print("--- DATOS CRUDOS DESDE DICCIONARIO ---")
# Aquí cambiamos read_csv() por el constructor directo DataFrame()
df_clientes = pd.DataFrame(diccionario_clientes)
print(df_clientes)

#df_clientes.info()
#print(df_clientes['correo'].isna().sum())

# ==========================================
# 2. ELIMINACIÓN DE CLONES EXACTOS
# ==========================================
df_clientes_limpio = df_clientes.drop_duplicates()

#df_clientes_limpio.info()

# ==========================================
# 3. TRATAMIENTO DE NULOS (Toma de decisiones)
# ==========================================

df_clientes_limpio['correo'] = df_clientes_limpio['correo'].fillna("sin_correo@empresa.com")
df_clientes_limpio['ciudad'] = df_clientes_limpio['ciudad'].fillna("DESCONOCIDA")

# ==========================================
# 4. ESTANDARIZACIÓN DE TEXTOS
# ==========================================

df_clientes_limpio['nombre'] = df_clientes_limpio['nombre'].str.strip().str.title()
df_clientes_limpio['ciudad'] = df_clientes_limpio['ciudad'].str.strip().str.title()
df_clientes_limpio['correo'] = df_clientes_limpio['correo'].str.strip().str.lower()

# ==========================================
# RESULTADO FINAL
# ==========================================
print("\n--- DATOS LIMPIOS: LISTOS PARA CALIDAD RELACIONAL ---")
print(df_clientes_limpio)

df_clientes_limpio.to_csv("data/processed/limpios.csv", index=False)