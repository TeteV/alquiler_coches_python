# Revisión del proyecto — Nestor

**Fuente de verdad:** `proyecto/01-capas/`
**Fases detectadas:** 01 (capas)

## REVISIÓN FASE 03 - 2026-03-03 — Nota: 0/10

>Sin implementar

## REVISIÓN FASE 02 - 2026-03-03 — Nota: 0/10

>Sin implementar

## REVISIÓN FASE 01 - 2026-03-03 — Nota: 4/10

### Cumple

- Repositorio creado y accesible.
- `README.md` en la raíz, extenso y bien trabajado: descripción, arquitectura, instrucciones de uso, validaciones y ejemplos.
- Subcarpeta `proyecto/` con carpeta de fase `01-capas/`.
- Estructura de paquetes Python con `__init__.py` en todos los directorios e imports relativos correctos.
- Clases principales creadas con código real: `Vehiculo`, `VehiculosRepository`, `VehiculosService` y `SucursalA`.
- Encapsulamiento básico en `Vehiculo`: atributos privados (`_matricula`, `_anio`), `@property` y setters con validación.
- `main.py` correcto: configura el `sys.path` y llama al menú.
- Alcance del menú adecuado para una aplicación de este tipo: 8 opciones (listar, buscar, alquilar, devolver, registrar, modificar, eliminar y salir).

### Errores y aspectos a mejorar

- **[BUG] `domain/vehiculo.py:21-24` — el setter de `matricula` valida pero no guarda el valor.**. Además, el `__init__` asigna directamente `self._matricula = matricula` saltándose la validación, por lo que se pueden crear vehículos con matrículas inválidas.
  - *Cómo resolverlo:* Añade `self._matricula = value` al final del setter. En `__init__` cambia `self._matricula = matricula` por `self.matricula = matricula` (sin guión bajo) para que pase por el setter.

- **[BUG] `presentation/menu.py:29-32` — la lógica de la búsqueda está invertida.** La condición `if not vehiculo:` intenta acceder a los atributos del vehículo cuando este es `None`, produciendo un `AttributeError`. El mensaje "Vehículo no encontrado" se muestra precisamente cuando el vehículo sí existe.
  - *Cómo resolverlo:* Invierte la condición: `if vehiculo:` para mostrar los datos, y `else:` para el mensaje de no encontrado.

- **[DISEÑO] Las capas no corresponden al modelo de referencia.** La estructura real es:
  ```
  alquiler_coches/
  ├── application/     ← tiene el repositorio (debería estar en infrastructure/)
  ├── services/        ← capa extra no prevista en el modelo
  ├── infraestructure/ ← vacía
  └── presentation/    ← correcto
  ```
  `application/` debería contener los servicios (casos de uso); `infrastructure/` debería contener el repositorio en memoria y los datos iniciales. La carpeta `services/` no es una capa estándar del modelo.
  - *Cómo resolverlo:* Mueve `VehiculosRepository` a `infrastructure/`, mueve `VehiculosService` a `application/` y elimina la carpeta `services/`. Corrige también el typo `infraestructure` → `infrastructure`.

- **[DISEÑO] `application/vehiculos_repository.py:16-18` — `obtener_todos()` imprime directamente en la capa de datos.** La capa de repositorio no debe responsabilizarse de presentar información; debe devolver los datos y dejar que la presentación decida cómo mostrarlos.
  - *Cómo resolverlo:* Cambia el método para que devuelva `list(self._vehiculos.values())` y mueve el `print` al menú.

- **[DISEÑO] `presentation/menu.py:3` — el menú importa `VehiculosRepository` directamente.** La capa de presentación no debería conocer el repositorio; solo debería interactuar con el servicio.
  - *Cómo resolverlo:* Crea el repositorio y el servicio en `main.py` y pasa el servicio ya configurado al menú. Elimina el import de `VehiculosRepository` del menú.

- **[IMPORTANTE] Opciones 3, 4 y 6 del menú sin implementar.** Las opciones «Opción 3», «Opción 4» y «Modificar vehículo» solo imprimen texto de relleno; el menú no está completo.
  - *Cómo resolverlo:* Define qué hacen esas opciones (por ejemplo, alquilar, devolver y modificar datos) e impleméntalas usando los métodos ya disponibles en el servicio.

- **[IMPORTANTE] Datos iniciales hardcoded en el menú.** Los vehículos de prueba se crean directamente dentro de `menu.py`, mezclando responsabilidades. Sé que lo haces para pruebas, pero hay que arreglarlo.
  - *Cómo resolverlo:* Crea un módulo en `infrastructure/` (por ejemplo, `datos_iniciales.py`) con una función que reciba el repositorio o el servicio y cargue los datos. Llama a esa función desde `main.py`, no desde el menú.

- **[IMPORTANTE] El dominio solo tiene dos entidades (`Vehiculo` y `SucursalA`); el checklist requiere al menos tres.**
  - *Cómo resolverlo:* Añade una tercera entidad de dominio con sentido para tu sistema de alquiler; por ejemplo una clase `Cliente` (quien alquila el vehículo), `Contrato` (que representa el alquiler activo) o `Sucursal` como clase base de la que hereden distintos tipos de sucursal.

- **[IMPORTANTE] No hay herencia real en el código.** El checklist exige que al menos una clase use herencia (`class Hija(Padre):`). El nombre `SucursalA` sugiere la intención, pero no hay ninguna relación de herencia implementada en ningún fichero.
  - *Cómo resolverlo:* Define una clase base `Sucursal` en `domain/` con los atributos y métodos comunes, y haz que `SucursalA` herede de ella (`class SucursalA(Sucursal):`). Alternativamente, si tu tercera entidad lo permite, usa herencia en otro par de clases del dominio.

- **[IMPORTANTE] `domain/sucursal_a.py` no está integrada en el sistema: falta repositorio y opciones de menú.** La clase `SucursalA` existe en el dominio pero no hay repositorio para guardar sucursales, ni servicios que las gestionen, ni opciones en el menú para crearlas, consultarlas o asignarles vehículos. La funcionalidad de sucursales queda completamente inutilizada.
  - *Cómo resolverlo:* Crea un repositorio de sucursales en `infrastructure/` (similar a `VehiculosRepository`), un método o servicio en `application/` para gestionarlas, y añade al menú al menos las opciones básicas: listar sucursales, crear sucursal y asignar un vehículo a una sucursal.

- **[SUGERENCIA] `services/vehiculos_service.py` — `eliminar_vehiculo` no captura excepciones.** A diferencia de `agregar_vehiculo`, que captura `ValueError` y devuelve `False`, `eliminar_vehiculo` deja que la excepción se propague. Esto es inconsistente.
  - *Cómo resolverlo:* Aplica el mismo patrón `try/except ValueError` en `eliminar_vehiculo`, o define una política coherente para el manejo de errores en todos los métodos del servicio.

- **[SUGERENCIA] `presentation/menu.py:1` — comentario con ruta local de Windows.** La primera línea contiene una ruta absoluta del equipo de desarrollo que no aporta nada al repositorio.
  - *Cómo resolverlo:* Elimina esa línea o sustitúyela por la instrucción de ejecución correcta: `python main.py` desde `proyecto/01-capas/`.
