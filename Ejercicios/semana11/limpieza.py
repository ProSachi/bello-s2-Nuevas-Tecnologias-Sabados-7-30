def limpiar(df, nombre):
    print(f"\n[{nombre}] Nulos por columna:")
    print(df.isnull().sum())
    print(f"[{nombre}] Filas duplicadas: {df.duplicated().sum()}")

    df = df.copy()
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].str.strip().str.lower()

    df = df.dropna().drop_duplicates().reset_index(drop=True)
    print(f"[{nombre}] Filas tras limpieza: {len(df)}")
    return df


def limpiar_datos(clientes, ventas):
    return limpiar(clientes, "clientes"), limpiar(ventas, "ventas")