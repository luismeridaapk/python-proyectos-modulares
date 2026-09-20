# ==============================================================================
# PROYECTO: Sistema de Análisis de Registros (LogAnalytics)
# ==============================================================================
# DESCRIPCIÓN:
#   Módulo de procesamiento de datos (Processor).
#   Contiene las funciones encargadas de transformar las cadenas de texto raw
#   en diccionarios estructurados, filtrar registros por categoría y calcular
#   las estadísticas de los tipos de registro.
# FECHA: 19 de Septiembre de 2026
# MÓDULO: Módulo 7 - Proyecto 1 (Procesamiento de Logs)
# ==============================================================================


# ==============================================================================
# ETAPA 1: ESTRUCTURACIÓN Y TRANSFORMACIÓN DE DATOS
# ==============================================================================

def estructurar_registros(lineas_raw):
    """
    Convierte una lista de cadenas de texto sin formato en una lista de diccionarios.

    Args:
        lineas_raw (list): Lista de cadenas de texto con formato "fecha | tipo | mensaje".

    Returns:
        list: Lista de diccionarios donde cada elemento contiene las claves 'fecha', 'tipo' y 'mensaje'.
    """
    # Función lambda para desglosar la línea mediante el separador ' | '
    plantilla = lambda linea: {
        "fecha": linea.split(" | ")[0],
        "tipo": linea.split(" | ")[1],
        "mensaje": linea.split(" | ")[2]}
    
    # List comprehension para aplicar la plantilla a cada línea
    lista_diccionarios = [plantilla(linea) for linea in lineas_raw]
    return lista_diccionarios


# ==============================================================================
# ETAPA 2: FILTRADO Y ANÁLISIS ESTADÍSTICO
# ==============================================================================

def filtrar_por_tipo(registros, tipo_buscado):
    """
    Filtra los registros según el tipo especificado (INFO, ERROR, WARNING).

    Args:
        registros (list): Lista de diccionarios de registros estructurados.
        tipo_buscado (str): La categoría por la cual se desea filtrar.

    Returns:
        list: Lista de diccionarios que coinciden con el tipo buscado.
    """
    # Uso de filter() con lambda para obtener solo las coincidencias
    filtrados = list(filter(lambda registro: registro["tipo"] == tipo_buscado, registros))
    return filtrados 


def obtener_estadisticas(registros):
    """
    Calcula el total de ocurrencias por cada tipo de registro.

    Args:
        registros (list): Lista de diccionarios de registros estructurados.

    Returns:
        dict: Diccionario con el conteo acumulado para INFO, ERROR y WARNING.
    """
    # Inicialización de contadores
    contador = {"INFO":0,
                "ERROR": 0,
                "WARNING": 0}
    
    # Recorrido para comparar el tipo de cada registro con los tipos en el diccionario
    for clave, valor in contador.items():
        for dic in registros:
            if dic["tipo"] == clave:
                contador[clave] += 1
    return contador