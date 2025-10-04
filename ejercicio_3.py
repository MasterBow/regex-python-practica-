import re

def validar_contrasena(contrasena):
    """
    Verifica si una contraseña cumple con los criterios de seguridad.

    Args:
        contrasena (str): La contraseña a validar.

    Returns:
        tuple: Un booleano indicando si es válida y una lista de errores.
    """
    errores = []

    # 1. Mínimo 8 caracteres
    if len(contrasena) < 8:
        errores.append("Debe tener al menos 8 caracteres de longitud.")

    # 2. Al menos una letra mayúscula (A-Z)
    if not re.search(r'[A-Z]', contrasena):
        errores.append("Debe contener al menos una letra mayúscula.")

    # 3. Al menos una letra minúscula (a-z)
    if not re.search(r'[a-z]', contrasena):
        errores.append("Debe contener al menos una letra minúscula.")

    # 4. Al menos un número (0-9)
    if not re.search(r'\d', contrasena):
        errores.append("Debe contener al menos un número.")

    # 5. Al menos un carácter especial (@$!%*?&#)
    if not re.search(r'[@$!%*?&#]', contrasena):
        errores.append("Debe contener al menos un carácter especial (@$!%*?&#).")

    es_valida = len(errores) == 0
    return es_valida, errores

# --- Casos de prueba ---
contrasenas_a_probar = ["Segura123!", "contrasena", "MAYUSCULA123!", "P@ssw0rd"]

for pwd in contrasenas_a_probar:
    valida, mensajes = validar_contrasena(pwd)
    if valida:
        print(f"✅ '{pwd}' → Válida")
    else:
        print(f"❌ '{pwd}' → Inválida. Razones: {' '.join(mensajes)}")
