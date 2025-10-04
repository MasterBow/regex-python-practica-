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
    # Patrón para un correo electrónico básico
    patron = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
    
    # Retorna True si toda la cadena coincide con el patrón
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
