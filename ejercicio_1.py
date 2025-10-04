# ejercicio_1.py
import re

def validar_correo(correo):
    """
    Valida si una cadena de texto es un correo electrónico válido.

    Args:
        correo (str): La cadena de texto a validar.

    Returns:
        bool: True si el correo es válido, False en caso contrario.
    """
    # Explicación detallada del patrón:
    # ^                  -> Inicio de la cadena
    # [\w\.-]+           -> Uno o más caracteres de palabra, punto o guion (usuario)
    # @                  -> El símbolo de arroba
    # [\w\.-]+           -> Uno o más caracteres de palabra, punto o guion (dominio)
    # \.                 -> Un punto literal
    # [a-zA-Z]{2,}       -> Al menos dos letras para el TLD (Top-Level Domain)
    # $                  -> Fin de la cadena
    patron = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
    
    return bool(re.fullmatch(patron, correo))

# --- Casos de prueba ---
if __name__ == "__main__":
    correos_prueba = [
        "usuario@ejemplo.com",
        "nombre.apellido@dominio.mx",
        "usuarioejemplo.com",
        "@ejemplo.com"
    ]

    print("Validación de correos electrónicos:\n")
    for correo in correos_prueba:
        estado = "Válido" if validar_correo(correo) else "Inválido"
        print(f"'{correo}' → {estado}")
