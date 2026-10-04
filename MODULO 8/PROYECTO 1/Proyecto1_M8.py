# ==============================================================================
# PROYECTO: Sistema Resiliente de Auditoría de Registros (Robust Log Auditor)
# ==============================================================================
# DESCRIPCIÓN:
#   Script principal de orquestación e interfaz de línea de comandos (Proyecto1_M8.py).
#   Integra la inicialización del sistema de trazabilidad con la lectura resiliente
#   de archivos mediante un flujo estructurado en try-except-else-finally.
# FECHA: 26 de Septiembre de 2026
# MÓDULO: Módulo 8 - Proyecto 1 (Auditoría & Logging)
# ==============================================================================

from logger_config import obtener_logger
from log_processor import leer_archivo_logs


# ==============================================================================
# CONFIGURACIÓN E INICIALIZACIÓN DEL SISTEMA
# ==============================================================================

# Inicialización del registrador de auditoría al arrancar la aplicación
logger = obtener_logger()
logger.info("Aplicación iniciada")


# ==============================================================================
# BUCLE PRINCIPAL / MENÚ INTERACTIVO (CLI)
# ==============================================================================

while True:
    print("\n" + "="*50)
    print("      SISTEMA DE AUDITORÍA Y PROCESAMIENTO DE LOGS")
    print("="*50)
    print("1.- Procesar archivo de logs")
    print("2.- Salir")
    print("="*50)
    
    # --------------------------------------------------------------------------
    # ESTRUCTURA ROBUSTA DE CONTROL DE FLUJO Y EXCEPCIONES
    # --------------------------------------------------------------------------
    try:
        opcion = input("Elija una opción (1-2): ").strip()
        
        # Opciones de flujo del menú
        if opcion == "1":
            # Limpieza de entrada para remover comillas accidentales de la ruta
            ruta_archivo = input("Ingrese la ruta del archivo logs: ").strip().strip('"\'')
            if not ruta_archivo:
                raise ValueError("La ruta del archivo no puede estar vacía.")
            
            # Ejecución de lectura y auditoría de registros
            registros = leer_archivo_logs(ruta_archivo, logger)
            
        elif opcion == "2":
            logger.info("El usuario finalizó la sesión")
            print("\nSaliendo del procesador de archivos log...")
            break
            
        else:
            raise ValueError("Opción no válida. Seleccione 1 o 2.")

    # --------------------------------------------------------------------------
    # MANEJO DE EXCEPCIONES Y REGISTRO EN BITÁCORA
    # --------------------------------------------------------------------------
    except ValueError as ve:
        print(f"\nError: {ve}")
        logger.warning(ve)
        
    except KeyboardInterrupt:
        print("\n\nEjecución interrumpida por el usuario. Saliendo...")
        break
        
    # --------------------------------------------------------------------------
    # BLOQUE ELSE: Confirmación de procesamiento exitoso
    # --------------------------------------------------------------------------
    else:
        print(f"\nSe procesaron {len(registros)} registros válidos.")
        logger.info(f"Procesamiento finalizado. Registros procesados: {len(registros)}")
        
    # --------------------------------------------------------------------------
    # BLOQUE FINALLY: Cierre de ciclo visual garantizado
    # --------------------------------------------------------------------------
    finally:
        print("-" * 50)