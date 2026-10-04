# ==============================================================================
# PROYECTO: Sistema Integrado de Auditoría y Métricas Financieras (FinancialTracker)
# ==============================================================================
# DESCRIPCIÓN:
#   Módulo de configuración del sistema de trazabilidad (logger_config.py).
#   Inicializa el logger nativo de Python para la persistencia de eventos.
# FECHA: 3 de Octubre de 2026
# MÓDULO: Módulo 8 - Proyecto 2 (Integrador Fase 2)
# ==============================================================================

import logging


# ==============================================================================
# CONFIGURACIÓN Y OBTENCIÓN DEL LOGGER
# ==============================================================================

def obtener_logger():
    """
    Configura y retorna la instancia del registrador (logger) para la aplicación.
    Guarda los eventos en 'app.log' con nivel mínimo INFO.
    """
    logging.basicConfig(
        filename='app.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)
    return logger