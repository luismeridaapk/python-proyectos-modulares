# ==============================================================================
# PROYECTO: Sistema de Gestión de Inventario Multi-Sede
# ==============================================================================
# DESCRIPCIÓN:
#   Herramienta de consola para gestionar un inventario de productos.
#   Permite agregar productos, buscar por nombre, calcular valor total,
#   generar reportes por categoría utilizando conjuntos (sets) y
#   mantener un registro de stock en memoria.
# FECHA: 13 de Septiembre de 2026
# MÓDULO: 5-6 - Estructuras de Datos II (Diccionarios, Conjuntos) y Funciones
# ==============================================================================

# --- Configuración Inicial / Base de Datos en Memoria ---
# La lista 'inventario' almacenará diccionarios con los datos de cada producto.
inventario = []

# ==============================================================================
# ETAPA 1: GESTIÓN DE PRODUCTOS (AGREGAR Y BUSCAR)
# ==============================================================================

def agregar_producto(inventario, nombre, precio, cantidad, categoria):
    """
    Valida y agrega un nuevo producto a la lista de inventario.
    
    Args:
        inventario (list): Lista donde se guardarán los productos.
        nombre (str): Nombre del producto.
        precio (float): Precio unitario.
        cantidad (int): Cantidad en stock.
        categoria (str): Categoría del producto.
    
    Returns:
        bool: True si se agregó correctamente, False si hubo error de validación.
    """
    # Validaciones: nombre y categoría no pueden estar vacíos, precio > 0, cantidad >= 0
    if not nombre:
        return False
    elif precio <= 0:
        return False
    elif cantidad < 0:
        return False
    else: 
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
            "categoria": categoria
        }
        inventario.append(producto)
        return True 

def buscar_producto(inventario, nombre):
    """
    Busca un producto en el inventario por su nombre exacto.
    
    Args:
        inventario (list): Lista de productos.
        nombre (str): Nombre del producto a buscar.
    
    Returns:
        dict: Diccionario del producto si se encuentra, None si no.
    """
    for inv in inventario:
        if inv["nombre"] == nombre:
            return inv
    return None 

# ==============================================================================
# ETAPA 2: ANÁLISIS DE DATOS (CÁLCULOS Y REPORTES)
# ==============================================================================

def Calcular_Valor(inventario):
    """
    Calcula el valor total monetario y la cantidad total de unidades en el inventario.
    
    Args:
        inventario (list): Lista de productos.
    
    Returns:
        tuple: (total_unidades, valor_total_monetario)
    """
    acumulador = 0  # Acumulador para el valor monetario
    total = 0       # Acumulador para la cantidad de unidades
    for dic in inventario:
        acumulador += dic["precio"] * dic["cantidad"]
        total += dic["cantidad"]
    return total, acumulador

def Reporte_por_Categoría(inventario):
    """
    Genera un reporte contando cuántos productos hay por categoría.
    Utiliza conjuntos (sets) para identificar categorías únicas.
    
    Args:
        inventario (list): Lista de productos.
    
    Returns:
        dict: Diccionario con categorías como claves y conteos como valores.
    """
    categorias_unicas = set()
    reporte = {}
    for dic in inventario:
        categoria = dic["categoria"]
        if categoria not in categorias_unicas:
            categorias_unicas.add(categoria)
            reporte[categoria] = 1
        else:
            reporte[categoria] += 1
    return reporte

# ==============================================================================
# ETAPA 3: INTERFAZ DE USUARIO (MENÚ PRINCIPAL)
# ==============================================================================

def Menú_Principal(inventario):
    """
    Interfaz de consola con menú interactivo para gestionar el inventario.
    Incluye normalización de categorías a minúsculas para evitar duplicados.
    """
    while True:
        print("Agregar | 2. Buscar | 3. Valor Total | 4. Reporte | 5. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            categoria = input("Categoría: ")
            # Normalizar categoría a minúsculas para evitar duplicados (Ej: "Electrónica" == "electronica")
            categoria = categoria.lower()
            
            if agregar_producto(inventario, nombre, precio, cantidad, categoria):
                print("Producto agregado")
            else:
                print("Error de validación")

        elif opcion == "2":
            buscar = input("Buscar producto: ")
            resultado = buscar_producto(inventario, buscar)
            if resultado == None:
                print("Producto no encontrado")
            else:
                print(f"Encontrado: {resultado}")

        elif opcion == "3":
            total_unidades, valor_total = Calcular_Valor(inventario)
            print(f"Total Unidades: {total_unidades} | Valor Total: ${valor_total:.2f}")

        elif opcion == "4":
            reporte = Reporte_por_Categoría(inventario)
            print("=== Reporte por Categoría ===")
            for cat, count in reporte.items():
                print(f"   {cat.capitalize()}: {count} productos")

        elif opcion == "5":
            print("Hasta luego")
            break
        else:
            print("Opción no válida")

# --- Ejecución del Programa ---
    Menú_Principal(inventario)