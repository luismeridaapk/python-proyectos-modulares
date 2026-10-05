# ==============================================================================
# PROYECTO: Sistema Modular de Gestión de Biblioteca (POO)
# ==============================================================================
# DESCRIPCIÓN:
#   Script principal e interfaz interactiva (CLI) para gestionar la biblioteca
#   y sus libros instanciados.
# FECHA: 4 de Octubre de 2026
# MÓDULO: Módulo 9 - Proyecto 1 (Script Principal)
# ==============================================================================

from libro import Libro
from biblioteca import Biblioteca


def precargar_datos(mi_biblioteca: Biblioteca):
    """Carga inicial de libros de prueba."""
    libros_demo = [
        Libro("978-1", "Cien Años de Soledad", "Gabriel García Márquez", 18.50),
        Libro("978-2", "Don Quijote de la Mancha", "Miguel de Cervantes", 22.00),
        Libro("978-3", "1984", "George Orwell", 15.00)
    ]
    for libro in libros_demo:
        mi_biblioteca.agregar_libro(libro)


def main():
    biblioteca = Biblioteca("Biblioteca Central")
    precargar_datos(biblioteca)

    while True:
        print("\n" + "=" * 50)
        print(f"   GESTIÓN DE BIBLIOTECA - {biblioteca.nombre}")
        print("=" * 50)
        print("1. Ver catálogo de libros")
        print("2. Registrar un nuevo libro")
        print("3. Buscar libro por ISBN")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Aplicar descuento a un libro")
        print("7. Ver métricas globales (Atributo de clase)")
        print("8. Salir")
        print("-" * 50)

        opcion = input("Seleccione una opción (1-8): ").strip()

        if opcion == "1":
            print("\n--- CATÁLOGO COMPLETO ---")
            catalogo = biblioteca.listar_libros()
            if not catalogo:
                print("No hay libros registrados en el catálogo.")
            else:
                for libro in catalogo:
                    print(libro)  

        elif opcion == "2":
            print("\n--- REGISTRAR NUEVO LIBRO ---")
            isbn = input("ISBN: ").strip()
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            try:
                precio = float(input("Precio: "))
                nuevo_libro = Libro(isbn, titulo, autor, precio)
                if biblioteca.agregar_libro(nuevo_libro):
                    print("Libro registrado con éxito.")
                else:
                    print(f"Error: Ya existe un libro con el ISBN '{isbn}'.")
            except ValueError:
                print("Error: El precio debe ser un número válido.")

        elif opcion == "3":
            print("\n--- BUSCAR LIBRO ---")
            isbn = input("Ingrese el ISBN a buscar: ").strip()
            libro = biblioteca.buscar_por_isbn(isbn)
            if libro:
                print(f"Encontrado: {libro}")
                print(f"  Detalle técnico (__repr__): {repr(libro)}")
            else:
                print(f"No se encontró ningún libro con ISBN '{isbn}'.")

        elif opcion == "4":
            print("\n--- PRESTAR LIBRO ---")
            isbn = input("Ingrese el ISBN del libro a prestar: ").strip()
            if biblioteca.prestar_libro(isbn):
                print("El libro se ha prestado correctamente.")
            else:
                print("No se pudo prestar (El libro no existe o ya está prestado).")

        elif opcion == "5":
            print("\n--- DEVOLVER LIBRO ---")
            isbn = input("Ingrese el ISBN del libro a devolver: ").strip()
            if biblioteca.devolver_libro(isbn):
                print("El libro ha sido devuelto con éxito.")
            else:
                print("No se pudo devolver (El libro no existe o no estaba prestado).")

        elif opcion == "6":
            print("\n--- APLICAR DESCUENTO ---")
            isbn = input("Ingrese el ISBN del libro: ").strip()
            libro = biblioteca.buscar_por_isbn(isbn)
            if libro:
                try:
                    porcentaje = float(input("Porcentaje de descuento (1-100): "))
                    nuevo_precio = libro.aplicar_descuento(porcentaje)
                    print(f"Descuento aplicado. Nuevo precio: ${nuevo_precio:.2f}")
                except ValueError:
                    print("Error: El porcentaje debe ser numérico.")
            else:
                print("Libro no encontrado.")

        elif opcion == "7":
            print("\n--- MÉTRICAS Y ESTADÍSTICAS ---")
            print(f"{biblioteca}")
            print(f"Total histórico de instancias 'Libro' creadas: {Libro.total_libros_creados}")

        elif opcion == "8":
            print("\n¡Gracias por utilizar el Sistema de Gestión de Biblioteca!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()