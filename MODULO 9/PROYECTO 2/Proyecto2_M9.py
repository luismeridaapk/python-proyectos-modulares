# ==============================================================================
# PROYECTO: Sistema de Gestión de Inventario para Tienda Pequeña
# ==============================================================================
# DESCRIPCIÓN:
#   Script principal de orquestación e interfaz de línea de comandos (Proyecto2_M9.py).
#   Integra la carga persistente del inventario con el menú interactivo y la
#   delegación de operaciones a módulos especializados (validación, lógica,
#   analítica y almacenamiento). Garantiza la preservación de datos mediante
#   guardado automático al finalizar la sesión.
# FECHA: 4 de Octubre de 2026
# MÓDULO: Módulo 9 - Proyecto 2 (POO Aplicada)
# ==============================================================================

from models import Producto, Inventario
from validation import validar_texto, validar_entero, validar_precio, validar_cantidad
from operations import agregar_producto, registrar_venta, actualizar_stock
from analytics import generar_reporte_completo
from storage import guardar_inventario, cargar_inventario


# ==============================================================================
# INTERFAZ DE USUARIO: MENÚ DE OPCIONES PRINCIPALES
# ==============================================================================

def mostrar_menu():
    print("\n" + "="*30)
    print("       MENÚ PRINCIPAL")
    print("="*30)
    print("1. Agregar Producto")
    print("2. Registrar Venta")
    print("3. Actualizar Stock")
    print("4. Ver Productos por Categoría")
    print("5. Generar Reporte Completo")
    print("6. Guardar Inventario")
    print("7. Salir y Guardar")
    print("="*30)


# ==============================================================================
# BUCLE PRINCIPAL / ORQUESTACIÓN DE FLUJO
# ==============================================================================

def main():
    # --------------------------------------------------------------------------
    # INICIALIZACIÓN RESILIENTE: Carga historial existente o crea inventario vacío
    # --------------------------------------------------------------------------
    inventario = cargar_inventario(Inventario, Producto, "datos/inventario.json")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        # ----------------------------------------------------------------------
        # ALTA DE PRODUCTOS: Captura validada y registro en el sistema
        # ----------------------------------------------------------------------
        if opcion == "1":
            print("\n--- Agregar Producto ---")
            codigo = validar_texto("Código: ")
            nombre = validar_texto("Nombre: ")
            precio = validar_precio("Precio: ")
            stock = validar_cantidad("Stock: ")
            categoria = validar_texto("Categoría: ")

            resultado = agregar_producto(inventario, codigo, nombre, precio, stock, categoria)
            print(resultado)

        # ----------------------------------------------------------------------
        # REGISTRO DE VENTAS: Validación de existencia y deducción de stock
        # ----------------------------------------------------------------------
        elif opcion == "2":
            print("\n--- Registrar Venta ---")
            codigo = validar_texto("Código del producto: ")
            cantidad = validar_cantidad("Cantidad a vender: ")

            resultado = registrar_venta(inventario, codigo, cantidad)
            print(resultado)

        # ----------------------------------------------------------------------
        # ACTUALIZACIÓN DE STOCK: Corrección manual de existencias
        # ----------------------------------------------------------------------
        elif opcion == "3":
            print("\n--- Actualizar Stock ---")
            codigo = validar_texto("Código del producto: ")
            nueva_cantidad = validar_cantidad("Nueva cantidad en stock: ")

            resultado = actualizar_stock(inventario, codigo, nueva_cantidad)
            print(resultado)

        # ----------------------------------------------------------------------
        # FILTRADO CATEGÓRICO: Búsqueda y listado de artículos por tipo
        # ----------------------------------------------------------------------
        elif opcion == "4":
            print("\n--- Productos por Categoría ---")
            categoria = validar_texto("Categoría a buscar: ")
            productos = inventario.buscar_por_categoria(categoria)

            if productos:
                for p in productos:
                    print(p)
            else:
                print(f"No hay productos en la categoría: {categoria}")

        # ----------------------------------------------------------------------
        # ANÁLISIS Y REPORTES: Generación de resumen ejecutivo
        # ----------------------------------------------------------------------
        elif opcion == "5":
            print("\n--- Reporte ---")
            generar_reporte_completo(inventario)

        # ----------------------------------------------------------------------
        # PERSISTENCIA MANUAL: Guardado explícito sin cerrar la aplicación
        # ----------------------------------------------------------------------
        elif opcion == "6":
            guardar_inventario(inventario, "datos/inventario.json")
            print("Inventario guardado correctamente.")

        # ----------------------------------------------------------------------
        # FINALIZACIÓN DE SESIÓN: Persistencia y cierre del bucle principal
        # ----------------------------------------------------------------------
        elif opcion == "7":
            guardar_inventario(inventario, "datos/inventario.json")
            print("Saliendo del programa. Hasta luego!")
            break

        # ----------------------------------------------------------------------
        # MANEJO DE ENTRADAS INVÁLIDAS
        # ----------------------------------------------------------------------
        else:
            print("Opción inválida. Intenta de nuevo.")


# ==============================================================================
# PUNTO DE ENTRADA ESTÁNDAR DE LA APLICACIÓN
# ==============================================================================

if __name__ == "__main__":
    main()