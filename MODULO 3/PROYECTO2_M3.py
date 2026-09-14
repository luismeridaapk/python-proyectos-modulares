"""
MÓDULO3: Motor de Evaluación de Licencias y Auditoría de Facturación
DESCRIPCIÓN: Sistema de procesamiento de parámetros financieros, geográficos 
y de antigüedad para la clasificación automática de cuentas, 
 generación de folios de auditoría y cálculo de descuentos.
AUTOR: Luis Mérida


"""
licencias_proveedor = ("MAX_USUARIOS_100", "USO_PERMITIDO_LATAM", "MODO_STRICT")

nombre_empresa = input("Nombre de la empresa: ").upper()
sector_industrial = input("Sector indusrtrial: ")
cantidad_usuarios = int(input("Cantidad de usuarios activos: "))
costo_mensual = float(input("Costo mensual del plan actual: $"))
años_antiguedad = int(input("Años de antiguedad como cliente: "))
region_operacion = input("Región de operación: ").upper()
cadena_años = f"0{años_antiguedad}" if años_antiguedad <10 else str(años_antiguedad)
invertidos = cadena_años[-2:][::-1]
codigo_licencia = F"{nombre_empresa[0:3]}{len(sector_industrial)}{invertidos}" 

if region_operacion == "LATAM" and años_antiguedad > 2 and 10 <= cantidad_usuarios <= 100 and costo_mensual >= 5000:
    clasificacion = "RENOVACIÓN PREMIER"
elif cantidad_usuarios < 100 and años_antiguedad >= 1:
    clasificacion = "RENOVACIÓN ESTÁNDAR"
elif cantidad_usuarios > 100:
    clasificacion = "BLOQUEO POR EXCESO"
else:
    clasificacion = "REVISIÓN MANUAL" 

factor_descuento = 15 if clasificacion == "RENOVACIÓN PREMIER" else 0
costo_final =  costo_mensual - (costo_mensual *( factor_descuento/100))

lista_auditoria = [nombre_empresa, sector_industrial, cantidad_usuarios, costo_mensual, años_antiguedad, region_operacion]
lista_auditoria.insert(0, "FOLIO-9988")
lista_auditoria.extend([codigo_licencia, clasificacion, factor_descuento, costo_mensual, costo_final])
sublista = lista_auditoria[7:9]

print(lista_auditoria)
print(sublista)