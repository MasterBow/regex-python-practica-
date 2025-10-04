import re
from datetime import datetime

def formatear_fechas(texto):
    """
    Encuentra fechas en diferentes formatos y las convierte a YYYY-MM-DD.

    Args:
        texto (str): El texto a analizar.

    Returns:
        list: Una lista de tuplas con la fecha original y la formateada.
    """
    # Mapeo de meses en español e inglés a números para facilitar la conversión
    meses_map = {
        'Ene': '01', 'Feb': '02', 'Mar': '03', 'Abr': '04', 'May': '05', 'Jun': '06',
        'Jul': '07', 'Ago': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dic': '12',
        'Enero': '01', 'Febrero': '02', 'Marzo': '03', 'Abril': '04', 'Mayo': '05', 'Junio': '06',
        'Julio': '07', 'Agosto': '08', 'Septiembre': '09', 'Octubre': '10', 'Noviembre': '11', 'Diciembre': '12'
    }
    
    # Patrones para cada formato de fecha
    patrones = {
        # DD/MM/YYYY
        r'\b(\d{2})/(\d{2})/(\d{4})\b': '%d/%m/%Y',
        # YYYY-MM-DD
        r'\b(\d{4})-(\d{2})-(\d{2})\b': '%Y-%m-%d',
        # DD-MMM-YYYY (ej. 01-Dic-2024)
        r'\b(\d{2})-([A-Za-z]{3})-(\d{4})\b': None, # Manejo especial
        # Mes DD, YYYY (ej. Diciembre 01, 2024)
        r'\b([A-Za-z]+)\s(\d{1,2}),\s(\d{4})\b': None # Manejo especial
    }
    
    fechas_convertidas = []

    for patron, formato_str in patrones.items():
        coincidencias = re.findall(patron, texto)
        for fecha_encontrada in coincidencias:
            fecha_original_str = ' '.join(fecha_encontrada).replace('-', ' ') # Unificar separadores
            
            try:
                if patron == r'\b(\d{2})-([A-Za-z]{3})-(\d{4})\b': # DD-MMM-YYYY
                    dia, mes_str, anio = fecha_encontrada
                    mes_num = meses_map[mes_str.capitalize()]
                    fecha_obj = datetime.strptime(f"{dia}/{mes_num}/{anio}", '%d/%m/%Y')
                    fecha_original_str = f"{dia}-{mes_str}-{anio}"

                elif patron == r'\b([A-Za-z]+)\s(\d{1,2}),\s(\d{4})\b': # Mes DD, YYYY
                    mes_str, dia, anio = fecha_encontrada
                    mes_num = meses_map[mes_str.capitalize()]
                    fecha_obj = datetime.strptime(f"{dia}/{mes_num}/{anio}", '%d/%m/%Y')
                    fecha_original_str = f"{mes_str} {dia}, {anio}"

                else: # Formatos directos
                    fecha_obj = datetime.strptime("-".join(fecha_encontrada), formato_str.replace('/','-'))
                    fecha_original_str = "/".join(fecha_encontrada) if "/" in patron else "-".join(fecha_encontrada)
                
                fecha_estandar = fecha_obj.strftime('%Y-%m-%d')
                fechas_convertidas.append((fecha_original_str, fecha_estandar))
            except (ValueError, KeyError):
                # Ignora si el mes no se encuentra o el formato es inválido
                continue
                
    return fechas_convertidas

# --- Ejemplo de uso ---
texto_fechas = "La reunión es el 15/03/2024. El proyecto inicia el 2024-04-20 y termina en Junio 30, 2024. La entrega final es 01-Jul-2024."
resultado = formatear_fechas(texto_fechas)

print("Fechas encontradas y convertidas:")
for original, estandar in resultado:
    print(f"- Formato original: {original} → Estándar: {estandar}")
