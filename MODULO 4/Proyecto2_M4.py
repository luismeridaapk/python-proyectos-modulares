# =============================================================================
# PROYECTO: StudentGradeAnalyzer - Analizador de Calificaciones Académicas
# DESCRIPCIÓN: 
#   Herramienta de consola que gestiona notas de estudiantes, calcula estadísticas
#   (promedio, máximo, mínimo) y determina el rendimiento académico.
#   Implementa lógica manual sin usar funciones nativas sum(), max(), min().
# FECHA: 28 de Agosto de 2026
# MÓDULO: 4 - Fundamentos de Programación e Lógica Imperativa
# =============================================================================

# --- Configuración Inicial ---
LIMITE_NOTAS = 10
contador_notas = 0
suma_acumulada = 0
lista_notas = []
contador_aprobados = 0
contador_reprobados = 0

# =============================================================================
# ETAPA 1: ENTRADA DE DATOS
# =============================================================================
# Bucle para solicitar notas al usuario hasta alcanzar el límite o recibir "0"
while contador_notas < LIMITE_NOTAS:
    entrada_usuario = input(f"Ingrese una nota (0 a {LIMITE_NOTAS} máx. | '0' para terminar): ")
    
    # Verificar condición de salida
    if entrada_usuario == "0" or entrada_usuario == "":
        break
    
    # Validar que la entrada sea un número entero
    if entrada_usuario.isdigit():
        nota = int(entrada_usuario)
        lista_notas.append(nota)
        suma_acumulada += nota
        contador_notas += 1
    else:
        print("Entrada inválida. Por favor ingrese un número entero.")

# =============================================================================
# ETAPA 2: VALIDACIÓN DE DATOS
# =============================================================================
# Verificar si se ingresaron al menos una nota para evitar errores de división
if len(lista_notas) == 0:
    print("No se ingresaron notas. No se puede generar el reporte.")
    exit()

# =============================================================================
# ETAPA 3: PROCESAMIENTO DE DATOS
# =============================================================================
# Inicializar variables para encontrar el valor máximo y mínimo
# Se asume que la primera nota es tanto la más alta como la más baja inicialmente
nota_maxima = lista_notas[0]
nota_minima = lista_notas[0]

# Recorrer la lista para encontrar el valor más alto y más bajo manualmente
for indice in range(len(lista_notas)):
    nota_actual = lista_notas[indice]
    
    if nota_actual > nota_maxima:
        nota_maxima = nota_actual
    
    if nota_actual < nota_minima:
        nota_minima = nota_actual

# Recorrer la lista para contar aprobados (>= 6.0) y reprobados
for nota in lista_notas:
    if nota >= 6:
        contador_aprobados += 1
    else:
        contador_reprobados += 1

# Calcular el promedio manualmente
promedio = suma_acumulada / contador_notas

# Determinar la calificación cualitativa basada en el promedio
if promedio >= 9:
    calificacion_cualitativa = "Excelente"
elif promedio >= 7:
    calificacion_cualitativa = "Bien"
elif promedio >= 6:
    calificacion_cualitativa = "Necesita mejorar"
else:
    calificacion_cualitativa = "Reprobado"

# =============================================================================
# ETAPA 4: SALIDA DE RESULTADOS (REPORTE)
# =============================================================================

print("--------REPORTE DE CALIFICACIONES--------")
print(f"Total de notas ingresadas: {contador_notas}")
print(f"Promedio general: {promedio:.1f}")
print(f"Nota más alta: {nota_maxima} | Nota más baja: {nota_minima}")
print(f"Aprobados: {contador_aprobados} | Reprobados: {contador_reprobados}")
print(f"Calificación Final: {calificacion_cualitativa} ({promedio:.1f})")