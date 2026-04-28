# Guía de rutas Flask — Alquiler de Coches (ut4e1)

**Dominio:** gestión de vehículos en un sistema de alquiler de coches (CRUD + cambio de estado alquilado/disponible).

---

## 1. Estado del proyecto en el momento de este briefing

La subcarpeta de referencia es `proyecto/01-capas/alquiler_coches/`.

| Capa real | Contenido actual |
|---|---|
| `domain/` | `Vehiculo`, `SucursalA` |
| `services/` | `VehiculosService` (orquestador) |
| `application/` | `VehiculosRepository` (repositorio en memoria) |
| `infraestructure/` | Vacía |
| `presentation/` | `menu.py` (menú de consola) |

> La nomenclatura de capas difiere del modelo canónico. Para Flask, la capa de presentación (`presentation/`) se sustituirá por rutas Flask. El resto de capas no requiere modificación para ut4e1.

---

## 2. Inventario completo del menú

Análisis de `presentation/menu.py`:

| # | Texto en menú | Categoría | Método del servicio | Excepciones capturadas en menú |
|---|---|---|---|---|
| 1 | Listar vehículos | Lectura (colección) | `listar_vehiculos()` | — |
| 2 | Buscar por matrícula | Lectura (elemento) | `buscar_vehiculo(matricula)` | — (bug conocido: lógica invertida) |
| 3 | Opción 3 *(sin implementar)* | — intención: **Alquilar vehículo** | no existe → **a añadir** | — |
| 4 | Opción 4 *(sin implementar)* | — intención: **Devolver vehículo** | no existe → **a añadir** | — |
| 5 | Registrar vehículo | Acción (alta) | `agregar_vehiculo(matricula, marca, modelo, anio, puertas)` | `ValueError` |
| 6 | Modificar vehículo *(sin implementar)* | Acción (actualización parcial) | no existe → **a añadir** | — |
| 7 | Eliminar vehículo | Acción (baja) | `eliminar_vehiculo(matricula)` | `ValueError` (no capturado en servicio) |
| 8 | Salir | Control de flujo | — | — |

**Operaciones de dominio adicionales** presentes en `domain/vehiculo.py` pero sin opción de menú:

| Operación | Método de dominio | Estado |
|---|---|---|
| Alquilar vehículo | `Vehiculo.alquilar()` | Disponible en dominio; sin servicio ni menú |
| Devolver vehículo | `Vehiculo.devolver()` | Disponible en dominio; sin servicio ni menú |

---

### Ejemplo: cómo quedaría `app.py` con dos rutas ya hechas

El siguiente fragmento muestra la estructura mínima de `app.py` con dos rutas implementadas
para que puedas tomar el patrón y aplicarlo al resto:

```python
from flask import Flask
from alquiler_coches.application.vehiculos_repository import VehiculosRepository
from alquiler_coches.services.vehiculos_service import VehiculosService

app = Flask(__name__)

repositorio = VehiculosRepository()
servicio = VehiculosService(repositorio)


@app.route("/")
def bienvenida():
    return (
        "Bienvenido al sistema de alquiler de coches\n"
        "  /vehiculos              → lista todos los vehículos\n"
        "  /vehiculos/<matricula>  → detalle de un vehículo\n"
    )


@app.route("/vehiculos")
def listar_vehiculos():
    # Nota: en el estado actual del proyecto, listar_vehiculos() imprime
    # directamente en lugar de devolver datos. Antes de implementar esta ruta
    # hay que corregir el repositorio para que devuelva la lista (ver sección 4).
    # Como alternativa provisional puedes usar buscar_vehiculo con una matrícula conocida.
    vehiculos = servicio.listar_vehiculos()
    if not vehiculos:
        return "No hay vehículos registrados."
    return "\n".join(str(v) for v in vehiculos)


if __name__ == "__main__":
    app.run(debug=True)
```

**Lo que hace cada parte:**

- El repositorio y el servicio se crean **una sola vez** fuera de las vistas, al arrancar la
  aplicación. Así todas las rutas comparten el mismo estado en memoria.
- Cada función de vista llama al método del servicio correspondiente y devuelve texto plano.
- Para rutas con `ValueError` puedes devolver una tupla `(mensaje, código)`:
  `return "No encontrado", 404` o `return "Ya existe", 409`.

---

## 4. Métodos del servicio a añadir (delegación pura)

Para cubrir toda la API, se necesitan los siguientes métodos en `VehiculosService`:

> Antes de implementar cualquier ruta, corrige el bug en `listar_vehiculos()`: el repositorio actualmente imprime en lugar de devolver la lista. Cambia `repository.obtener_todos()` para que devuelva `list(self._vehiculos.values())` y el servicio devuelva esa lista.

