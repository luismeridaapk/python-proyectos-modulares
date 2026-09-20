# ==============================================================================
# PROYECTO: Sistema de Gestión y Análisis de Proyectos (ProjectTracker)
# ==============================================================================
# DESCRIPCIÓN:
#   Script principal de orquestación y flujo de control (Proyecto2_M7.py).
#   Integra la lectura/escritura de archivos (io_manager) con el procesamiento
#   analítico (analytics) mediante una interfaz interactiva de consola (CLI).
# FECHA: 20 de Septiembre de 2026
# MÓDULO: Módulo 7 - Proyecto 2 (Consolidación)
# ==============================================================================

from io_manager import cargar_tareas, guardar_tareas_txt, exportar_json
from analytics import (
    estructurar_tareas,
    obtener_estados_unicos,
    calcular_metricas_horas,
    filtrar_por_estado
)


# ==============================================================================
# CONFIGURACIÓN DE RUTAS Y CARGA INICIAL
# ==============================================================================

# Definición de rutas relativas para almacenamiento y exportación
ruta_entrada = "MODULO 7/PROYECTO 2/datos/tareas.txt" 
ruta_salida = "MODULO 7/PROYECTO 2/datos/reporte_consolidado.json"

# Carga e inicialización de datos en memoria al arrancar el programa
lineas_raw = cargar_tareas(ruta_entrada)
tareas = estructurar_tareas(lineas_raw)


# ==============================================================================
# BUCLE PRINCIPAL / MENÚ INTERACTIVO
# ==============================================================================

while True:
    print("\n" + "="*50)
    print("  SISTEMA DE GESTIÓN DE PROYECTOS (ProjectTracker)")
    print("="*50)
    print("1. Ver todas las tareas")
    print("2. Agregar una nueva tarea")
    print("3. Consultar estados únicos")
    print("4. Ver métricas de horas (Total y Promedio)")
    print("5. Guardar cambios y exportar reporte JSON (Salir)")
    print("="*50)
    
    opcion = input("Selecciona una opción (1-5): ").strip()
    
    # --------------------------------------------------------------------------
    # OPCIÓN 1: Visualización formateada de todas las tareas
    # --------------------------------------------------------------------------
    if opcion == "1":
        if tareas:
            print("\n--- LISTA DE TAREAS REGISTRADAS ---")
            for i in tareas:
                print(f"ID: {i['id']} | Tarea: {i['titulo']} | Estado: {i['estado']} | Horas: {i['horas']}")
        else:
            print("\nNo hay tareas registradas en el sistema.")

    # --------------------------------------------------------------------------
    # OPCIÓN 2: Captura y registro de una nueva tarea
    # --------------------------------------------------------------------------
    elif opcion == "2":
        print("\n--- AGREGAR NUEVA TAREA ---")
        id_nueva = int(input("Nuevo id: ").strip())
        tarea = input("Nueva tarea: ").strip()
        estado = input("Nuevo estado (PENDIENTE/EN_PROCESO/COMPLETADO): ").strip().upper()
        horas = int(input("Horas: ").strip())

        # Creación y anexado del diccionario a la estructura en memoria
        tareas.append({
            "id": id_nueva,
            "titulo": tarea,
            "estado": estado,
            "horas": horas
        })
        print("¡Tarea agregada exitosamente!")

    # --------------------------------------------------------------------------
    # OPCIÓN 3: Consulta de categorías / estados únicos
    # --------------------------------------------------------------------------
    elif opcion == "3":
        unicos = obtener_estados_unicos(tareas)
        contador = 1
        print("\n--- ESTADOS ÚNICOS REGISTRADOS ---")
        for i in unicos:
            print(f"{contador}.- {i}")
            contador += 1

    # --------------------------------------------------------------------------
    # OPCIÓN 4: Cálculo y despliegue de métricas acumuladas
    # --------------------------------------------------------------------------
    elif opcion == "4":
        total, promedio = calcular_metricas_horas(tareas)
        print("\n--- MÉTRICAS DE HORAS ---")
        print(f"Total: {total} | Promedio: {promedio:.2f}")

    # --------------------------------------------------------------------------
    # OPCIÓN 5: Persistencia de cambios, exportación JSON y salida
    # --------------------------------------------------------------------------
    elif opcion == "5":
        # Conversión de la lista de diccionarios a formato texto plano
        lineas_para_guardar = [f"{dic['id']} | {dic['titulo']} | {dic['estado']} | {dic['horas']}" for dic in tareas] 
        # Persistencia en .txt y exportación del reporte .json
        guardar_tareas_txt(ruta_entrada, lineas_para_guardar)
        exportar_json(ruta_salida, tareas)
        
        print("\nCambios guardados y documento '.json' exportado de forma correcta.")
        print("Saliendo del programa.")
        break

    # --------------------------------------------------------------------------
    # MANEJO DE OPCIONES INVÁLIDAS
    # --------------------------------------------------------------------------
    else:
        print("\nOpción no válida. Intenta de nuevo.")