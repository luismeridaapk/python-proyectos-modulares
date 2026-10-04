# ==============================================================================
# PROYECTO: Sistema Integrado de Auditoría y Métricas Financieras (FinancialTracker)
# ==============================================================================
# DESCRIPCIÓN:
#   Módulo de procesamiento y análisis financiero (core_analytics.py).
#   Contiene las funciones para lectura resiliente de transacciones, cálculo
#   de balance/métricas, extracción de categorías y exportación en formato JSON.
# FECHA: 3 de Octubre de 2026
# MÓDULO: Módulo 8 - Proyecto 2 (Integrador Fase 2)
# ==============================================================================

import json


# ==============================================================================
# LECTURA Y PROCESAMIENTO RESILIENTE DE TRANSACCIONES
# ==============================================================================

def cargar_transacciones(ruta_archivo, logger):
    """
    Lee un archivo de texto plano con transacciones y las parsea a diccionarios.
    
    Aplica tolerancia a fallos: omite líneas con campos insuficientes o valores
    numéricos inválidos registrando una advertencia mediante el logger.
    """
    transacciones_validas = []
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                try:
                    partes = linea.strip().split(',')
                    if len(partes) != 5:
                        raise ValueError("Formato no válido: debe contener exactamente 5 campos")
                    
                    # Casting de datos y estructuración en diccionario
                    transacciones_validas.append({
                        "id": int(partes[0]),
                        "fecha": partes[1],
                        "categoria": partes[2],
                        "monto": float(partes[3]),
                        "tipo": partes[4]
                    })
                except (ValueError, Exception) as error:
                    logger.warning(f"Línea omitida por error: {error}")
                    continue

    except FileNotFoundError:
        logger.error(f"Archivo no encontrado en la ruta: {ruta_archivo}")
    except PermissionError:
        logger.error(f"Sin permisos para leer el archivo: {ruta_archivo}")

    return transacciones_validas


# ==============================================================================
# CÁLCULO DE MÉTRICAS FINANCIERAS Y AGREGACIONES
# ==============================================================================

def calcular_metricas(transacciones):
    """
    Calcula el total de ingresos, total de egresos y el balance neto final.
    Retorna un diccionario estructurado con los resultados numéricos.
    """
    ingresos = 0.0
    egresos = 0.0
    
    for t in transacciones:
        if t["tipo"] == "INGRESO":
            ingresos += t["monto"]
        elif t["tipo"] == "EGRESO":
            egresos += t["monto"]
            
    balance = ingresos - egresos
    
    return {
        "total_ingresos": ingresos,
        "total_egresos": egresos,
        "balance_neto": balance
    }


def obtener_categorias_unicas(transacciones):
    """
    Extrae un conjunto (set) con todas las categorías registradas sin duplicados.
    """
    unicas = set()
    for t in transacciones:
        unicas.add(t["categoria"])
    return unicas


# ==============================================================================
# PERSISTENCIA Y EXPORTACIÓN DE REPORTES EN JSON
# ==============================================================================

def exportar_reporte_json(ruta_salida, transacciones, metricas, logger):
    """
    Exporta la estructura completa de transacciones y métricas en un archivo .json.
    """
    datos_reporte = {
        "metricas": metricas,
        "transacciones": transacciones
    }
    try:
        with open(ruta_salida, 'w', encoding='utf-8') as archivo:
            json.dump(datos_reporte, archivo, indent=4, ensure_ascii=False)
            
        logger.info(f"Reporte exportado exitosamente a: {ruta_salida}")

    except Exception as error:
        logger.error(f"Ocurrió un error al exportar el archivo JSON: {error}")