| Método a añadir | Delegación | Descripción |
|---|---|---|
| `alquilar_vehiculo(matricula) -> dict` | `buscar_vehiculo` + `vehiculo.alquilar()` | Cambia el estado a `alquilado=True`; lanza `ValueError` si no existe o ya está alquilado |
| `devolver_vehiculo(matricula) -> dict` | `buscar_vehiculo` + `vehiculo.devolver()` | Cambia el estado a `alquilado=False`; lanza `ValueError` si no existe o no estaba alquilado |
| `modificar_vehiculo(matricula, **campos) -> dict` | `buscar_vehiculo` + asignación de atributos | Actualiza marca, modelo, anio o puertas; lanza `ValueError` si no existe |
| `listar_vehiculos() -> list[Vehiculo]` | `repository.obtener_todos()` corregido | Devuelve lista de dicts serializables (no imprime) |

> `SucursalA` existe en el dominio pero no está integrada en servicios ni repositorio. Para ut4e1, queda fuera del alcance de la API. Si en fases posteriores se integra, habrá que añadir un `SucursalService`.

---

## 5. Rutas sugeridas (toda la API)

Los parámetros de creación/modificación se pasan como segmentos de URL.

### Vehículos — consulta

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/vehiculos` | `listar_vehiculos()` | Lista todos los vehículos |
| `/vehiculos/<matricula>` | `buscar_vehiculo(matricula)` | Detalle de un vehículo; 404 si no existe |

### Vehículos — alta y baja

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/vehiculos/nuevo/<matricula>/<marca>/<modelo>/<anio>/<puertas>` | `agregar_vehiculo(matricula, marca, modelo, anio, puertas)` | Alta de vehículo; 409 si matrícula duplicada; 400 si datos inválidos |
| `/vehiculos/<matricula>/eliminar` | `eliminar_vehiculo(matricula)` | Baja de vehículo; 404 si no existe |

### Vehículos — modificación

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/vehiculos/<matricula>/modificar/<marca>/<modelo>/<anio>/<puertas>` | `modificar_vehiculo(matricula, **campos)` | Actualiza marca, modelo, anio o puertas; 404 si no existe; 400 si datos inválidos |

### Vehículos — cambio de estado

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/vehiculos/<matricula>/alquilar` | `alquilar_vehiculo(matricula)` | Marca el vehículo como alquilado; 404 si no existe; 409 si ya estaba alquilado |
| `/vehiculos/<matricula>/devolver` | `devolver_vehiculo(matricula)` | Marca el vehículo como disponible; 404 si no existe; 409 si no estaba alquilado |

**Total: 7 rutas / 7 operaciones.**

---

## 6. Puntos de atención específicos del dominio

### 6.1. Estado `alquilado` como campo de transición, no como CRUD
El campo `alquilado` no se debe actualizar a través de `PUT /vehiculos/<matricula>` (modificación general). El cambio de estado tiene rutas propias (`/alquilar`, `/devolver`) para evitar que un cliente lo establezca directamente a `true` sin pasar por la lógica de dominio.

### 6.2. Código de estado para vehículo ya alquilado / ya devuelto
Usar `409 Conflict` cuando se intenta alquilar un vehículo que ya está alquilado, o devolver uno que no estaba alquilado. No usar `400 Bad Request` (la petición está bien formada; el conflicto es de estado del recurso).

### 6.3. Código de estado para matrícula duplicada
Usar `409 Conflict` al hacer `/vehiculos/nuevo/...` con una matrícula que ya existe en el repositorio.

### 6.4. Formato de matrícula — validación en dominio
La clase `Vehiculo` valida el formato (letra + dígito, longitud 2). El setter actual tiene un bug: no guarda el valor. Antes de exponer la API, hay que corregir `domain/vehiculo.py` o la validación no funcionará. El error que lanzará el dominio es `ValueError`; la ruta debe capturarlo y devolver `400`. **Corrige este bug antes de exponer la API o las validaciones de formato no funcionarán.**

### 6.5. Ausencia de módulo `errores.py`
El proyecto no tiene un módulo centralizado de excepciones personalizadas. Para ut4e1 es aceptable usar `ValueError` nativo. En ut4e2 se recomienda crear `application/excepciones.py` con clases como `VehiculoNoEncontrado`, `MatriculaDuplicada`, `VehiculoYaAlquilado` para afinar los códigos HTTP sin inspeccionar el mensaje del error.

### 6.6. `listar_vehiculos()` devuelve `None` actualmente
El repositorio imprime directamente en lugar de devolver datos. Hay que corregirlo antes de implementar `/vehiculos`. Ver sección 4.

### 6.7. Mostrar vehículos como texto
`Vehiculo` no tiene método `__str__` definido. Para mostrar un vehículo en la ruta Flask, accede directamente a sus atributos: `f"{v.matricula} — {v.marca} {v.modelo} ({v.anio})"`. Si el dominio define `__str__`, puedes usar directamente `str(vehiculo)`.
