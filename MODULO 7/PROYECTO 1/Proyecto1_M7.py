# ==============================================================================
# PROYECTO: Sistema de Análisis de Registros (LogAnalytics)
# ==============================================================================
# DESCRIPCIÓN:
#   Módulo Principal u Orquestador (Main).
#   Coordina la integración de las funciones de lectura, estructuración,
#   análisis estadístico, filtrado de errores y exportación final del reporte
#   en formato JSON.
# FECHA: 19 de Septiembre de 2026
# MÓDULO: Módulo 7 - Proyecto 1 (Procesamiento de Logs)
# ==============================================================================

# Importación de módulos locales personalizados
from io_handler import leer_registros, guardar_reporte_json
from processor import estructurar_registros, obtener_estadisticas, filtrar_por_tipo


# ==============================================================================
# ETAPA 1: CONFIGURACIÓN DE RUTAS Y LECTURA DE DATOS
# ==============================================================================

# Definición de las rutas relativas de entrada y salida
ruta_entrada = "MODULO 7/PROYECTO 1/datos/registros.txt"
ruta_salida = "MODULO 7/PROYECTO 1/datos/registros.json"

# Lectura inicial del archivo de registros raw
lineas = leer_registros(ruta_entrada)


# ==============================================================================
# ETAPA 2: PROCESAMIENTO Y ANÁLISIS
# ==============================================================================

# Conversión de líneas de texto a lista de diccionarios
registros = estructurar_registros(lineas)

# Cálculo de estadísticas globales por tipo de registro
estadisticas = obtener_estadisticas(registros)

# Filtrado exclusivo de registros etiquetados como "ERROR"
errores = filtrar_por_tipo(registros, "ERROR")


# ==============================================================================
# ETAPA 3: CONSOLIDACIÓN Y EXPORTACIÓN DEL REPORTE
# ==============================================================================

# Construcción de la estructura final del reporte
reporte_final = {
    "resumen": estadisticas,
    "errores_detectados": errores}

# Guardado en disco del archivo JSON
guardar_reporte_json(ruta_salida, reporte_final)

# Mensaje de confirmación en consola
print("\nReporte JSON generado con éxito en:", ruta_salida)
