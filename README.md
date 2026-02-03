# 🚗 Alquiler de Coches - Aplicación Python

Una aplicación de gestión de alquiler de vehículos desarrollada en Python, implementando una arquitectura de capas (Presentation, Application, Domain e Infrastructure).

## 📋 Descripción

Esta aplicación permite gestionar el alquiler y devolución de vehículos. Ofrece un sistema completo con validaciones de datos y un menú interactivo para facilitar la interacción del usuario.

## ✨ Características

- **Gestión de Vehículos**: Crear y administrar un catálogo de vehículos
- **Validación de Datos**: Validación rigurosa de matrículas y años
- **Control de Alquileres**: Marcar vehículos como alquilados o disponibles
- **Interfaz Interactiva**: Menú por consola fácil de usar
- **Arquitectura Modular**: Separación clara de capas (MVC)

## 🏗️ Arquitectura

El proyecto está estructurado siguiendo el patrón de arquitectura de capas (MVC):

```
alquiler_coches/
├── presentation/      # Capa de presentación (interfaz de usuario)
│   └── menu.py       # Menú interactivo principal
├── application/      # Capa de aplicación (repositorio de datos)
│   └── vehiculos_repository.py  # Gestión de almacenamiento de vehículos
├── domain/           # Capa de dominio (entidades y reglas de negocio)
│   ├── vehiculo.py   # Clase Vehiculo con validaciones
│   └── sucursal_a.py # Gestión de sucursales
├── services/         # Capa de servicios (lógica de negocio)
│   └── vehiculos_service.py  # Orquestación entre presentation y application
└── infraestructure/  # Capa de infraestructura (persistencia futura)
```

**Flujo de datos:**
```
Menu (Presentación) 
  ↓
VehiculosService (Servicios)
  ↓
VehiculosRepository (Aplicación)
  ↓
Vehiculo (Dominio)
```

## 🔧 Requisitos

- Python 3.7 o superior
- Ninguna dependencia externa adicional

## 🚀 Cómo usar

1. **Clonar o descargar** el proyecto
2. **Navegar** al directorio del proyecto:
   ```bash
   cd proyecto/01-capas/alquiler_coches
   ```
3. **Ejecutar** la aplicación:
   ```bash
   python -m presentation.menu
   ```

## 📝 Menú Principal

La aplicación ofrece las siguientes opciones:

1. **Listar vehículos**: Muestra todos los vehículos registrados en el sistema
2. **Buscar por matrícula**: Busca un vehículo específico por su matrícula
3. Opción 3: (En desarrollo)
4. Opción 4: (En desarrollo)
5. **Registrar vehículo**: Permite agregar un nuevo vehículo al repositorio
6. **Modificar vehículo**: Permite actualizar los datos de un vehículo existente
7. **Eliminar vehículo**: Elimina un vehículo del repositorio
8. **Salir**: Cierra la aplicación

## 🔑 Clases Principales

### Vehiculo

Representa un vehículo disponible para alquilar.

**Atributos:**
- `matricula`: Identificador único del vehículo (formato: letra+número)
- `marca`: Marca del fabricante
- `modelo`: Modelo del vehículo
- `anio`: Año de fabricación (1900-2026)
- `puertas`: Número de puertas (opcional)
- `alquilado`: Estado del alquiler (True/False)

**Métodos:**
- `alquilar()`: Marca el vehículo como alquilado
- `devolver()`: Marca el vehículo como disponible

**Validaciones:**
- La matrícula debe tener formato: letra + número
- El año debe estar entre 1900 y el año actual

### VehiculosRepository

Gestiona la persistencia y almacenamiento de vehículos en el repositorio.

**Métodos:**
- `agregar(vehiculo)`: Agrega un nuevo vehículo al repositorio (con validación de matrícula duplicada)
- `obtener_todos()`: Retorna todos los vehículos almacenados
- `buscar_por_matricula(matricula)`: Busca un vehículo específico
- `eliminar_por_matricula(matricula)`: Elimina un vehículo del repositorio

### VehiculosService

Capa de servicios que orquesta la lógica de negocio entre el repositorio y la presentación.

**Métodos:**
- `agregar_vehiculo()`: Crea un nuevo vehículo y lo agrega al repositorio con manejo de errores
- `listar_vehiculos()`: Obtiene y muestra todos los vehículos
- `buscar_vehiculo(matricula)`: Busca un vehículo por matrícula
- `eliminar_vehiculo(matricula)`: Elimina un vehículo con validación

## ⚠️ Validaciones Implementadas

- ✅ Validación de formato de matrícula
- ✅ Validación del rango de años
- ✅ Manejo de errores en la entrada del usuario
- ✅ Control de estado de vehículos (alquilado/disponible)
- ✅ Prevención de matrículas duplicadas en el repositorio
- ✅ Conversión a mayúsculas de matrículas para consistencia

## 📅 Implementación Actual

**Funcionalidades completadas:**
- ✅ **Repositorio de Vehículos**: Implementación completa con métodos CRxD (Create, Read, Delete)
- ✅ **Capa de Servicios**: Orquestación entre presentación y datos
- ✅ **Menú Interactivo**: Sistema de 8 opciones funcionales con manejo de errores
- ✅ **Gestión de Almacenamiento**: Los vehículos se guardan sin sobrescribirse (uso de diccionario con matrícula como clave)
- ✅ **Búsqueda por Matrícula**: Funcionalidad de búsqueda individual
- ✅ **Listar Todos**: Visualización completa del catálogo
- ✅ **Eliminación de Vehículos**: Opción para remover vehículos del sistema
- ✅ **Registro de Vehículos**: Formulario completo para agregar nuevos vehículos

## 📖 Ejemplo de Uso

```python
from domain.vehiculo import Vehiculo
from application.vehiculos_repository import VehiculosRepository
from services.vehiculos_service import VehiculosService

# Inicializar el servicio
repository = VehiculosRepository()
servicio = VehiculosService(repository)

# Agregar vehículos
servicio.agregar_vehiculo("A1", "Toyota", "Corolla", 2023, puertas=4)
servicio.agregar_vehiculo("B2", "Honda", "Civic", 2022, puertas=4)

# Listar todos los vehículos
servicio.listar_vehiculos()

# Buscar un vehículo específico
vehiculo = servicio.buscar_vehiculo("A1")

# Eliminar un vehículo
servicio.eliminar_vehiculo("B2")
```

## 🎯 Próximas Mejoras

- 🔲 Agregar funcionalidad de alquilar/devolver vehículos
- 🔲 Persistencia de datos en base de datos
- 🔲 Interfaz gráfica (GUI)
- 🔲 Sistema de pagos y facturación

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes, abre un issue primero para discutir los cambios propuestos.

## 📄 Licencia

Este proyecto está disponible bajo licencia libre.