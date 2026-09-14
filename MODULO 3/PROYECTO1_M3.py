"""
Módulo: Generación y Validación de Credenciales de Usuario
Descripción: Recibe insumos de usuario, aplica normalización de datos 
e integra metadatos de red para la construcción de tokens.
Autor: Luis Mérida
""" 

metadatos = ("SRV_MEX", "NODE_01", "SEC_LEVEL_3", "AUTH_KEY")
nombre = input("Ingrese su nombre: ").upper()
palabra_clave = input("Ingrese su palabra clave favorita: ").upper()
numero = int(input("Digite un número entero de 4 digitos: "))


datos_usuario = [nombre, palabra_clave, numero]
datos_usuario.insert(1, metadatos[1])
datos_usuario.append("@")
caracteres_nombre = nombre[0:2]
caracteres_clave = palabra_clave[-2:]
invertido = int(str(numero)[::-1])

contraseña = f"{caracteres_nombre}{caracteres_clave}{invertido}{datos_usuario[1]}{datos_usuario[-1]}"

acceso = input("Ingrese su contraseña generada para ingresar al sistema: ").upper()
acceso_sistema = "ACCESO CONCEDIDO" if acceso == contraseña else "Acceso denegado"
print(acceso_sistema)
