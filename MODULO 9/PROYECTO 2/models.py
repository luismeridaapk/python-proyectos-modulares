# ==============================================================================
# PROYECTO: Sistema de Gestión de Inventario para Tienda Pequeña
# ==============================================================================
# DESCRIPCIÓN:
#   Módulo de modelos (models.py). Define las clases base del dominio:
#   Producto (artículo individual), Inventario (colección y búsqueda) y
#   Venta (registro transaccional con cálculo de totales).
# FECHA: 4 de Octubre de 2026
# MÓDULO: Módulo 9 - Proyecto 2 (POO Aplicada)
# ==============================================================================


# ==============================================================================
# CLASE PRODUCTO: REPRESENTA UN ARTÍCULO INDIVIDUAL DEL INVENTARIO
# ==============================================================================

class Producto:
    # --------------------------------------------------------------------------
    # CONSTRUCTOR: Inicializa los atributos del producto
    # --------------------------------------------------------------------------
    def __init__(self, codigo, nombre, precio, stock, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    # --------------------------------------------------------------------------
    # REPRESENTACIÓN AMIGABLE PARA EL USUARIO FINAL
    # --------------------------------------------------------------------------
    def __str__(self):
        return (f"{self.codigo}, producto: {self.nombre}, "
                f"precio: {self.precio}, stock: {self.stock}, "
                f"categoria: {self.categoria}")

    # --------------------------------------------------------------------------
    # REPRESENTACIÓN TÉCNICA / NO AMBIGUA DEL OBJETO
    # --------------------------------------------------------------------------
    def __repr__(self):
        return (f"Producto(codigo={self.codigo}, nombre={self.nombre}, "
                f"precio={self.precio}, stock={self.stock}, "
                f"categoria={self.categoria})")

    # --------------------------------------------------------------------------
    # VALIDADOR DE DISPONIBILIDAD: Indica si hay unidades disponibles
    # --------------------------------------------------------------------------
    def tiene_stock(self):
        return self.stock > 0


# ==============================================================================
# CLASE INVENTARIO: GESTIÓN CENTRAL DE LA COLECCIÓN DE PRODUCTOS
# ==============================================================================

class Inventario:
    # --------------------------------------------------------------------------
    # CONSTRUCTOR: Crea una colección vacía de productos
    # --------------------------------------------------------------------------
    def __init__(self):
        self.productos = []

    # --------------------------------------------------------------------------
    # ALTA DE PRODUCTOS: Incorpora un objeto Producto a la colección
    # --------------------------------------------------------------------------
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # --------------------------------------------------------------------------
    # BAJA DE PRODUCTOS: Elimina por código usando búsqueda lineal manual
    # --------------------------------------------------------------------------
    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                self.productos.remove(producto)
                return f"Producto {producto.nombre} eliminado con exito"
        return "Producto no encontrado"

    # --------------------------------------------------------------------------
    # BÚSQUEDA POR IDENTIFICADOR ÚNICO: Retorna el objeto o None
    # --------------------------------------------------------------------------
    def buscar_por_codigo(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    # --------------------------------------------------------------------------
    # FILTRADO POR CATEGORÍA: Retorna lista de coincidencias (comprehension)
    # --------------------------------------------------------------------------
    def buscar_por_categoria(self, categoria):
        coincidencias = [producto for producto in self.productos
                         if producto.categoria == categoria]
        return coincidencias


# ==============================================================================
# CLASE VENTA: REGISTRO TRANSACCIONAL Y CÁLCULO DE TOTAL A PAGAR
# ==============================================================================

class Venta:
    # --------------------------------------------------------------------------
    # CONSTRUCTOR: Captura los datos de la transacción de venta
    # --------------------------------------------------------------------------
    def __init__(self, codigo_producto, nombre_producto, cantidad, precio_unitario):
        self.codigo = codigo_producto
        self.nombre_producto = nombre_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    # --------------------------------------------------------------------------
    # CÁLCULO DE MONTO TOTAL: Cantidad por precio unitario
    # --------------------------------------------------------------------------
    def total(self):
        return self.precio_unitario * self.cantidad

    # --------------------------------------------------------------------------
    # REPRESENTACIÓN DEL TICKET DE VENTA
    # --------------------------------------------------------------------------
    def __str__(self):
        return (f"Venta: {self.nombre_producto}, {self.cantidad} piezas x "
                f"{self.precio_unitario:.2f}, total a pagar {self.total():.2f}")