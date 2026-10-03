def analizar(df):
    print("\nInfo general:")
    df.info()
    print("\nEstadísticas numéricas:")
    print(df.describe())
    for col, etiqueta in [
        ("ciudad", "ciudad"),
        ("categoria", "categoría"),
        ("segmento_cliente", "segmento de cliente"),
        ("canal", "canal"),
    ]:
        print(f"\nTotal vendido por {etiqueta}:")
        print(df.groupby(col)["total"].sum().sort_values(ascending=False))