# =============================================================================
# PROYECTO: CLI-NumberGame - Juego de Adivinanza Numérica
# DESCRIPCIÓN: Aplicación de consola donde el usuario intenta adivinar un número secreto.
# AUTOR: Luis Pedro Mérida López
# =============================================================================

# Definición del número secreto y límite de intentos
NUMERO_SECRETO = 9
intentos = 5

# Bucle principal que se ejecuta mientras queden intentos
while intentos > 0:
    # Solicita al usuario que ingrese un número entero
    # Convierte la entrada de texto a entero para comparaciones numéricas
    numero_usuario = int(input("Digite un número entero para intentar adivinar el número secreto: "))
    
    # Verifica si el usuario adivinó el número correcto
    if numero_usuario == NUMERO_SECRETO:
        print("Adivinaste el número secreto")
        break
    else:
        # Reduce el contador de intentos restantes
        intentos -= 1
        print(f"Número equivocado te quedan {intentos} intentos")
        # Si no acertó, se verifican pistas para ayudar al usuario
        if numero_usuario > NUMERO_SECRETO:
            print("'PISTA': El número secreto es más bajo")
        elif numero_usuario < NUMERO_SECRETO:
            print("'PISTA': El número secreto es más alto")
        
# Verifica si el usuario agotó todos los intentos
if intentos == 0:
    print(f"Se acabaron tus intentos | El número secreto era: {NUMERO_SECRETO}")
