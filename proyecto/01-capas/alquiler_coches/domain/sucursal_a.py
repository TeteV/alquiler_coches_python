class SucursalA:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion
        self.vehiculos = []

    def obtener_informacion(self) -> str:
        return f"Sucursal: {self.nombre}, Dirección: {self.direccion}"
    
    def agregar_vehiculo(self, vehiculo) -> None:
        self.vehiculos.append(vehiculo)

    def alquilar_vehiculo(self, vehiculo) -> str:
        if vehiculo not in self.vehiculos:
            raise ValueError("El vehículo no pertenece a esta sucursal.")   
        return vehiculo.alquilar()

    def devolver_vehiculo(self, vehiculo) -> str:
        if vehiculo not in self.vehiculos:
            raise ValueError("El vehículo no pertenece a esta sucursal.")   
        return vehiculo.devolver()