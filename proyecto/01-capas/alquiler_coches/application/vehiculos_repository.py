from ..domain.vehiculo import Vehiculo


class VehiculosRepository:
    def __init__(self):
        """Inicializa el repositorio con una lista vacía de vehículos."""
        self._vehiculos = {}
    
    def agregar(self, vehiculo: Vehiculo):
        for v in self._vehiculos.values():
            if v.matricula == vehiculo.matricula:
                raise ValueError(f"Ya existe un vehículo con la matrícula {vehiculo.matricula}.")
        self._vehiculos[vehiculo.matricula] = vehiculo
        print(f"Vehículo con matrícula {vehiculo.matricula} agregado correctamente.")

    def obtener_todos(self):
        for v in self._vehiculos.values():
            print(f"Matrícula: {v.matricula}, Marca: {v.marca}, Modelo: {v.modelo}, Año: {v.anio}, Puertas: {v.puertas}, Alquilado: {v.alquilado}")

    def buscar_por_matricula(self, matricula: str):
        return self._vehiculos.get(matricula, None)
    
    def eliminar_por_matricula(self, matricula: str):
        vehiculo = self.buscar_por_matricula(matricula)
        if not vehiculo:
            raise ValueError(f"No se encontró un vehículo con la matrícula {matricula}.")
        del self._vehiculos[matricula]
        print(f"Vehículo con matrícula {matricula} eliminado correctamente.")