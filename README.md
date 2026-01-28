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

El proyecto está estructurado siguiendo el patrón de arquitectura de capas:

```
alquiler_coches/
├── presentation/      # Capa de presentación (interfaz de usuario)
│   └── menu.py       # Menú interactivo
├── application/      # Capa de aplicación (lógica de negocio)
├── domain/           # Capa de dominio (entidades y reglas)
│   ├── vehiculo.py   # Clase Vehiculo
│   └── sucursal_a.py # Gestión de sucursales
└── infraestructure/  # Capa de infraestructura (persistencia)
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

1. Opción 1
2. Opción 2
3. Opción 3
4. Opción 4
5. Opción 5
6. Opción 6
7. Opción 7
8. Salir

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

## ⚠️ Validaciones Implementadas

- ✅ Validación de formato de matrícula
- ✅ Validación del rango de años
- ✅ Manejo de errores en la entrada del usuario
- ✅ Control de estado de vehículos (alquilado/disponible)

## 📖 Ejemplo de Uso

```python
from domain.vehiculo import Vehiculo

# Crear un nuevo vehículo
auto = Vehiculo("A1", "Toyota", "Corolla", 2023, puertas=4)

# Alquilar el vehículo
print(auto.alquilar())  # Vehiculo alquilado con éxito.

# Devolver el vehículo
print(auto.devolver())  # Vehiculo devuelto con éxito.
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes, abre un issue primero para discutir los cambios propuestos.

## 📄 Licencia

Este proyecto está disponible bajo licencia libre.