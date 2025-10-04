import re

def extraer_urls(texto):
    """
    Extrae URLs de un texto y las descompone en protocolo, dominio y ruta.

    Args:
        texto (str): El texto a analizar.
    """
    # Expresión regular para encontrar URLs
    patron_url = r'(https?://[^\s/$.?#].[^\s]*|www\.[^\s/$.?#].[^\s]*)'
    urls_encontradas = re.findall(patron_url, texto)

    # Expresión regular para descomponer cada URL
    # (https?)?   -> Grupo 1: Protocolo (http o https), opcional
    # (www\.)?    -> Grupo 2: Subdominio 'www.', opcional
    # ([^/]+)     -> Grupo 3: Dominio (cualquier cosa hasta el siguiente '/')
    # (/.+)?      -> Grupo 4: Ruta (la barra y todo lo que sigue), opcional
    patron_descomposicion = r'(https?)?://?(www\.)?([^/]+)(/.+)?'

    for i, url in enumerate(urls_encontradas, 1):
        print(f"URL {i}: {url}")
        match = re.match(patron_descomposicion, url)
        if match:
            protocolo = match.group(1) or 'http' # Asume http si no está presente
            dominio = (match.group(2) or '') + match.group(3)
            ruta = match.group(4) or 'N/A'

            print(f"  Protocolo: {protocolo}")
            print(f"  Dominio: {dominio}")
            if ruta != 'N/A':
                print(f"  Ruta: {ruta}")
        print() # Línea en blanco para separar

# --- Ejemplo de uso ---
texto_ejemplo = "Visita https://www.google.com o http://github.com/usuario. También puedes ir a www.python.org para más info."
extraer_urls(texto_ejemplo)
