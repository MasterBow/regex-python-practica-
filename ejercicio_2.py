import re

def extraer_telefonos(texto):
    """
    Encuentra y extrae todos los números de teléfono de un texto.

    Args:
        texto (str): El texto del cual extraer los números.

    Returns:
        list: Una lista con los números de teléfono encontrados.
    """
    # Expresión regular para detectar los diferentes formatos de teléfono
    # \(?     -> Paréntesis de apertura opcional
    # \d{3}   -> Exactamente 3 dígitos (LADA)
    # \)?     -> Paréntesis de cierre opcional
    # [\s-]?  -> Un espacio o un guion opcional
    # \d{3}   -> Exactamente 3 dígitos
    # [\s-]?  -> Un espacio o un guion opcional
    # \d{4}   -> Exactamente 4 dígitos
    patron = r'\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}'

    telefonos = re.findall(patron, texto)
    return telefonos

# --- Ejemplo de uso ---
texto_entrada = "Contacta a Juan al 646-123-4567 o a María al (664) 987-6543. También puedes llamar al 5551234567."
telefonos_encontrados = extraer_telefonos(texto_entrada)

print(f"Teléfonos encontrados: {telefonos_encontrados}")
