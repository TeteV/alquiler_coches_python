from typing import List, Optional
from domain.vehiculo import Vehiculo


class VehiculosRepository:
    def __init__(self):
        """Inicializa el repositorio con una lista vacía de vehículos."""
        self._vehiculos: List[Vehiculo] = []
    
    def agregar(self, vehiculo: Vehiculo):
        if self._existe_matricula(vehiculo.matricula):
            return print("La matrícula ya existe en el sistema.")
        
        self._vehiculos.append(vehiculo)
        return print("Vehículo agregado con éxito.")