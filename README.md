# 🐍 Python: Suite de Desarrollos y Arquitectura Modular

Repositorio centralizado de soluciones de software en Python orientadas a la resolución de problemas de negocio, optimización de lógica financiera, consolidación logística de inventarios e interfaces de línea de comandos (CLI).

---

## 📁 Estructura del Repositorio

| Módulo | Proyectos | Arquitectura y Conceptos Aplicados |
| :--- | :--- | :--- |
| **MODULO 3** | `PROYECTO1_M3`<br>`PROYECTO2_M3` | • Slicing & Formateo de Cadenas (`f-strings`)<br>• Tuplas inmutables de metadatos<br>• Métodos de listas (`insert`, `append`, `extend`)<br>• Operadores ternarios y lógica condicional compuesta |
| **MODULO 4** | `Proyecto1_M4`<br>`Proyecto2_M4` | • Control de flujo imperativo (`while`, `for`, `break`)<br>• Algoritmos de análisis manual ($min$, $max$ y acumulados sin dependencias)<br>• Sanitización y validación de entradas con `.isdigit()` |
| **MODULO 5** | `Proyecto1_M5`<br>`Proyecto2_M5` | • Diccionarios anidados y acceso optimizado en $O(1)$ (`.get()`)<br>• Álgebra de conjuntos (intersecciones `&`, uniones `\|`, diferencias)<br>• Consolidación logístico-financiera multi-sede |
| **MODULO 6** | `Proyecto1_M6`<br>`Proyecto2_M6` | • Arquitectura modular basada en funciones puras<br>• Manejo de parámetros dinámicos (`*args`, `**kwargs`)<br>• Normalización de datos e interfaces interactivas continuas |
| **MODULO 7** | `Proyecto1_M7`<br>`Proyecto2_M7` | • Persistencia I/O en `.txt` y exportación a `.json`<br>• Programación funcional (`filter`, `lambda`, *list comprehensions*)<br>• Manejo de excepciones y separación de responsabilidades (I/O, Analytics, Core) |

---

## 🚀 Proyectos Destacados

### 💼 E-Commerce & Multi-Branch Inventory Manager (`MODULO 5`)
* **Descripción:** Engine CLI para la consolidación e integración de stock multi-sede en tiempo real.
* **Aspectos Técnicos:**
  * Implementación de álgebra de conjuntos (`sets`) para detección de SKUs duplicados y aislamiento de productos exclusivos por región.
  * Agregación de inventarios y valorización monetaria de catálogo con complejidad temporal de consulta $O(1)$.

### 👤 User Profile Generator & Inventory Engine (`MODULO 6`)
* **Descripción:** Suite de funciones parametrizadas y modularizadas para gestión de perfiles de usuario e inventarios en memoria.
* **Aspectos Técnicos:**
  * Retorno de tuplas de validación `(bool, mensaje)` para control de estado.
  * Empleo de `**kwargs` para inyección de metadatos extensibles.
  * Normalización de datos y arquitectura de menú interactivo para consola.

### 📊 LogAnalytics & ProjectTracker CLI (`MODULO 7`)
* **Descripción:** Sistema de procesamiento analítico de logs y gestión modular de proyectos con almacenamiento persistente.
* **Aspectos Técnicos:**
  * Manejo seguro de archivos mediante bloques `with open()` en UTF-8 y control de excepciones (`FileNotFoundError`).
  * Transformación de cadenas desestructuradas a listas de diccionarios casteados.
  * Agregaciones analíticas (horas totales/promedio), conjuntos de estados únicos (`sets`) y filtros funcionales con `filter()` y `lambda`.
  * Exportación de reportes estructurados a archivos `.json` con sangría normalizada.

---

## 🛠️ Tecnologías y Estándares
* **Lenguaje:** Python 3.x
* **Estándar de Código:** PEP 8
* **Entorno:** Visual Studio Code
* **Control de Versiones:** Git & GitHub