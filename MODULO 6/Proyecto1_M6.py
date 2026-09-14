# ==============================================================================
# PROYECTO: Generador de Perfiles de Usuario
# ==============================================================================
# DESCRIPCIÓN:
#   Sistema modular de validación, construcción y clasificación de perfiles.
#   Diseñado para procesar datos de entrada, aplicar reglas de negocio y
#   generar un perfil estructurado con segmentación automática.
# FECHA: 12 de Septiembre de 2026
# MÓDULO: 6 - Funciones, Parámetros y Ámbito de Variables
# ==============================================================================

# ==============================================================================
# ETAPA 1: VALIDACIÓN DE DATOS DE ENTRADA
# ==============================================================================

def validador(nombre, edad, correo):
    """
    Valida los datos básicos de un usuario.
    
    Args:
        nombre (str): Nombre del usuario.
        edad (str/int): Edad del usuario (puede venir como texto de input()).
        correo (str): Correo electrónico del usuario.
    
    Returns:
        tuple: (bool, str) - Indicador de validez y mensaje de estado.
    """
    if not nombre:
        return (False, "Nombre no válido")
    elif not str(edad).isdigit():
        return (False, "Edad no válida")
    elif not (1 <= int(edad) <= 120):
        return (False, "Edad no válida")
    elif "@" not in correo or "." not in correo:
        return (False, "Correo no válido")
    else:
        return (True, "Todos los datos son válidos")

# ==============================================================================
# ETAPA 2: CONSTRUCCIÓN DEL PERFIL ESTRUCTURADO
# ==============================================================================

def construir(nombre, edad=0, *intereses, **atributos):
    """
    Construye un diccionario de perfil a partir de datos variables.
    
    Args:
        nombre (str): Nombre del usuario (obligatorio).
        edad (int/str): Edad del usuario (opcional, default 0).
        *intereses: Cantidad variable de intereses del usuario.
        **atributos: Pares clave-valor para datos extra (ciudad, teléfono, etc).
    
    Returns:
        dict: Perfil estructurado con validación de edad automática.
    """
    if isinstance(edad, int):
        edad_num = edad
    elif isinstance(edad, str) and edad.isdigit():
        edad_num = int(edad)
    else:
        edad_num = 0
    
    es_edad_valida = 1 <= edad_num <= 120

    if not es_edad_valida:
        edad_num = 0
 
    return {
        "nombre": nombre,
        "edad": edad_num,
        "edad_validada": es_edad_valida,
        "intereses": intereses,
        "datos_extra": atributos
    }

# ==============================================================================
# ETAPA 3: CLASIFICACIÓN Y SEGMENTACIÓN
# ==============================================================================

def clasificador(perfil):
    """
    Clasifica un perfil según edad y nivel de actividad.
    
    Args:
        perfil (dict): Diccionario de perfil generado por construir().
    
    Returns:
        tuple: (str, str) - Categoría de edad y nivel de actividad.
    """
    categoria = None
    actividad = None
    
    if perfil["edad"] >= 60:
        categoria = "Adulto mayor"
    elif perfil["edad"] >= 26:
        categoria = "Adulto"
    elif perfil["edad"] >= 18:
        categoria = "Adulto joven"
    else:
        categoria = "Menor de edad"

    if len(perfil["intereses"]) >= 4:
        actividad = "Activo"
    elif len(perfil["intereses"]) >= 1:
        actividad = "Moderado"
    else:
        actividad = "Sedentario"
        
    return (categoria, actividad)

# ==============================================================================
# ETAPA 4: PROGRAMA PRINCIPAL / INTERFAZ DE CONSOLA
# ==============================================================================

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
correo = input("Ingrese su correo: ")

es_valido, mensaje = validador(nombre, edad, correo)

if not es_valido:
    print(f"Error: {mensaje}")
    exit()

interes1 = input("Primer interés: ")
interes2 = input("Segundo interés: ")
interes3 = input("Tercer interés: ")

lista_intereses = []
lista_intereses.append(interes1)
lista_intereses.append(interes2)
lista_intereses.append(interes3)

ciudad = input("Ciudad: ")
telefono = input("Teléfono: ")

perfil = construir(nombre, edad, *lista_intereses, ciudad=ciudad, telefono=telefono)

categoria, actividad = clasificador(perfil)

print("--- Perfil Generado ---")
print(f"Nombre: {perfil['nombre']}")
print(f"Edad: {perfil['edad']}")
print(f"Categoría: {categoria}")
print(f"Nivel de Actividad: {actividad}")