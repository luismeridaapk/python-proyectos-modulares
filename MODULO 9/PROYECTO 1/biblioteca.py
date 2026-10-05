# ==============================================================================
# PROYECTO: Sistema Modular de Gestión de Biblioteca (POO)
# ==============================================================================
# DESCRIPCIÓN:
#   Clase contenedora y administradora (biblioteca.py) que gestiona colecciones
#   de objetos de la clase Libro (búsqueda, inserción y cambio de estados).
# FECHA: 4 de Octubre de 2026
# MÓDULO: Módulo 9 - Proyecto 1 (POO Base)
# ==============================================================================

from libro import Libro


class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.catalogo = []

    def agregar_libro(self, libro: Libro) -> bool:
        if not self.buscar_por_isbn(libro.isbn):
            self.catalogo.append(libro)
            return True
        return False

    def buscar_por_isbn(self, isbn: str):
        """Recorre el catálogo y retorna el objeto Libro si coincide el ISBN."""
        for libro in self.catalogo:
            if libro.isbn == isbn:
                return libro
        return None  

    def listar_libros(self) -> list:
        """Retorna la lista completa de libros almacenados."""
        return self.catalogo

    def prestar_libro(self, isbn: str) -> bool:
        """Busca el libro por ISBN y ejecuta su método de préstamo."""
        libro = self.buscar_por_isbn(isbn)
        if libro:
            return libro.prestar()
        return False

    def devolver_libro(self, isbn: str) -> bool:
        """Busca el libro por ISBN y ejecuta su método de devolución."""
        libro = self.buscar_por_isbn(isbn)
        if libro:
            return libro.devolver()
        return False

    def __str__(self) -> str:
        """Representación textual de la biblioteca y cantidad de libros."""
        return f"Biblioteca '{self.nombre}' | Total de títulos: {len(self.catalogo)}"