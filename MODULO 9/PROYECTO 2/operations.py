# ==============================================================================
# PROYECTO: Sistema de Gestión de Inventario para Tienda Pequeña
# ==============================================================================
# DESCRIPCIÓN:
#   Módulo de operaciones de negocio (operations.py). Contiene las funciones
#   puras que manipulan el estado del inventario: alta de productos, registro
#   de ventas con validación de stock y actualización de existencias.
#   No interactúa directamente con el usuario; recibe datos limpios y retorna
#   mensajes de resultado.
# FECHA: 4 de Octubre de 2026
# MÓDULO: Módulo 9 - Proyecto 2 (POO Aplicada)
# ==============================================================================

from models import Producto, Inventario


# ==============================================================================
# ALTA DE PRODUCTOS: CREACIÓN Y REGISTRO EN EL SISTEMA
# ==============================================================================

def agregar_producto(inventario, codigo, nombre, precio, stock, categoria):
    # --------------------------------------------------------------------------
    # INSTANCIACIÓN Y REGISTRO: Construcción del objeto y su incorporación
    # --------------------------------------------------------------------------
    producto_nuevo = Producto(codigo, nombre, precio, stock, categoria)
    inventario.agregar_producto(producto_nuevo)
    return f"Producto: {producto_nuevo.nombre} agregado correctamente al inventario"


# ==============================================================================
# REGISTRO DE VENTAS: VALIDACIÓN Y DEDUCCIÓN DE STOCK
# ==============================================================================

def registrar_venta(inventario, codigo, cantidad):
    # --------------------------------------------------------------------------
    # BÚSQUEDA DEL ARTÍCULO: Localización por código único
    # --------------------------------------------------------------------------
    codigo_encontrado = inventario.buscar_por_codigo(codigo)

    # --------------------------------------------------------------------------
    # VALIDACIONES DE NEGOCIO: Existencia y disponibilidad de stock
    # --------------------------------------------------------------------------
    if codigo_encontrado is None:
        return "Error: producto no encontrado"
    elif cantidad > codigo_encontrado.stock:
        return f"Error: stock insuficiente. Disponible: {codigo_encontrado.stock}"

    # --------------------------------------------------------------------------
    # EJECUCIÓN DE LA VENTA: Deducción de unidades y confirmación
    # --------------------------------------------------------------------------
    else:
        codigo_encontrado.stock -= cantidad
        return "Venta exitosa"


# ==============================================================================
# ACTUALIZACIÓN DE STOCK: CORRECCIÓN MANUAL DE EXISTENCIAS
# ==============================================================================

def actualizar_stock(inventario, codigo, nueva_cantidad):
    # --------------------------------------------------------------------------
    # BÚSQUEDA DEL ARTÍCULO: Localización por código único
    # --------------------------------------------------------------------------
    producto = inventario.buscar_por_codigo(codigo)

    # --------------------------------------------------------------------------
    # VALIDACIÓN Y MODIFICACIÓN: Existencia y reasignación de valor
    # --------------------------------------------------------------------------
    if producto is None:
        return "Error: producto no encontrado"
    else:
        producto.stock = nueva_cantidad
        return f"Stock de {producto.nombre} actualizado a {nueva_cantidad}"