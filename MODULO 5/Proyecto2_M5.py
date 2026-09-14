# =============================================================================
# PROYECTO: E-Commerce Logistics & Inventory Operations Engine
# DESCRIPCIÓN: 
#   Sistema integrado CLI para procesamiento de órdenes, análisis algebraico
#   de inventario multi-sede, auditoría algorítmica de paquetes y reporte final.
# FECHA: 06 de Septiembre de 2026
# MÓDULO: Integración Global (Semanas 1 a 5)
# =============================================================================

# =============================================================================
# ETAPA 1: PROCESAMIENTO DE ORDEN Y REGLAS FINANCIERAS
# =============================================================================

monto = float(input("Ingrese un monto de compra: "))
edad = int(input("Ingrese su edad: "))
codigo = input("Si cuenta con cupón ingreselo: ").upper()
distancia = float(input("Distancia de envío (KM): "))

descuento = 0
if codigo == "DESCUENTO10":
    descuento = monto * .10
elif codigo == "VIP20" and monto > 1000:
    descuento = monto * .20
monto_final = monto - descuento

if monto_final > 1500 or edad > 65:
    envio = 0
else:
    envio = 5 * distancia

clasificacion_cliente = "Cliente Preferencial" if monto_final > 800 else "Cliente Estándar"

print("---------------- DESGLOSE DE ORDEN ----------------")
print(f"Tipo de Cliente     : {clasificacion_cliente}")
print(f"Monto con descuento : ${monto_final:,.2f}")
print(f"Costo del envío     : ${envio:,.2f}")
print(f"Monto total a pagar : ${monto_final + envio:,.2f}")

# =============================================================================
# ETAPA 2: ANÁLISIS DE INVENTARIO MULTI-SEDE Y SELECCIÓN DE PRODUCTO
# =============================================================================

inventario_sedes = {
    "Almacen_A": {
        "SKU-100": {"nombre": "Consola Gamer", "categoria": "Videojuegos", "precio": 500.0, "stock": 10},
        "SKU-200": {"nombre": "Smart TV 55", "categoria": "Electrónica", "precio": 700.0, "stock": 5},
        "SKU-300": {"nombre": "Audífonos Noise-Cancelling", "categoria": "Audio", "precio": 150.0, "stock": 20}
    },
    "Almacen_B": {
        "SKU-200": {"nombre": "Smart TV 55", "categoria": "Electrónica", "precio": 700.0, "stock": 8},
        "SKU-400": {"nombre": "Cámara Mirrorless", "categoria": "Fotografía", "precio": 900.0, "stock": 4},
        "SKU-300": {"nombre": "Audífonos Noise-Cancelling", "categoria": "Audio", "precio": 150.0, "stock": 12}
    }
}

skus_almacen_a = set(inventario_sedes["Almacen_A"].keys())
skus_almacen_b = set(inventario_sedes["Almacen_B"].keys())
catalogo = skus_almacen_a | skus_almacen_b
ambos = skus_almacen_a.intersection(skus_almacen_b)

inventario_global = {}
for almacen, dic in inventario_sedes.items():
    for sku, valores in dic.items():
        producto_exitente = inventario_global.get(sku)
        if producto_exitente is None:
            inventario_global[sku] = {
               "nombre": valores.get("nombre"),
               "categoria" : valores.get("categoria"),
               "precio": valores.get("precio"),
               "stock_total": valores.get("stock"),
               "sedes_presentes": {almacen} 
            }
        else:
            producto_exitente["stock_total"] += valores.get("stock",0)
            producto_exitente["sedes_presentes"].add(almacen)

buscador = input("Ingrese el SKU del producto que desea adquirir con su compra: ").strip().upper()
producto = inventario_global.get(buscador)
if producto:
    print(f"--- FICHA TÉCNICA DEL PRODUCTO ---")
    print(f"Nombre           : {producto['nombre']}")
    print(f"Categoría        : {producto['categoria']}")
    print(f"Precio Unitario  : ${producto['precio']:.2f}")
    print(f"Stock Acumulado  : {producto['stock_total']} unidades")
    if producto["stock_total"] > 0:
        producto["stock_total"] -= 1
        print(f"¡Producto reservado exitosamente! Stock restante: {producto['stock_total']} unidades.")
    else:
        print("El producto seleccionado está agotado.")
else:
    print(f"[ALERTA] El SKU '{buscador}' no existe en el catálogo.")

# =============================================================================
# ETAPA 3: AUDITORÍA Y FILTRADO MANUAL DE PAQUETES DE ENVÍO
# =============================================================================

lote_paquetes = [12.5, 4.0, 25.0, 8.2, 3.5, 18.0, 2.0, 30.5, 15.0]
rango_permitido = (1.0, 20.0)
primeros_paquetes = lote_paquetes[0:5]
paquetes_validos = []
paquetes_rechazados = []
for i in lote_paquetes:
    if i >= rango_permitido[0] and i <= rango_permitido[1]:
        paquetes_validos.append(i)
    else:
        paquetes_rechazados.append(i)
contador = 0
suma = 0
maximo = paquetes_validos[0]
for i in paquetes_validos:
    contador += 1
    suma += i
    if i > maximo:
        maximo = i
promedio = suma / contador

print("---------------- BÚSQUEDA EN LOTE ----------------")
buscar_peso = float(input("Ingrese el peso exacto a buscar en el lote válido (kg): "))
for i in range(len(paquetes_validos)):
    if buscar_peso == paquetes_validos[i]:
        print(f"¡Éxito! El paquete de {buscar_peso} kg se encuentra en la posición/índice {i}.")
        break
else:
    print(f"[ALERTA] No se encontró ningún paquete con el peso de {buscar_peso} kg en la lista válida.")

# =============================================================================
# ETAPA 4: CONSOLIDADOR Y REPORTE EJECUTIVO FINAL
# =============================================================================

print("          REPORTE GENERAL DE OPERACIONES          ")
print("DATOS DE LA ORDEN FINANCIERA:")
print(f"Clasificación Cliente : {clasificacion_cliente}")
print(f"Monto Base            : ${monto:,.2f}")
print(f"Descuento Aplicado    : ${descuento:,.2f}")
print(f"Costo de Envío        : ${envio:,.2f}")
print(f"Total Final Pagado    : ${monto_final + envio:,.2f}")

print("RESERVA DE INVENTARIO:")
if producto:
    print(f"SKU Seleccionado      : {buscador}")
    print(f"Producto              : {producto['nombre']}")
    print(f"Precio Unitario       : ${producto['precio']:.2f}")
    print(f"Stock Restante        : {producto['stock_total']} unidades")
else:
    print(f"SKU Seleccionado      : {buscador} (No registrado en catálogo)")

print("RESUMEN LOGÍSTICO Y AUDITORÍA:")
print(f"Muestra (Slicing)     : {primeros_paquetes}")
print(f"Paquetes Aprobados    : {contador} unidades")
print(f"Paquetes Rechazados   : {len(paquetes_rechazados)} unidades")
print(f"Peso Total Carga      : {suma:.2f} kg")
print(f"Peso Máximo Registrado: {maximo:.2f} kg")
print(f"Peso Promedio         : {promedio:.2f} kg")
