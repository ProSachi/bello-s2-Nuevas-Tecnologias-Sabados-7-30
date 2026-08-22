def limpiar_cadena(texto):
    """Elimina espacios en blanco extra y convierte a minúsculas."""
    if isinstance(texto, str):
        return texto.strip().lower()
    return ""

def validar_edad(edad):
    """Verifica que la edad sea un número lógico para un humano."""
    try:
        edad_num = int(edad)
        if 0 < edad_num <= 120:
            return edad_num
        return None
    except (ValueError, TypeError):
        return None
