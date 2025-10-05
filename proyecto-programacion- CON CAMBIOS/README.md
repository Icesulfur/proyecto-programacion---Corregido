# SISTEMA DE GESTIÓN DE BIBLIOTECA

## Programación I - Proyecto Integrador

---

**UNIVERSIDAD ARGENTINA DE LA EMPRESA (UADE)**  
**Materia:** Programación I  
**Profesor:** ABEL ISRAEL LAIME HUANCA  
**Grupo:** 5

---

## INTEGRANTES DEL EQUIPO

| **Apellido y Nombre** | **Rol** |
|----------------------|---------|
| **TASSONE, FACUNDO JAVIER** | Líder de Proyecto + Menú Principal |
| **LEE, HYO LIN** | Especialista en Persistencia de Datos |
| **IGLESIAS, MARTIN DAMIAN** | Desarrollador Módulo Libros |
| **KIDYBA, LAUTARO AGUSTIN** | Desarrollador Módulo Préstamos |
| **MILITELLO, LUCA SANTINO** | Desarrollador Módulo Usuarios |

---

## ÍNDICE

1. [**Idea General del Proyecto**](#1-idea-general-del-proyecto)
2. [**Definición de Roles del Equipo**](#2-definición-de-roles-del-equipo)
3. [**Primer Boceto del Menú Principal**](#3-primer-boceto-del-menú-principal)
4. [**Ejemplo Inicial de Entrada/Salida por Consola**](#4-ejemplo-inicial-de-entradasalida-por-consola)
5. [**Estructura Técnica Inicial**](#5-estructura-técnica-inicial)
6. [**Actualizaciones del Proyecto**](#6-actualizaciones-del-proyecto)

---

## 1. IDEA GENERAL DEL PROYECTO

### **Nombre del Proyecto**
Sistema de Gestión de Biblioteca

### **Descripción del Proyecto**
Desarrollo de una aplicación de consola en Python que simule las operaciones básicas de una biblioteca. El sistema permitirá gestionar libros, usuarios y préstamos de manera sencilla e intuitiva.

### **Objetivo**
Crear un sistema funcional que permita:
- **Gestión de Libros**: Agregar, buscar, modificar y eliminar libros del catálogo
- **Gestión de Usuarios**: Registrar socios, mantener sus datos actualizados
- **Sistema de Préstamos**: Controlar préstamos y devoluciones de libros

### **Alcance**
- **Lenguaje**: Python
- **Interfaz**: Consola/Terminal
- **Persistencia**: Archivos JSON
- **Tipo de aplicación**: Standalone (sin base de datos)

---

## 2. DEFINICIÓN DE ROLES DEL EQUIPO

| **Integrante** | **Rol** | **Responsabilidades Principales** |
|----------------|---------|-----------------------------------|
| TASSONE, FACUNDO JAVIER | **Líder de Proyecto + Menú Principal** | Coordinación del equipo, seguimiento del cronograma, implementación del menú principal y sistema de navegación |
| IGLESIAS, MARTIN DAMIAN | **Especialista en Persistencia de Datos** | Diseño de la estructura de datos, implementación de la persistencia en archivos JSON, funciones de carga y guardado |
| MILITELLO, LUCA SANTINO | **Desarrollador Módulo Libros** | CRUD completo de libros: agregar, buscar, listar, modificar y eliminar libros del sistema |
| LEE, HYO LIN | **Desarrollador Módulo Usuarios** | CRUD completo de usuarios: registro de socios, búsqueda, actualización y gestión de usuarios |
| KIDYBA, LAUTARO AGUSTIN | **Desarrollador Módulo Préstamos** | Sistema de préstamos y devoluciones, validaciones de disponibilidad, control de fechas |

### **Coordinación entre Módulos**
- Cada desarrollador trabajará en su módulo específico
- El especialista en datos dará soporte a todos los módulos para la persistencia
- El líder coordinará la integración de todos los módulos

---

## 3. PRIMER BOCETO DEL MENÚ PRINCIPAL

### **Estructura Principal**

```
═══════════════════════════════════════
    SISTEMA DE GESTIÓN DE BIBLIOTECA
═══════════════════════════════════════

1. GESTIÓN DE LIBROS
   1.1. Agregar libro
   1.2. Buscar libro
   1.3. Listar todos los libros
   1.4. Modificar libro
   1.5. Eliminar libro
   1.6. Volver al menú principal

2. GESTIÓN DE USUARIOS
   2.1. Registrar nuevo usuario
   2.2. Buscar usuario
   2.3. Listar usuarios
   2.4. Modificar datos de usuario
   2.5. Eliminar usuario
   2.6. Volver al menú principal

3. SISTEMA DE PRÉSTAMOS
   3.1. Realizar préstamo
   3.2. Registrar devolución
   3.3. Ver préstamos activos
   3.4. Historial de préstamos
   3.5. Volver al menú principal

4. SALIR DEL SISTEMA

═══════════════════════════════════════
Seleccione una opción [1-4]: _
```

### **Flujo de Navegación**
```
INICIO → MENÚ PRINCIPAL → SUBMENÚ ESPECÍFICO → OPERACIÓN → CONFIRMACIÓN → MENÚ PRINCIPAL
```

### **Validaciones del Menú**
- Control de opciones válidas (1-4)
- Mensajes de error para entradas inválidas
- Confirmación antes de salir del sistema
- Navegación intuitiva entre módulos

---

## 4. EJEMPLO INICIAL DE ENTRADA/SALIDA POR CONSOLA

### **Ejemplo 1: Inicio del Sistema**
```
═══════════════════════════════════════
    SISTEMA DE GESTIÓN DE BIBLIOTECA
═══════════════════════════════════════
    Versión 1.0 - Grupo 5
    
Inicializando sistema...
Cargando datos de libros...
Cargando datos de usuarios...
Cargando datos de préstamos...

¡Sistema listo para usar!

Presione ENTER para continuar...
```

### **Ejemplo 2: Agregar un Libro (Módulo Libros)**
```
═══════════════════════════════════════
           AGREGAR NUEVO LIBRO
═══════════════════════════════════════

Ingrese los datos del libro:

Título: El Principito
Autor: Antoine de Saint-Exupéry  
ISBN: 978-84-376-0494-7
Año de publicación: 1943
Género: Literatura infantil
Cantidad de ejemplares: 5

──────────────────────────────────────
CONFIRMACIÓN DE DATOS:
──────────────────────────────────────
Título: El Principito
Autor: Antoine de Saint-Exupéry
ISBN: 978-84-376-0494-7
Año: 1943
Género: Literatura infantil
Ejemplares: 5
──────────────────────────────────────

¿Los datos son correctos? (s/n): s

¡Libro agregado exitosamente!
ID asignado: LIB001
  
Presione ENTER para continuar...
```

### **Ejemplo 3: Realizar Préstamo (Módulo Préstamos)**
```
═══════════════════════════════════════
          REALIZAR PRÉSTAMO
═══════════════════════════════════════

Paso 1: Identificar al usuario
DNI del usuario: 12345678

Usuario encontrado:
  Nombre: Juan Pérez
  DNI: 12345678
  Estado: Activo

Paso 2: Seleccionar libro
ID del libro: LIB001

Libro encontrado:
  Título: El Principito
  Autor: Antoine de Saint-Exupéry
  Disponibles: 4 de 5

──────────────────────────────────────
RESUMEN DEL PRÉSTAMO:
──────────────────────────────────────
Usuario: Juan Pérez (DNI: 12345678)
Libro: El Principito
Fecha de préstamo: 22/09/2025
Fecha de devolución: 06/10/2025 (14 días)
──────────────────────────────────────

¿Confirma el préstamo? (s/n): s

¡Préstamo registrado exitosamente!
  Código: PREST001
  
El libro debe devolverse antes del: 06/10/2025

Presione ENTER para continuar...
```

### **Ejemplo 4: Manejo de Errores**
```
═══════════════════════════════════════
           BUSCAR LIBRO
═══════════════════════════════════════

Ingrese el título a buscar: 
Error: El título no puede estar vacío.

Ingrese el título a buscar: python
Buscando libros con título "python"...

No se encontraron libros con ese título.

¿Desea realizar otra búsqueda? (s/n): n

Regresando al menú principal...
```

---

## 5. ESTRUCTURA TÉCNICA INICIAL

### **Archivos del Proyecto**
```
sistema-biblioteca/
├── main.py                    # Archivo principal con menú
├── modulos/
│   ├── gestion_libros.py     # Módulo de libros
│   ├── gestion_usuarios.py   # Módulo de usuarios  
│   ├── gestion_prestamos.py  # Módulo de préstamos
│   └── persistencia.py       # Manejo de archivos JSON
├── datos/
│   ├── libros.json          # Datos de libros
│   ├── usuarios.json        # Datos de usuarios
│   └── prestamos.json       # Datos de préstamos
└── utilidades.py            # Funciones auxiliares
```

### **Tecnologías a Utilizar**
- **Python 3.x**: Lenguaje principal
- **JSON**: Formato de persistencia de datos
- **Librerías estándar**: `datetime`, `json`, `os`

### **Estructura de Datos (JSON)**

**Libro:**
```json
{
  "id": "LIB001",
  "titulo": "El Principito",
  "autor": "Antoine de Saint-Exupéry",
  "isbn": "978-84-376-0494-7",
  "año": 1943,
  "genero": "Literatura infantil", 
  "total_ejemplares": 5,
  "ejemplares_disponibles": 4
}
```

**Usuario:**
```json
{
  "dni": "12345678",
  "nombre": "Juan",
  "apellido": "Pérez", 
  "email": "juan.perez@email.com",
  "telefono": "1234567890",
  "fecha_registro": "22/09/2025",
  "activo": true
}
```

**Préstamo:**
```json
{
  "codigo": "PREST001",
  "usuario_dni": "12345678",
  "libro_id": "LIB001", 
  "fecha_prestamo": "22/09/2025",
  "fecha_devolucion_esperada": "06/10/2025",
  "fecha_devolucion_real": null,
  "estado": "activo"
}
```

---

## 6. ACTUALIZACIONES DEL PROYECTO

### **ENTREGA 2 - Implementación (04/10/2025)**

#### **Código Implementado:**
- **main.py**: Sistema de menú principal funcional con navegación completa
- **Módulos operativos**: Cada módulo (libros, usuarios, préstamos) con funcionalidades básicas implementadas
- **Sistema de utilidades**: Funciones auxiliares para limpieza de pantalla y pausa

#### **Funcionalidades Activas:**
- **Gestión de Libros**: Agregar y listar libros con almacenamiento en memoria
- **Gestión de Usuarios**: Registrar y listar usuarios con datos básicos (nombre, apellido, DNI)  
- **Sistema de Préstamos**: Crear y listar préstamos con ID automático y estado
- **Navegación completa**: Menús y submenús completamente funcionales

#### **Estructura de Datos Implementada:**
```python
# Listas en memoria para almacenamiento temporal
libros = []      # Diccionarios con id, titulo, autor
usuarios = []    # Diccionarios con nombre, apellido, dni  
prestamos = []   # Diccionarios con id, usuario_dni, libro_titulo, estado
```

#### **Validaciones Implementadas:**
- Control de opciones válidas en todos los menús
- Manejo de errores de entrada del usuario
- Navegación segura entre módulos

#### **Estado Actual del Proyecto:**
- Menú funcionando con opciones básicas
- Estructura de directorios del proyecto  
- Funciones principales esbozadas
- Uso de listas y cadenas (strings)

### **Próximos Pasos (Entrega 3):**
- Desarrollo de estructura de datos completa
- Implementar persistencia real con archivos JSON
- Agregar validaciones más robustas  
- Funciones de búsqueda y modificación
- Integración completa entre módulos
- Sistema de préstamos con validación de disponibilidad

