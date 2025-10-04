# regex-python-practica-
Practica sobre Desarrollar habilidades en el uso de expresiones regulares (regex) en Python mediante ejercicios prácticos que aumentan progresivamente en complejidad.
1. Validador de Correos Electrónicos Simple

Este programa utiliza una expresión regular para verificar si una cadena de texto tiene la estructura básica de un correo electrónico.Resumen de la solución

El código define una función validar_correo que toma un correo electrónico como entrada. Usa una expresión regular para comprobar que la cadena contiene caracteres antes y después de un @, y que termina con un punto seguido de un dominio de al menos dos letras.

--- Casos de prueba ---

print(f"'usuario@ejemplo.com' → {'Válido' if validar_correo('usuario@ejemplo.com') else 'Inválido'}")

print(f"'nombre.apellido@dominio.mx' → {'Válido' if validar_correo('nombre.apellido@dominio.mx') else 'Inválido'}")

print(f"'usuarioejemplo.com' → {'Válido' if validar_correo('usuarioejemplo.com') else 'Inválido'}")

print(f"'@ejemplo.com' → {'Válido' if validar_correo('@ejemplo.com') else 'Inválido'}")

-----

### 2. Extractor de Números de Teléfono

Este programa utiliza una expresión regular para encontrar todos los números de teléfono con formato mexicano de 10 dígitos dentro de un texto.

#### Resumen de la solución

La función `extraer_telefonos` recibe un texto y busca todas las coincidencias que sigan los patrones de números telefónicos especificados (10 dígitos seguidos, con guiones, espacios o paréntesis).

--- Ejemplo de uso ---

texto_entrada = "Contacta a Juan al 646-123-4567 o a María al (664) 987-6543. También puedes llamar al 5551234567."

telefonos_encontrados = extraer_telefonos(texto_entrada)

print(f"Teléfonos encontrados: {telefonos_encontrados}")
Guarda el código en un archivo de Python (por ejemplo, extractor_telefonos.py).
Ejecuta el script.
Puedes cambiar el valor de la variable texto_entrada para analizar diferentes textos.
-----3. Validador de Contraseñas Seguras

Este validador verifica si una contraseña cumple con varios criterios de seguridad y, si no, informa al usuario qué le falta.Resumen de la solución

La función validar_contrasena revisa una contraseña contra una lista de requisitos. Utiliza expresiones regulares para verificar la presencia de mayúsculas, minúsculas, números y caracteres especiales. También comprueba la longitud mínima.

--- Casos de prueba ---

contrasenas_a_probar = ["Segura123!", "contrasena", "MAYUSCULA123!", "P@ssw0rd"]

for pwd in contrasenas_a_probar:
valida, mensajes = validar_contrasena(pwd)

if valida:

    print(f"✅ '{pwd}' → Válida")

else:

    print(f"❌ '{pwd}' → Inválida. Razones: {' '.join(mensajes)}")

-----

### 4. Extractor de URLs y Dominios

Este programa busca URLs en un texto y luego las descompone para extraer el protocolo, el dominio y la ruta.

#### Resumen de la solución

Primero, una expresión regular encuentra todas las posibles URLs en el texto. Luego, otra expresión regular más detallada se aplica a cada URL encontrada para separar sus componentes.

--- Ejemplo de uso ---

texto_ejemplo = "Visita https://www.google.com o http://github.com/usuario. También puedes ir a www.python.org para más info."

extraer_urls(texto_ejemplo)
-----5. Analizador de Fechas y Formateador

Este programa encuentra fechas en varios formatos dentro de un texto y las convierte al formato estándar YYYY-MM-DD.Resumen de la solución

Este es el desafío más complejo. Se usan múltiples expresiones regulares, una para cada formato de fecha. La función datetime.strptime() ayuda a "entender" la fecha encontrada, y strftime() la convierte al formato deseado.

--- Ejemplo de uso ---

texto_fechas = "La reunión es el 15/03/2024. El proyecto inicia el 2024-04-20 y termina en Junio 30, 2024. La entrega final es 01-Jul-2024."

resultado = formatear_fechas(texto_fechas)

print("Fechas encontradas y convertidas:")

for original, estandar in resultado:
print(f"- Formato original: {original} → Estándar: {estandar}")
## ✅ 1. Validador de Correos Electrónicos
El código valida correctamente los formatos válidos (usuario@ejemplo.com, nombre.apellido@dominio.mx) y rechaza los inválidos (usuarioejemplo.com, @ejemplo.com) tal como se pedía.

## ✅ 2. Extractor de Números de Teléfono
La expresión regular identifica y extrae exitosamente los tres formatos de número telefónico del texto de ejemplo, devolviendo la lista: ['646-123-4567', '(664) 987-6543', '5551234567'].

## ✅ 3. Validador de Contraseñas Seguras
El programa evalúa correctamente cada contraseña de prueba. Aprueba las que son seguras (Segura123!, P@ssw0rd) y rechaza las que no lo son, indicando con precisión los criterios que faltan en cada caso.

## ✅ 4. Extractor de URLs y Dominios
La solución extrae y descompone las URLs como se esperaba. Identifica https://www.google.com y http://github.com/usuario, separando su protocolo, dominio y ruta correctamente. Incluso es capaz de procesar www.python.org, asumiendo el protocolo http por defecto.
## ✅ 5. Analizador de Fechas y Formateador
El script encuentra cada uno de los distintos formatos de fecha en el texto (DD/MM/YYYY, YYYY-MM-DD, Mes DD, YYYY y DD-MMM-YYYY) y los convierte exitosamente al formato estándar YYYY-MM-DD.
En resumen, pu

