# **Sistema Gestor para Bibliotecas**

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![CLI](https://img.shields.io/badge/Interface-CLI-green.svg)](https://es.wikipedia.org/wiki/Interfaz_de_l%C3%ADnea_de_comandos)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MI### 🏛️ Patrón de Arquitectura

El proyecto sigue una **arquitectura en capas** para mantener la separación de responsabilidades:

#### Capas del Sistema

1. **Capa de Presentación** (`views/`)
   - Interfaces de usuario CLI
   - Gestión de entrada y salida
   - Navegación entre menús

2. **Capa de Lógica de Negocio** (`services/`)
   - Reglas de negocio de la biblioteca
   - Validaciones complejas
   - Gestión de operaciones CRUD

3. **Capa de Datos** (`models/`)
   - Definición de entidades
   - Estructura de datos
   - Métodos de serialización

4. **Capa de Persistencia** (`data/`)
   - Almacenamiento en JSON
   - Gestión de archivos
   - Backup y recuperación

### 🎯 Decisiones de Diseño Clave

#### **Separación de Responsabilidades**
- **Validaciones independientes**: Se creó un servicio separado para validaciones (`validation_and_dataManagement_service.py`) para mantener la lógica de negocio limpia
- **Servicios especializados**: Cada funcionalidad tiene su propia vista y lógica

#### **Escalabilidad**
- **CRUD completo**: Implementación de operaciones Create, Read, Update, Delete para futuras expansiones
- **Modelos extensibles**: Estructura de clases que permite agregar nuevos campos fácilmente
- **Servicios modulares**: Fácil adición de nuevas funcionalidades

#### **Experiencia de Usuario**
- **Interfaz intuitiva**: Menús numerados y navegación clara
- **Validación en tiempo real**: Feedback inmediato al usuario
- **Confirmaciones**: Prevención de errores con confirmaciones de acciones críticas

#### **Mantenibilidad**
- **Código documentado**: Comentarios y estructura clara
- **Testing integrado**: Suite de pruebas para validar funcionalidad
- **Configuración externa**: Separación de configuración del código

### 🔧 Tecnologías y Herramientas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.13.5 | Lenguaje principal |
| **Pytest** | 8.4.1 | Framework de testing |
| **JSON** | Nativo | Persistencia de datos |

### 📊 Características Técnicas

- **Persistencia**: Archivos JSON para almacenamiento ligero
- **Validación**: Sistema robusto de validación de datos
- **Error Handling**: Manejo graceful de errores
- **Testing**: Cobertura completa de pruebas unitarias

## 📞 Soporte y Contacto

- **GitHub Issues**: [Reportar problemas](https://github.com/Juan-Wills/Python_2847248/issues)
- **Documentación**: Ver este README y comentarios en el código

## 🙏 Agradecimientos

- Desarrollado como parte del curso de Python
- Inspirado en sistemas reales de gestión bibliotecaria
- Gracias a la comunidad de Python por las herramientas utilizadas


## 📋 Tabla de Contenidos

- [Características](#-características)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Funcionalidades](#-funcionalidades)
- [Testing](#-testing)
- [Arquitectura](#-arquitectura)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

## ✨ Características

- **Gestión de Libros**: CRUD completo para el inventario de libros
- **Gestión de Usuarios**: Administración de usuarios de la biblioteca
- **Sistema de Préstamos**: Control de préstamos y devoluciones
- **Gestión de Multas**: Cálculo automático y administración de multas por retrasos
- **Reportes**: Estadísticas de libros más prestados
- **Validación de Datos**: Sistema robusto de validación de entradas
- **Interfaz CLI**: Interfaz de línea de comandos intuitiva y fácil de usar
- **Persistencia de Datos**: Almacenamiento en archivos JSON

## 🚀 Instalación

### Opción 1: Clonar desde GitHub

```bash
# Clonar el repositorio
git clone https://github.com/Juan-Wills/Python_2847248.git

# Navegar al directorio del proyecto
cd Python_2847248/taller_final/Biblioteca

# Crear un entorno virtual (recomendado)
python -m venv biblioteca_env

# Activar el entorno virtual
# En Windows:
biblioteca_env\Scripts\activate
# En macOS/Linux:
source biblioteca_env/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Opción 2: Instalación con Conda

```bash
# Crear entorno desde el archivo requirements.txt
conda create --name biblioteca --file requirements.txt

# Activar el entorno
conda activate biblioteca
```

## 🎯 Uso

### Ejecutar la Aplicación

```bash
python main.py
```

### Primeros Pasos

1. **Ejecutar el programa**: Al iniciar, se mostrará el menú principal
2. **Navegar**: Use los números para seleccionar opciones
3. **Agregar datos**: Comience agregando usuarios y libros antes de crear préstamos
4. **Seguir instrucciones**: La aplicación guiará paso a paso cada proceso

### Dependencias Principales

Las dependencias se instalan automáticamente con el comando anterior:

- **pytest**: Framework de testing
- **typing_extensions**: Extensiones de tipado para Python

## 📖 Guía de Usuario

### Menú Principal

Al ejecutar el programa se mostrará el menú principal:

![img main.py menu](imgs%20MD/main%20menu.jpg)

### Opciones Disponibles

1. **Libros** - Gestión del inventario de libros
2. **Usuarios** - Administración de usuarios
3. **Préstamos y Devoluciones** - Control de préstamos
4. **Multas** - Gestión de multas y pagos

#### 📚 Gestión de Libros

![img book main menu](imgs%20MD/book%20main%20menu.jpg)

**Funcionalidades disponibles:**
- ➕ **Agregar libro**: Registrar nuevos libros en el inventario
- 🔍 **Buscar libro**: Encontrar libros por diferentes criterios
- ✏️ **Actualizar libro**: Modificar información de libros existentes
- 🗑️ **Eliminar libro**: Remover libros del sistema

#### 👥 Gestión de Usuarios

![img user main menu](imgs%20MD/user%20main%20menu.jpg)

**Funcionalidades disponibles:**
- ➕ **Agregar usuario**: Registrar nuevos usuarios
- 🔍 **Buscar usuario**: Encontrar usuarios por diferentes criterios
- ✏️ **Actualizar usuario**: Modificar información de usuarios
- 🗑️ **Eliminar usuario**: Remover usuarios del sistema

#### 📋 Gestión de Préstamos

![img loan main menu](imgs%20MD/loan%20main%20menu.jpg)

**Funcionalidades disponibles:**
- ➕ **Crear préstamo**: Registrar nuevos préstamos
- 🔍 **Consultar préstamos**: Ver historial de préstamos
- 📥 **Registrar devolución**: Procesar devoluciones de libros
- 📊 **Reporte de libros más prestados**: Estadísticas de préstamos

#### 💰 Gestión de Multas

![img fine main menu](imgs%20MD/fine%20main%20menu.jpg)

**Funcionalidades disponibles:**
- 🔍 **Consultar multas**: Ver multas pendientes y pagadas
- 💳 **Pagar multa**: Procesar pagos de multas

## 🛠️ Estructura del Proyecto

```
Biblioteca/
├── main.py                   
├── requirements.txt           
├── README.MD                 
├── data/                     
│   ├── libros.json          
│   ├── usuarios.json        
│   └── prestamos.json       
├── models/                  
│   ├── libro.py             
│   ├── usuario.py           
│   └── prestamo.py          
├── services/                
│   ├── biblioteca_service.py
│   └── validation_and_dataManagement_service.py 
├── views/                    
│   ├── view_libros.py       
│   ├── view_usuarios.py     
│   ├── view_prestamos.py    
│   └── view_multas.py       
├── tests/                   
│   ├── test_models.py       
│   ├── test_biblioteca_services.py 
│   └── test_validation_and_dataManagement_service.py
└── imgs MD/                  
```

## 📋 Funcionalidades Detalladas

### 📚 Libros y Usuarios

Debido a que la estructura de gestión de usuarios y libros es similar, se explicarán sus funcionalidades de manera conjunta.

#### ➕ Agregar Nuevo Registro

El usuario deberá completar los campos con las características del elemento (libro o usuario) que desea ingresar.

**Ejemplo - Agregar Libro:**
![img add book (filled fields)](imgs%20MD/add%20book%20(details).jpg)

**Ejemplo - Agregar Usuario:**
![img add user (filled fields)](imgs%20MD/add%20user%20(details).jpg)

**Proceso de confirmación:**
Después de completar los campos, se mostrará una vista previa y se solicitará confirmación para agregar el registro a la base de datos.

**Confirmación de Libro:**
![img add book (confirm)](imgs%20MD/add%20book%20(confirm).jpg)

**Confirmación de Usuario:**
![img add user (confirm)](imgs%20MD/add%20user%20(confirm).jpg)

> **Nota**: Si se rechaza la confirmación, el sistema regresará al menú principal.

#### 🔍 Buscar por Categoría

El usuario puede filtrar resultados por diferentes características:

**Opción "Ver Todos":** Muestra todos los registros sin filtros.

**Búsqueda de Libros (Todos):**
![img find book (all)](imgs%20MD/find%20book%20(all).jpg)

**Búsqueda de Usuarios (Todos):**
![img find user (all)](imgs%20MD/find%20user%20(all).jpg)

**Búsqueda Específica:** Para filtros específicos, ingrese la información de la categoría deseada.

**Ejemplo:** Categoría: correo, Información: jane@example.com

**Búsqueda Específica de Libro:**
![img find book (specific)](imgs%20MD/find%20book%20(specific).jpg)

**Búsqueda Específica de Usuario:**
![img find user (specific)](imgs%20MD/find%20user%20(specific).jpg)

#### ✏️ Actualizar Registro

**Proceso de actualización:**
1. Seleccionar criterio de búsqueda para localizar el elemento
2. Si hay múltiples coincidencias, se solicitará un criterio más específico (ej: ID)
3. Confirmar que el elemento mostrado es correcto

**Localizar Libro:**
![img update book (find)](imgs%20MD/update%20book%20(find).jpg)

**Localizar Usuario:**
![img update user (find)](imgs%20MD/update%20user%20(find).jpg)

**Seleccionar campo a modificar:**
![img update book (category)](imgs%20MD/update%20book%20(category).jpg)

**Actualizar información de usuario:**
![img update user (update info)](imgs%20MD/update%20user%20(update%20info).jpg)

**Confirmar cambios:**
![img update book (confirm)](imgs%20MD/update%20book%20(confirm).jpg)

![img update user (confirm)](imgs%20MD/update%20user%20(confirm).jpg)

#### 🗑️ Eliminar Registro

**Proceso:**
1. Ingresar el ID del elemento a eliminar
2. Para múltiples IDs, separarlos con comas
3. Confirmar la eliminación

**Eliminar Libro:**
![img delete book](imgs%20MD/delete%20book.jpg)

**Eliminar Usuario:**
![img delete user](imgs%20MD/delete%20user.jpg)

### 📋 Préstamos y Multas

> **Prerequisito**: Debe existir al menos un libro y un usuario registrados antes de crear préstamos.

> **Nota**: Para acceder a la sección de multas deben existir préstamos vencidos.

#### ➕ Crear Préstamo

**Requisitos del sistema:**

1. **Validación de Libro:**
   - Debe estar disponible (no prestado)
   - Confirmación de que es el libro correcto
   
   ![img add loan (book)](imgs%20MD/add%20loan%20(book).jpg)

2. **Validación de Usuario:**
   - No debe tener multas pendientes
   - Confirmación de identidad del usuario
   
   ![img add loan (user)](imgs%20MD/add%20loan%20(user).jpg)

**Vista previa del préstamo:**
![img add loan (details)](imgs%20MD/add%20loan%20(details%20-%20confirm).jpg)

> **Nota**: Si no se especifica fecha de préstamo, se usará la fecha actual.

#### 📋 Ver Registro de Préstamos

**Filtros disponibles:**
- Ver todos los préstamos
- Buscar por criterios específicos

![img find loan (all)](imgs%20MD/find%20loan%20(all).jpg)

![img find loan (specific)](imgs%20MD/find%20loan%20(spec).jpg)

#### 📥 Registrar Devolución

**Requisitos:**
- El préstamo debe estar en estado "Pendiente"

![img loan devolution](imgs%20MD/loan%20devolution.jpg)

#### 📊 Reporte de Libros Más Prestados

Genera estadísticas mostrando:
- Cada libro prestado y frecuencia
- Total de libros prestados

![img most loaned books](imgs%20MD/most%20loaned%20books.jpg)

### 💰 Gestión de Multas

#### 🔍 Ver Registro de Multas

**Opciones de búsqueda:**
- Ver todas las multas
- Buscar por ID específico

![img find fines (all)](imgs%20MD/find%20fines%20(all).jpg)

![img find fines (specific)](imgs%20MD/find%20fines%20(spec).jpg)

#### 💳 Pagar Multa

**Requisitos:**
- La multa debe tener deuda pendiente
- El monto debe ser exacto al valor de la deuda

![img pay fine](imgs%20MD/pay%20fine.jpg)

## 🧪 Testing

El proyecto incluye un conjunto completo de pruebas unitarias.

### Ejecutar Pruebas

```bash
# Ejecutar todas las pruebas
pytest tests/

# Ejecutar pruebas específicas
python tests/test_models.py
python tests/test_biblioteca_services.py
```

### Cobertura de Pruebas

- **Modelos**: Tests para clases Libro, Usuario, Prestamo
- **Servicios**: Tests para lógica de negocio
- **Validaciones**: Tests para validación de datos
