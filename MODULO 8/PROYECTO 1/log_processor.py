# ==============================================================================
# PROYECTO: Sistema Resiliente de Auditoría de Registros (Robust Log Auditor)
# ==============================================================================
# DESCRIPCIÓN:
#   Módulo de procesamiento y lectura resiliente de archivos de texto (log_processor.py).
#   Contiene la lógica para validar la estructura de cada línea, verificar umbrales
#   de negocio e iterar sobre el archivo capturando excepciones de I/O y formato.
# FECHA: 26 de Septiembre de 2026
# MÓDULO: Módulo 8 - Proyecto 1 (Auditoría & Logging)
# ==============================================================================


# ==============================================================================
# LÓGICA DE PROCESAMIENTO Y VALIDACIÓN DE LÍNEAS
# ==============================================================================

def procesar_linea(linea):
    """
    Limpia, valida y convierte una cadena de texto representando un registro de log.
    
    Aplica reglas de negocio:
    - Comprueba la existencia de exactamente 4 campos separados por coma.
    - Convierte el cuarto campo a un entero válido.
    - Valida que el valor numérico no supere el umbral de 100.
    
    Retorna un diccionario estructurado si el registro es válido.
    """
    # Limpieza de saltos de línea/espacios y segmentación por comas
    linea_limpia = linea.strip().split(',')
    
    # Validación del número de campos requeridos
    if len(linea_limpia) != 4:
        raise ValueError("Formato incorrecto: debe contener 4 campos")
    
    fecha = linea_limpia[0]
    nivel = linea_limpia[1]
    mensaje = linea_limpia[2]
    
    # Conversión segura del campo numérico a entero
    try:
        valor_num = int(linea_limpia[3])
    except ValueError:
        raise ValueError(f"El valor '{linea_limpia[3]}' no es un número entero válido")
    
    # Validación de regla de negocio (umbral superior a 100)
    if valor_num > 100:
        raise Exception("Alerta: El valor registrado supera el umbral permitido (100)")

    # Retorno de datos estructurados en formato diccionario
    return {
        "fecha": fecha,
        "nivel": nivel,
        "mensaje": mensaje,
        "valor": valor_num
    }


# ==============================================================================
# LECTURA RESILIENTE DE ARCHIVOS DE LOGS
# ==============================================================================

def leer_archivo_logs(ruta_archivo, logger):
    """
    Abre un archivo de texto e itera sobre sus líneas procesándolas de forma tolerante a fallos.
    
    Captura excepciones de acceso al archivo (I/O) y errores individuales en cada línea,
    registrando advertencias mediante el logger sin detener el flujo global del programa.
    
    Retorna una lista con todos los diccionarios de registros válidos procesados.
    """
    registros_validos = []
    
    # Apertura y lectura segura del archivo de origen
    try:
        with open(ruta_archivo, 'r', encoding="utf-8") as archivo:
            for linea in archivo:
                # Procesamiento tolerante a errores por línea individual
                try:
                    registro = procesar_linea(linea)
                    registros_validos.append(registro)
                except (ValueError, Exception) as error:
                    logger.warning(f"Línea omitida por error: {error}")
                    continue
                    
    # Captura de excepciones críticas a nivel de sistema de archivos
    except FileNotFoundError:
        logger.error(f"El archivo no existe: {ruta_archivo}")
        return registros_validos
    except PermissionError:
        logger.error(f"Sin permisos para leer: {ruta_archivo}")
        return registros_validos

    return registros_validos