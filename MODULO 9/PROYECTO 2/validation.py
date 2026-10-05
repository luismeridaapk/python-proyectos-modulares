# ==============================================================================
# PROYECTO: Sistema de Gestión de Inventario para Tienda Pequeña
# ==============================================================================
# DESCRIPCIÓN:
#   Módulo de validación de entradas (validation.py). Centraliza la captura y
#   saneamiento de datos ingresados por el usuario mediante bucles de reintentos.
#   Garantiza integridad de tipos (str, int, float) y reglas de negocio básicas
#   (valores positivos) antes de que los datos lleguen a las capas de lógica.
# FECHA: 4 de Octubre de 2026
# MÓDULO: Módulo 9 - Proyecto 2 (POO Aplicada)
# ==============================================================================


# ==============================================================================
# VALIDADORES DE TIPOS NATIVOS
# ==============================================================================

# --------------------------------------------------------------------------
# CAPTURA DE TEXTO NO VACÍO: Normaliza espacios y rechaza cadenas vacías
# --------------------------------------------------------------------------
def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error: el campo no puede quedar vacío.")

# --------------------------------------------------------------------------
# CAPTURA DE ENTERO SEGURO: Bloquea conversiones inválidas con try-except
# --------------------------------------------------------------------------
def validar_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: debes escribir un número entero válido.")

# --------------------------------------------------------------------------
# CAPTURA DE FLOTANTE SEGURO: Manejo robusto de decimales
# --------------------------------------------------------------------------
def validar_flotante(mensaje):
    while True:
        try:
            flotante = float(input(mensaje))
            return flotante
        except ValueError:
            print("Error: debes escribir un número decimal válido.")


# ==============================================================================
# VALIDADORES DE REGLAS DE NEGOCIO (REUTILIZACIÓN DE FUNCIONES BASE)
# ==============================================================================

# --------------------------------------------------------------------------
# MONTO ECONÓMICO: Delega en validar_flotante y exige valor estrictamente > 0
# --------------------------------------------------------------------------
def validar_precio(mensaje):
    while True:
        precio = validar_flotante(mensaje)
        if precio > 0:
            return precio
        print("Error: el precio debe ser mayor a cero.")

# --------------------------------------------------------------------------
# UNIDADES DE STOCK/VENTA: Delega en validar_entero y exige cantidad > 0
# --------------------------------------------------------------------------
def validar_cantidad(mensaje):
    while True:
        cantidad = validar_entero(mensaje)
        if cantidad > 0:
            return cantidad
        print("Error: la cantidad debe ser mayor a cero.")