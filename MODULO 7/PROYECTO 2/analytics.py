# ==============================================================================
# PROYECTO: Sistema de Gestión y Análisis de Proyectos (ProjectTracker)
# ==============================================================================
# DESCRIPCIÓN:
#   Módulo de procesamiento y analítica de datos (Analytics Module).
#   Encargado de la transformación de registros de texto a estructuras en memoria,
#   extracción de conjuntos únicos, cálculo de métricas acumuladas y filtrado.
# FECHA: 20 de Septiembre de 2026
# MÓDULO: Módulo 7 - Proyecto 2 (Consolidación)
# ==============================================================================


# ==============================================================================
# FUNCIONES DE PROCESAMIENTO Y ANALÍTICA
# ==============================================================================

def estructurar_tareas(lineas_raw):
    """
    Transforma una lista de cadenas de texto en formato plano a una lista de
    diccionarios con tipos de datos convertidos.

    Args:
        lineas_raw (list): Lista de cadenas de texto con separadores " | ".

    Returns:
        list: Lista de diccionarios con claves ('id', 'titulo', 'estado', 'horas').
    """
    # Función anónima para parsear cada línea y castear tipos numéricos
    plantilla = lambda linea: {
        "id": int(linea.split(" | ")[0]),
        "titulo": linea.split(" | ")[1],
        "estado": linea.split(" | ")[2],
        "horas": int(linea.split(" | ")[3])
    }
    # List comprehension para estructurar todos los registros
    lista_diccionarios = [plantilla(linea) for linea in lineas_raw]
    return lista_diccionarios


def obtener_estados_unicos(tareas):
    """
    Extrae las categorías de estados sin duplicados presentes en la lista de tareas.

    Args:
        tareas (list): Lista de diccionarios que representan las tareas.

    Returns:
        set: Conjunto de cadenas de texto con los estados únicos.
    """
    # Set comprehension para filtrar automáticamente duplicados
    unicos = {dic["estado"] for dic in tareas}
    return unicos


def calcular_metricas_horas(tareas):
    """
    Calcula la suma total y el promedio de horas acumuladas en las tareas.

    Args:
        tareas (list): Lista de diccionarios con la información de las tareas.

    Returns:
        tuple: Tupla con el formato (total_horas, promedio_horas).
    """
    # Manejo de lista vacía para evitar división por cero
    if not tareas:
        return (0, 0.0)

    # Extrae solo la clave 'horas' y calcula los agregados
    lista_horas = [dic["horas"] for dic in tareas]
    total_horas = sum(lista_horas)
    promedio_horas = total_horas / len(lista_horas)

    return (total_horas, promedio_horas)


def filtrar_por_estado(tareas, estado_buscado):
    """
    Filtra las tareas que coinciden con un estado específico.

    Args:
        tareas (list): Lista de diccionarios con las tareas.
        estado_buscado (str): El estado por el cual filtrar (ej. 'COMPLETADO').

    Returns:
        list: Subconjunto de tareas que cumplen con la condición.
    """
    # Programación funcional combinando filter() y lambda
    estados_filtrados = list(filter(lambda dic: dic["estado"] == estado_buscado, tareas))
    return estados_filtrados