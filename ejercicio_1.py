import re

def validar_correo(correo):
    """
    Valida si una cadena de texto es un correo electrónico válido.

    Args:
        correo (str): La cadena de texto a validar.

    Returns:
        bool: True si el correo es válido, False en caso contrario.
    """
    # Expresión regular para validar el formato de correo electrónico
    # ^                  -> Inicio de la cadena
    # [\w\.-]+           -> Uno o más caracteres de palabra, punto o guion (usuario)
    # @                  -> El símbolo de arroba
    # [\w\.-]+           -> Uno o más caracteres de palabra, punto o guion (dominio)
    # \.                 -> Un punto literal
    # [a-zA-Z]{2,}       -> Al menos dos letras para el TLD (Top-Level Domain)
    # $                  -> Fin de la cadena
    patron = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'

    if re.match(patron, correo):
        return True
    else:
        return False

# --- Casos de prueba ---
print(f"'usuario@ejemplo.com' → {'Válido' if validar_correo('usuario@ejemplo.com') else 'Inválido'}")
print(f"'nombre.apellido@dominio.mx' → {'Válido' if validar_correo('nombre.apellido@dominio.mx') else 'Inválido'}")
print(f"'usuarioejemplo.com' → {'Válido' if validar_correo('usuarioejemplo.com') else 'Inválido'}")
print(f"'@ejemplo.com' → {'Válido' if validar_correo('@ejemplo.com') else 'Inválido'}")
