# ==============================================================================
# PROYECTO: Sistema de Gestión de Inventario para Tienda Pequeña
# ==============================================================================
# DESCRIPCIÓN:
#   Módulo de persistencia (storage.py). Gestiona la serialización y deserialización
#   del inventario hacia/desde un archivo JSON. Implementa el patrón de conversión
#   Objeto -> Diccionario -> JSON (guardado) y JSON -> Diccionario -> Objeto (carga),
#   con manejo resiliente de archivos inexistentes mediante try-except.
# FECHA: 4 de Octubre de 2026
# MÓDULO: Módulo 9 - Proyecto 2 (POO Aplicada)
# ==============================================================================

import json
import logging


# ==============================================================================
# GUARDADO DE DATOS: SERIALIZACIÓN OBJETO -> DICT -> JSON
# ==============================================================================

def guardar_inventario(inventario, ruta_archivo):
    # --------------------------------------------------------------------------
    # CONSTRUCCIÓN DEL PAYLOAD: Transformación de objetos a estructuras nativas
    # --------------------------------------------------------------------------
    lista = []
    for producto in inventario.productos:
        diccionario = {
            "codigo": producto.codigo,
            "nombre": producto.nombre,
            "precio": producto.precio,
            "stock": producto.stock,
            "categoria": producto.categoria
        }
        lista.append(diccionario)

    # --------------------------------------------------------------------------
    # PERSISTENCIA EN DISCO: Escritura formateada con indentación legible
    # --------------------------------------------------------------------------
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4)
        logging.info("Productos guardados correctamente")


# ==============================================================================
# CARGA DE DATOS: DESERIALIZACIÓN JSON -> DICT -> OBJETO
# ==============================================================================

def cargar_inventario(InventarioClase, ProductoClase, ruta_archivo):
    try:
        # ----------------------------------------------------------------------
        # LECTURA DEL ARCHIVO: Deserialización de JSON a lista de diccionarios
        # ----------------------------------------------------------------------
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        # ----------------------------------------------------------------------
        # RECONSTRUCCIÓN DE OBJETOS: Iteración y rehidratación de entidades
        # ----------------------------------------------------------------------
        inventario = InventarioClase()
        for item in datos:
            producto = ProductoClase(
                item["codigo"],
                item["nombre"],
                item["precio"],
                item["stock"],
                item["categoria"]
            )
            inventario.agregar_producto(producto)

        logging.info("Inventario cargado correctamente")
        return inventario

    # --------------------------------------------------------------------------
    # MANEJO DE RESILIENCIA: Creación de instancia vacía si no hay historial
    # --------------------------------------------------------------------------
    except FileNotFoundError:
        logging.warning("No existe archivo previo, creando inventario nuevo")
        return InventarioClase()