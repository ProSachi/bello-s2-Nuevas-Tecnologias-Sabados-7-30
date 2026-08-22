# 1. Variables base
empresa_nombre = "DataTech Solutions"
fecha_reporte = "2026-08-10"

# 2. Lista de transacciones (simulando extracciones de una base de datos)
transacciones_usd = [1200.50, 340.00, 890.20, 150.00]
mensajes=["Generando reporte para:", "Cantidad de transacciones: " , "Última transacción registrada:"]

# 3. Diccionario que consolida la información
reporte_financiero = {
    "mensaje": mensajes,
    "empresa": empresa_nombre,
    "fecha": fecha_reporte,
    "transacciones_detalle": transacciones_usd, # Anidando la lista
    "total_operaciones": len(transacciones_usd) # Función len() cuenta los elementos
}

for clave,valor in reporte_financiero.items():
    print(clave, valor)

