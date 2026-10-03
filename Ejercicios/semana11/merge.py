from pathlib import Path

PROCESSED = Path(__file__).parent / "Data" / "processed"


def validar_premerge(clientes, ventas):
    ok = True
    if "id_cliente" not in clientes.columns or "id_cliente" not in ventas.columns:
        print("Falta la columna id_cliente en alguno de los dataframes.")
        return False

    if clientes["id_cliente"].duplicated().any():
        print("Hay id_cliente duplicados en clientes.")
        ok = False

    if clientes["id_cliente"].dtype != ventas["id_cliente"].dtype:
        print("El tipo de id_cliente difiere entre clientes y ventas.")
        ok = False

    huerfanos = ~ventas["id_cliente"].isin(clientes["id_cliente"])
    if huerfanos.any():
        print(f"Ventas sin cliente asociado: {huerfanos.sum()}")

    return ok


def unir(clientes, ventas):
    if not validar_premerge(clientes, ventas):
        return None
    df = ventas.merge(clientes, on="id_cliente", how="left", validate="m:1")
    PROCESSED.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED / "merge.csv", index=False)
    print(f"Merge realizado: {df.shape[0]} filas, {df.shape[1]} columnas.")
    return df