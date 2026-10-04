# ==============================================================================
# PROYECTO: Sistema Integrado de Auditoría y Métricas Financieras (FinancialTracker)
# ==============================================================================
# DESCRIPCIÓN:
#   Script principal de orquestación e interfaz de línea de comandos (Proyecto2_M8.py).
#   Integra la carga de datos en memoria, consulta de categorías, cálculo de métricas,
#   captura interactiva de transacciones y exportación de reportes JSON.
# FECHA: 3 de Octubre de 2026
# MÓDULO: Módulo 8 - Proyecto 2 (Integrador Fase 2)
# ==============================================================================

from logger_config import obtener_logger
from core_analytics import (
    cargar_transacciones,
    calcular_metricas,
    obtener_categorias_unicas,
    exportar_reporte_json
)
# ==============================================================================
# CONFIGURACIÓN DE RUTAS Y CARGA INICIAL EN MEMORIA
# ==============================================================================

logger = obtener_logger()
logger.info("Sesión iniciada en FinancialTracker")

# Definición de rutas relativas
ruta_archivo = "MODULO 8/PROYECTO 2/datos/transacciones.txt"
ruta_salida = "MODULO 8/PROYECTO 2/datos/reporte_consolidado.json"

# Carga e inicialización de transacciones al arrancar el programa
transacciones = cargar_transacciones(ruta_archivo, logger)


# ==============================================================================
# BUCLE PRINCIPAL / MENÚ INTERACTIVO (CLI)
# ==============================================================================

while True:
    print("\n" + "="*50)
    print("  SISTEMA INTEGRADO DE MÉTRICAS FINANCIERAS")
    print("="*50)
    print("1.- Ver catálogo completo de transacciones")
    print("2.- Registrar nueva transacción")
    print("3.- Consultar categorías únicas")
    print("4.- Ver métricas financieras (Ingresos, Egresos, Balance)")
    print("5.- Guardar cambios y exportar reporte JSON (Salir)")
    print("="*50)

    try:
        opcion = input("Elija una opción (1-5): ").strip()

        # ----------------------------------------------------------------------
        # OPCIÓN 1: Visualización del catálogo en memoria
        # ----------------------------------------------------------------------
        if opcion == "1":
            print("--- CATÁLOGO DE TRANSACCIONES ---")
            if transacciones:
                for t in transacciones:
                    print(f"ID: {t['id']} | Fecha: {t['fecha']} | Cat: {t['categoria']} | Monto: ${t['monto']:.2f} | Tipo: {t['tipo']}")
            else:
                print("No hay transacciones registradas o válidas.")

        # ----------------------------------------------------------------------
        # OPCIÓN 2: Registro de nueva transacción y persistencia en .txt
        # ----------------------------------------------------------------------
        elif opcion == "2":
            print("--- REGISTRAR NUEVA TRANSACCIÓN ---")
            try:
                id_trans = int(input("ID (numérico): ").strip())
                fecha = input("Fecha (AAAA-MM-DD): ").strip()
                categoria = input("Categoría: ").strip().upper()
                monto = float(input("Monto: ").strip())
                tipo = input("Tipo (INGRESO/EGRESO): ").strip().upper()

                if monto <= 0 or id_trans <= 0:
                    raise ValueError("El ID y el Monto deben ser valores positivos.")
                
                if tipo not in ["INGRESO", "EGRESO"]:
                    raise ValueError("El Tipo debe ser únicamente INGRESO o EGRESO.")
                linea_nueva = f"{id_trans},{fecha},{categoria},{monto},{tipo}\n"

                with open(ruta_archivo, "a", encoding="utf-8") as archivo:
                    archivo.write(linea_nueva)
                

                transacciones.append({
                    "id": id_trans,
                    "fecha": fecha,
                    "categoria": categoria,
                    "monto": monto,
                    "tipo": tipo
                })

                print("¡Transacción registrada y guardada correctamente!")
                print(f"ID: {id_trans} | Fecha: {fecha} | Categoría: {categoria} | Monto: ${monto:.2f} | Tipo: {tipo}")
                logger.info(f"Nueva transacción registrada: ID {id_trans}")

            except ValueError as ve:
                print(f"Error en los datos ingresados: {ve}")
                logger.warning(f"Error al registrar transacción: {ve}")

        # ----------------------------------------------------------------------
        # OPCIÓN 3: Consulta de categorías únicas
        # ----------------------------------------------------------------------
        elif opcion == "3":
            unicas = obtener_categorias_unicas(transacciones)
            print("\n--- CATEGORÍAS ÚNICAS REGISTRADAS ---")
            for idx, cat in enumerate(unicas, 1):
                print(f"{idx}.- {cat}")

        # ----------------------------------------------------------------------
        # OPCIÓN 4: Despliegue de métricas acumuladas
        # ----------------------------------------------------------------------
        elif opcion == "4":
            metricas = calcular_metricas(transacciones)
            print("\n--- MÉTRICAS FINANCIERAS ---")
            print(f"Total Ingresos: ${metricas['total_ingresos']:.2f}")
            print(f"Total Egresos:  ${metricas['total_egresos']:.2f}")
            print(f"Balance Neto:   ${metricas['balance_neto']:.2f}")

        # ----------------------------------------------------------------------
        # OPCIÓN 5: Exportación del reporte final JSON y salida
        # ----------------------------------------------------------------------
        elif opcion == "5":
            metricas = calcular_metricas(transacciones)
            exportar_reporte_json(ruta_salida, transacciones, metricas, logger)
            print("Cambios exportados a JSON de forma correcta. Finalizando programa...")
            logger.info("Sesión finalizada por el usuario")
            break

        else:
            raise ValueError("Opción fuera de rango. Seleccione un número entre 1 y 5.")

    # --------------------------------------------------------------------------
    # MANEJO GLOBAL DE EXCEPCIONES
    # --------------------------------------------------------------------------
    except ValueError as ve:
        print(f"\nError: {ve}")
        logger.warning(ve)

    except KeyboardInterrupt:
        print("\n\nEjecución interrumpida por el usuario. Saliendo...")
        break

    finally:
        print("-" * 50)