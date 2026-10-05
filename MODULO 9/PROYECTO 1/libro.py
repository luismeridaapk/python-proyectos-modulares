# ==============================================================================
# PROYECTO: Sistema Modular de Gestión de Biblioteca (POO)
# ==============================================================================
# DESCRIPCIÓN:
#   Clase modelo base (libro.py) que representa la entidad Libro.
#   Demuestra el uso de atributos de clase/instancia, constructor __init__,
#   métodos de modificación de estado y representación con __str__ y __repr__.
# FECHA: 4 de Octubre de 2026
# MÓDULO: Módulo 9 - Proyecto 1 (POO Base)
# ==============================================================================

class Libro:
    total_libros_creados = 0

    def __init__(self, isbn: str, titulo: str, autor: str, precio: float):
        # Atributos de Instancia
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.precio = float(precio)
        self.disponible = True
        
        Libro.total_libros_creados += 1

    def prestar(self) -> bool:
        """Cambia el estado del libro a no disponible si está disponible."""
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self) -> bool:
        """Restaura la disponibilidad del libro."""
        if not self.disponible:
            self.disponible = True
            return True
        return False

    def aplicar_descuento(self, porcentaje: float) -> float:
        """
        Aplica un porcentaje de descuento directamente al atributo precio
        y retorna el nuevo monto.
        """
        if 0 < porcentaje <= 100:
            monto_descuento = self.precio * (porcentaje / 100)
            self.precio -= monto_descuento
        return self.precio

    def __str__(self) -> str:
        """Representación amigable para el usuario final."""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[{self.isbn}] '{self.titulo}' - {self.autor} (${self.precio:.2f}) [{estado}]"

    def __repr__(self) -> str:
        """Representación técnica e inambigua para desarrollo/debugging."""
        return f"Libro(isbn='{self.isbn}', titulo='{self.titulo}', precio={self.precio:.2f})" 