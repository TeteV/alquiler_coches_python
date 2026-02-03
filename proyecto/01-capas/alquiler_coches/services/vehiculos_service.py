from ..domain.vehiculo import Vehiculo
from ..application.vehiculos_repository import VehiculosRepository


class VehiculosService:
    def __init__(self, repository: VehiculosRepository):
        self.repository = repository
    
    def agregar_vehiculo(self, matricula: str, marca: str, modelo: str, anio: int, puertas: int = 0):
        try:
            vehiculo = Vehiculo(matricula, marca, modelo, anio, puertas)
            self.repository.agregar(vehiculo)
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False
        
    def listar_vehiculos(self):
        self.repository.obtener_todos()
    
    def buscar_vehiculo(self, matricula: str):
        return self.repository.buscar_por_matricula(matricula)

    def eliminar_vehiculo(self, matricula: str):
        self.repository.eliminar_por_matricula(matricula)