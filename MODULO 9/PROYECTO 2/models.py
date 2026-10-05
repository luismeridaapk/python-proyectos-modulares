class Producto:
    def __init__(self, codigo, nombre, precio, stock, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def __str__(self):
        return f"{self.codigo}, producto: {self.nombre}, precio: {self.precio}, stock: {self.stock}, categoria: {self.categoria}"

    def __repr__(self):
        return f"Producto(codigo={self.codigo}, nombre={self.nombre}, precio={self.precio}, stock={self.stock}, categoria={self.categoria})"

    def tiene_stock(self):
        return self.stock > 0

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                self.productos.remove(producto)
                return f"Producto {producto.nombre} eliminado con exito"
        return f"Producto no encontrado"

    def buscar_por_codigo(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None
    
    def buscar_por_categoria(self, categoria):
        coincidencias = [producto for producto in self.productos if producto.categoria == categoria]
        return coincidencias

class Venta:
    def __init__(self, codigo_producto, nombre_producto, cantidad, precio_unitario):
        self.codigo = codigo_producto
        self.nombre_producto = nombre_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def total(self):
        return self.precio_unitario * self.cantidad

    def __str__(self):
        return f"Venta: {self.nombre_producto}, {self.cantidad} piezas x {self.precio_unitario:.2f}, total a pagar {self.total():.2f}"