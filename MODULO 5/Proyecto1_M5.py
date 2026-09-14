# =============================================================================
# PROYECTO: MultiBranchInventoryManager - Sistema de Gestión de Inventario Multi-Sede
# DESCRIPCIÓN: 
#   Herramienta de consola para consolidar datos de stock de múltiples sucursales,
#   ejecutar análisis de conjuntos sobre SKUs, realizar consultas optimizadas en
#   memoria y generar reportes de valorización e identifación de categorías.
# FECHA: 04 de Septiembre de 2026
# MÓDULO: 5 - Estructuras de Datos II (Diccionarios y Conjuntos)
# =============================================================================

# --- Configuración Inicial / Base de Datos en Memoria ---
inventario_sedes = {
    "Sede_Norte": {
        "LAP-001": {"nombre": "Laptop Pro 15", "categoria": "Electrónica", "precio": 1200.0, "stock": 15},
        "MON-002": {"nombre": "Monitor 4K 27", "categoria": "Electrónica", "precio": 350.0, "stock": 8},
        "TECL-003": {"nombre": "Teclado Mecánico", "categoria": "Accesorios", "precio": 80.0, "stock": 25},
        "RAT-004": {"nombre": "Ratón Inalámbrico", "categoria": "Accesorios", "precio": 35.0, "stock": 40}
    },
    "Sede_Sur": {
        "MON-002": {"nombre": "Monitor 4K 27", "categoria": "Electrónica", "precio": 350.0, "stock": 12},
        "TECL-003": {"nombre": "Teclado Mecánico", "categoria": "Accesorios", "precio": 80.0, "stock": 5},
        "SILL-005": {"nombre": "Silla Ergonómica", "categoria": "Mobiliario", "precio": 250.0, "stock": 10},
        "AUDI-006": {"nombre": "Audífonos Bluetooth", "categoria": "Audio", "precio": 110.0, "stock": 18}
    },
    "Sede_Centro": {
        "LAP-001": {"nombre": "Laptop Pro 15", "categoria": "Electrónica", "precio": 1200.0, "stock": 5},
        "SILL-005": {"nombre": "Silla Ergonómica", "categoria": "Mobiliario", "precio": 250.0, "stock": 3},
        "ESCR-007": {"nombre": "Escritorio Elevable", "categoria": "Mobiliario", "precio": 450.0, "stock": 7},
        "RAT-004": {"nombre": "Ratón Inalámbrico", "categoria": "Accesorios", "precio": 35.0, "stock": 15}
    }
}

# =============================================================================
# ETAPA 1: ANÁLISIS ALGEBRAICO DE CATÁLOGO (CONJUNTOS / SETS)
# =============================================================================

# Construir el catálogo único global recorriendo las sedes
catalogo_global = set()
for sede, productos in inventario_sedes.items():
    for sku in productos.keys():
        catalogo_global.add(sku)

# Extraer conjuntos independientes por sede para operaciones algebraicas
norte = set(inventario_sedes["Sede_Norte"])
sur = set(inventario_sedes["Sede_Sur"])
centro = set(inventario_sedes["Sede_Centro"])

# Operaciones de algebra de conjuntos
duplicados = (norte & sur) | (sur & centro) | (norte & centro)
exclusivos_sur = sur.difference(norte, centro)

# Extraer el conjunto de categorías únicas registradas
categorias_unicas = set()
for sede, productos in inventario_sedes.items():
    for datos in productos.values():
        categorias_unicas.add(datos["categoria"])

# =============================================================================
# ETAPA 2: AGREGACIÓN Y CONSOLIDACIÓN GLOBAL
# =============================================================================

inventario_global = {}

# Recorrer las sedes y consolidar stock y atributos por SKU
for nombre_sede, productos in inventario_sedes.items():
    for sku, datos in productos.items():
        producto_existente = inventario_global.get(sku)

        if producto_existente is None:
            inventario_global[sku] = {
                "nombre": datos.get("nombre"),
                "categoria": datos.get("categoria"),
                "precio": datos.get("precio"),
                "stock_total": datos.get("stock", 0),
                "sedes_presentes": {nombre_sede}
            }
        else:
            producto_existente["stock_total"] += datos.get("stock", 0)
            producto_existente["sedes_presentes"].add(nombre_sede)

# =============================================================================
# ETAPA 3: CONSULTAS BÚSQUEDA INTERACTIVA
# =============================================================================

print("       MÓDULO DE BÚSQUEDA DE PRODUCTO EN MEMORIA   ")

buscador = input("Ingrese el SKU del producto a consultar: ").strip().upper()

# Búsqueda óptima en O(1) usando el método .get()
producto = inventario_global.get(buscador)

if producto:
    print(f"--- FICHA TÉCNICA DEL PRODUCTO  ---")
    print(f"Nombre           : {producto['nombre']}")
    print(f"Categoría        : {producto['categoria']}")
    print(f"Precio Unitario  : ${producto['precio']:.2f}")
    print(f"Stock Acumulado  : {producto['stock_total']} unidades")
else:
    print(f"[ALERTA] El SKU '{buscador}' no se encuentra registrado en la base de datos.")

# =============================================================================
# ETAPA 4: PROCESAMIENTO Y REPORTE FINANCIERO / REPORTE DE STOCK
# =============================================================================

valor_total_empresa = 0
stock_por_categoria = {}

# Recorrer el diccionario consolidado mediante .items()
for sku, datos in inventario_global.items():
    valor_producto = datos["precio"] * datos["stock_total"]
    valor_total_empresa += valor_producto
    
    print(f"SKU: {sku:<8} | {datos['nombre']:<22} | Stock: {datos['stock_total']:<2} | Subtotal: ${valor_producto:>9.2f}")
    
    # Acumular unidades físicas por categoría
    categoria_actual = datos["categoria"]
    stock_por_categoria[categoria_actual] = stock_por_categoria.get(categoria_actual, 0) + datos["stock_total"]

# Identificar manualmente la categoría líder en unidades físicas
categoria_lider = None
max_unidades = 0

for categoria, unidades in stock_por_categoria.items():
    if unidades > max_unidades:
        max_unidades = unidades
        categoria_lider = categoria

# =============================================================================
# ETAPA 5: SALIDA DE RESULTADOS Y MÉTRICAS FINALES
# =============================================================================


print("             RESUMEN GENERAL EJECUTIVO            ")
print(f"Total de SKUs Únicos en Catálogo: {len(catalogo_global)}")
print(f"Categorías Registradas           : {', '.join(categorias_unicas)}")
print(f"SKUs Exclusivos Sede Sur         : {', '.join(exclusivos_sur)}")
print(f"Valor Monetario Total Inventario : ${valor_total_empresa:,.2f}")
print(f"Categoría con Mayor Stock Total  : {categoria_lider} ({max_unidades} unidades)")