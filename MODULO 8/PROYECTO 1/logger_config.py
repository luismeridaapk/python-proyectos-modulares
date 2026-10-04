# ==============================================================================
# PROYECTO: Sistema Resiliente de Auditoría de Registros (Robust Log Auditor)
# ==============================================================================
# DESCRIPCIÓN:
#   Módulo de configuración centralizada del sistema de trazabilidad (logger_config.py).
#   Define el archivo de salida para logs, el formato de estampilla de tiempo,
#   el nivel de severidad de los eventos y entrega la instancia para registro.
# FECHA: 26 de Septiembre de 2026
# MÓDULO: Módulo 8 - Proyecto 1 (Auditoría & Logging)
# ==============================================================================

import logging


# ==============================================================================
# CONFIGURACIÓN Y OBTENCIÓN DEL LOGGER
# ==============================================================================

def obtener_logger():
    """
    Configura y retorna la instancia del registrador (logger) del sistema.
    
    Establece la persistencia de eventos en 'app.log' con nivel mínimo INFO,
    definiendo un formato estandarizado con fecha, módulo, nivel y mensaje.
    """
    # Configuración base del sistema de logging
    logging.basicConfig(
        filename='app.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Obtención del registrador asociado al contexto del módulo actual
    logger = logging.getLogger(__name__)
    return logger