# ==============================================================================
# PROYECTO: Sistema de Gestión de Inventario para Tienda Pequeña
# ==============================================================================
# DESCRIPCIÓN:
#   Módulo de analítica y reportes (analytics.py). Provee funciones de agregación,
#   filtrado y resumen sobre la colección de productos. Utiliza comprensiones de
#   listas, generadores y métodos nativos de diccionarios para calcular métricas
#   clave del inventario sin modificar el estado original.
# FECHA: 4 de Octubre de 2026
# MÓDULO: Módulo 9 - Proyecto 2 (POO Aplicada)
# ==============================================================================


# ==============================================================================
# MÉTRICAS AGREGADAS DEL INVENTARIO
# ==============================================================================

# --------------------------------------------------------------------------
# CONTEO TOTAL: Cantidad absoluta de artículos registrados
# --------------------------------------------------------------------------
def total_productos(inventario):
    return len(inventario.productos)

# --------------------------------------------------------------------------
# VALUACIÓN ECONÓMICA: Suma del valor de mercado de todo el stock disponible
# --------------------------------------------------------------------------
def valor_total_inventario(inventario):
    return sum(p.precio * p.stock for p in inventario.productos)


# ==============================================================================
# FILTRADO Y AGRUPAMIENTO DE DATOS
# ==============================================================================

# --------------------------------------------------------------------------
# ALERTA DE REPOSICIÓN: Identifica artículos por debajo del umbral crítico
# --------------------------------------------------------------------------
def productos_stock_bajo(inventario, limite=5):
    productos_bajos = [producto for producto in inventario.productos
                       if producto.stock <= limite]
    return productos_bajos

# --------------------------------------------------------------------------
# DISTRIBUCIÓN CATEGÓRICA: Agrupa y cuenta artículos por tipo de categoría
# --------------------------------------------------------------------------
def productos_por_categoria(inventario):
    conteo = {}
    for producto in inventario.productos:
        conteo[producto.categoria] = conteo.get(producto.categoria, 0) + 1
    return conteo


# ==============================================================================
# ENSAMBLAJE E IMPRESIÓN DEL REPORTE EJECUTIVO
# ==============================================================================

def generar_reporte_completo(inventario):
    # --------------------------------------------------------------------------
    # OBTENCIÓN DE MÉTRICAS: Delegación en las funciones de análisis base
    # --------------------------------------------------------------------------
    total = total_productos(inventario)
    valor_total = valor_total_inventario(inventario)
    productos_bajos = productos_stock_bajo(inventario)
    categorias = productos_por_categoria(inventario)

    # --------------------------------------------------------------------------
    # RESUMEN GENERAL: Encabezado y cifras macroeconómicas
    # --------------------------------------------------------------------------
    print("=== REPORTE DEL INVENTARIO ===")
    print(f"Total de productos: {total}")
    print(f"Valor total: {valor_total:.2f}")

    # --------------------------------------------------------------------------
    # SECCIÓN DE ALERTAS: Listado de artículos con existencias críticas
    # --------------------------------------------------------------------------
    if productos_bajos:
        for producto in productos_bajos:
            print(f"{producto.codigo} {producto.nombre} Stock: {producto.stock}")
    else:
        print("No hay productos con stock bajo.")

    print("-" * 20)

    # --------------------------------------------------------------------------
    # DESGLOSE POR CATEGORÍA: Distribución cuantitativa de los artículos
    # --------------------------------------------------------------------------
    for categoria, cantidad in categorias.items():
        print(f"{categoria}, {cantidad} productos.")

    print("=" * 30)