# ==============================================================================
# PROYECTO: Sistema de Análisis de Registros (LogAnalytics)
# ==============================================================================
# DESCRIPCIÓN:
#   Módulo de entrada/salida de datos (I/O Handler).
#   Encargado de la lectura de archivos de registro de texto plano y de la
#   exportación de reportes procesados en formato JSON.
# FECHA: 19 de Septiembre de 2026
# MÓDULO: Módulo 7 - Proyecto 1 (Procesamiento de Logs)
# ==============================================================================

import json


# ==============================================================================
# FUNCIONES DE LECTURA Y ESCRITURA
# ==============================================================================

def leer_registros(ruta_archivo):
    """
    Lee un archivo de texto plano y devuelve una lista con sus líneas limpias.

    Args:
        ruta_archivo (str): La ubicación del archivo de registros a leer.

    Returns:
        list: Lista de cadenas de texto sin saltos de línea ni espacios extra.
              Devuelve una lista vacía [] si no se encuentra el archivo.
    """
    try:
        # Abre el archivo y limpia cada línea omitiendo saltos de línea ('\n')
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas_limpias = [linea.strip() for linea in archivo]
        return   lineas_limpias
    except FileNotFoundError:
        # Retorna lista vacía si la ruta no existe para evitar que el programa falle
        return []


def guardar_reporte_json(ruta_destino, datos):
    """
    Exporta una estructura de datos a un archivo con formato JSON.

    Args:
        ruta_destino (str): La ubicación donde se guardará el archivo JSON.
        datos (dict): Los datos estructurados del reporte a serializar.

    Returns:
        bool: True si la escritura fue exitosa.
    """
    # Guarda los datos con sangría de 4 espacios para legibilidad
    with open(ruta_destino, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)
    return True