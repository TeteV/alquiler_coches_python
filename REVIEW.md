# REVIEW — Nestor

## REVISIÓN FASE 01 - 2026-03-03 — Nota: 5/10

**Fuente de verdad:** `proyecto/01-capas/`

---

### Lo que cumple

- **Repositorio creado y accesible** — el repositorio existe y se puede clonar.
- **README.md en la raíz** — es extenso y recoge descripción, arquitectura, instrucciones de uso, validaciones y ejemplos. Muy bien trabajado.
- **Subcarpeta `proyecto/` con carpeta de fase `01-capas/`** — la organización de carpetas sigue el esquema pedido.
- **Estructura de paquetes Python** — todos los directorios tienen su `__init__.py` y los imports relativos funcionan correctamente.
- **Clases principales creadas** — `Vehiculo`, `VehiculosRepository`, `VehiculosService` y `SucursalA` están presentes y con código real.
- **Encapsulamiento básico** — `Vehiculo` usa atributos privados (`_matricula`, `_anio`) con `@property` y setters.
- **`main.py` correcto** — configura el `sys.path` y llama al menú correctamente.
- **Menú con opciones básicas visibles** — listar, registrar y eliminar funcionan en parte.

---

### Lo que no cumple y cómo corregirlo

#### 1. Las capas no corresponden al modelo de referencia

**Problema:** La arquitectura del proyecto tiene la siguiente estructura real:

```
alquiler_coches/
├── domain/          ✅ (correcto)
├── application/     ← contiene el repositorio (debería estar en infrastructure/)
├── services/        ← capa extra no prevista en el modelo
├── infraestructure/ ← vacía (y con typo: falta la 'c' → infrastructure)
└── presentation/    ✅ (correcto)
```

En el modelo de referencia, `application/` contiene los servicios (casos de uso) e `infrastructure/` contiene las implementaciones concretas (repositorio en memoria, datos iniciales). En tu caso:
- Los **servicios** (`VehiculosService`) están en una carpeta `services/` que no es una capa estándar.
- El **repositorio** (`VehiculosRepository`) está en `application/`, pero es una implementación concreta y debería estar en `infrastructure/`.
- La carpeta `infraestructure/` está vacía y tiene un error tipográfico (debería ser `infrastructure`).

**Cómo resolverlo:** Mueve `VehiculosRepository` a `infrastructure/` y `VehiculosService` a `application/`. Elimina la carpeta `services/`. Corrige el nombre `infraestructure` → `infrastructure`.

---

#### 2. El setter de `matricula` no guarda el valor

**Problema:** En `domain/vehiculo.py`, el setter de `matricula` valida el formato pero nunca asigna el valor al atributo privado:

```python
@matricula.setter
def matricula(self, value):
    value = value.strip().upper()
    if len(value) != 2 or not value[0].isalpha() or not value[1].isdigit():
        raise ValueError("La matrícula debe tener el formato 'letra+numero'.")
    # ← falta: self._matricula = value
```

Además, el `__init__` asigna directamente `self._matricula = matricula` saltándose la validación. Esto significa que se puede crear un vehículo con matrícula inválida.

**Cómo resolverlo:** Añade `self._matricula = value` al final del setter. En `__init__` cambia `self._matricula = matricula` por `self.matricula = matricula` (sin guión bajo) para que pase por el setter.

---

#### 3. Lógica invertida en la búsqueda del menú

**Problema:** En `presentation/menu.py`, la condición de búsqueda está al revés:

```python
vehiculo = servicio.buscar_vehiculo(matricula.upper())
if not vehiculo:                        # ← si NO se encuentra...
    print(f"Matrícula: {vehiculo.matricula}, ...")  # ← intenta acceder a sus atributos → error
else:
    print("Vehículo no encontrado.")    # ← se muestra cuando SÍ se encuentra
```

Esto provoca un `AttributeError` si el vehículo no existe, y muestra "no encontrado" cuando sí existe.

**Cómo resolverlo:** Invierte la condición:

```python
if vehiculo:
    print(f"Matrícula: {vehiculo.matricula}, Marca: {vehiculo.marca}, ...")
else:
    print("Vehículo no encontrado.")
```

---

#### 4. Opciones 3, 4 y 6 del menú sin implementar

**Problema:** Las opciones «Opción 3», «Opción 4» y «Modificar vehículo» solo imprimen un texto de ruta de relleno. El menú no está completo.

**Cómo resolverlo:** Define qué hacen esas opciones (por ejemplo, alquilar un vehículo, devolverlo y modificar datos) e impleméntalas usando los métodos ya disponibles en `VehiculosService`.

---

#### 5. Datos iniciales hardcoded en el menú

**Problema:** Los vehículos de prueba se crean directamente en `menu.py`:

```python
servicio.agregar_vehiculo("A1", "Toyota", "Corolla", 2023, puertas=4)
servicio.agregar_vehiculo("B2", "Honda", "Civic", 2022, puertas=4)
```

Esto mezcla responsabilidades: la presentación no debería cargar datos iniciales.

**Cómo resolverlo:** Crea un módulo en `infrastructure/` (por ejemplo, `datos_iniciales.py`) con una función que reciba el servicio o repositorio y cargue los datos. Llama a esa función desde `main.py`, no desde el menú.

---

#### 6. Comentario con ruta Windows en el menú

**Problema:** La primera línea de `presentation/menu.py` contiene una ruta absoluta de Windows:

```python
#La ruta para iniciar el proyecto es H:\CodigoVSCode\alquiler_coches_python\proyecto\01-capas>
```

Esto no aporta información útil en el repositorio.

**Cómo resolverlo:** Elimina esa línea o sustitúyela por la instrucción de ejecución correcta: `python main.py` desde `proyecto/01-capas/`.

---

#### 7. La clase `SucursalA` no está integrada

**Problema:** `domain/sucursal_a.py` implementa la clase `SucursalA` con métodos de gestión de vehículos, pero no se usa en ningún sitio del sistema (no aparece en el menú, ni en los servicios, ni en el repositorio).

**Cómo resolverlo:** Si la sucursal es parte del modelo de dominio de tu proyecto, intégrala en el flujo principal. Si no, elimínala para no añadir código muerto.

---

### Resumen de la nota

| Criterio | Estado |
|---|---|
| Repositorio creado y compartido | ✅ |
| README.md con instrucciones | ✅ |
| Subcarpeta `proyecto/` y carpeta de fase | ✅ |
| Organización en capas correcta | ❌ (capas mal asignadas, infrastructure vacía) |
| Estructura de módulos y paquetes Python | ✅ |
| POO con clases y encapsulamiento | ⚠️ (setter matrícula buggeado) |
| Menú funciona correctamente | ❌ (búsqueda invertida, 3 opciones sin implementar) |
| Nombres significativos y PEP8 | ⚠️ (typo en `infraestructure`) |

**Nota final: 5/10**
