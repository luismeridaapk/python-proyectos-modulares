# ==============================================================================
# PROYECTO: Sistema de Gestión y Análisis de Proyectos (ProjectTracker)
# ==============================================================================
# DESCRIPCIÓN:
#   Módulo de gestión de entradas y salidas de datos (I/O Manager).
#   Encargado de cargar registros desde texto plano, actualizar el archivo
#   de almacenamiento local e importar/exportar reportes en formato JSON.
# FECHA: 20 de Septiembre de 2026
# MÓDULO: Módulo 7 - Proyecto 2 (Consolidación)
# ==============================================================================

import json


# ==============================================================================
# FUNCIONES DE LECTURA Y ESCRITURA (I/O)
# ==============================================================================

def cargar_tareas(ruta_archivo):
    """
    Lee un archivo de texto y devuelve una lista con las líneas no vacías.

    Args:
        ruta_archivo (str): La ubicación del archivo de tareas a leer.

    Returns:
        list: Lista de cadenas de texto sin saltos de línea ni espacios extra.
              Devuelve una lista vacía [] si no se encuentra el archivo.
    """
    try:
        # Abre el archivo y limpia cada línea omitiendo saltos de línea y líneas vacías
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = [linea.strip() for linea in archivo if linea.strip()]
        return lineas
    except FileNotFoundError:
        # Retorna lista vacía si la ruta no existe para evitar que el programa falle
        return []


def guardar_tareas_txt(ruta_archivo, lineas):
    """
    Guarda una lista de cadenas de texto en un archivo .txt, sobrescribiendo su contenido.

    Args:
        ruta_archivo (str): La ubicación de destino del archivo .txt a guardar.
        lineas (list): Lista de cadenas de texto formateadas a escribir.

    Returns:
        bool: True si la escritura fue exitosa.
    """
    # Escribe cada registro asegurando un único salto de línea final
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        for linea in lineas:
            archivo.write(linea.rstrip('\n') + '\n')
    return True


def exportar_json(ruta_archivo, datos):
    """
    Exporta una estructura de datos (lista de diccionarios) a un archivo JSON.

    Args:
        ruta_archivo (str): La ubicación de destino donde se guardará el archivo JSON.
        datos (list/dict): Estructura de datos a serializar.

    Returns:
        bool: True si la exportación fue exitosa.
    """
    # Serializa los datos en formato JSON con sangría de 4 espacios para legibilidad
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)
    return True