# 1. Entrada de datos (input siempre devuelve texto, por eso usamos float())
precio_unitario = float(input("Ingresa el precio del producto: "))
cantidad = int(input("Ingresa la cantidad vendida: "))

# 2. Proceso (Lógica de negocio)
subtotal = precio_unitario * cantidad
impuesto = subtotal * 0.19  # IVA del 19%
total = subtotal + impuesto

# 3. Salida con F-Strings (Forma moderna y avanzada de mostrar datos)
print(f"--- Recibo de Venta ---")
print(f"Subtotal: ${subtotal:,.2f}")
print(f"IVA (19%): ${impuesto:,.2f}")
print(f"Total a pagar: ${total:,.2f}")
