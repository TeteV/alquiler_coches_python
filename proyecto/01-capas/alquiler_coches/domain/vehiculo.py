import datetime


class Vehiculo:
    def __init__(self, matricula, marca, modelo, anio, puertas = 0):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.puertas = puertas
        self.alquilado = False

    @property
    def matricula(self):
        return self._matricula
    @property
    def anio(self):
        return self._anio
    
    @matricula.setter
    def matricula(self, value):
        value = value.strip().upper()
        if len(value) != 2 or not value[0].isalpha() or not value[1].isdigit():
            raise ValueError("La matrícula debe tener el formato 'letra+numero'.")
    @anio.setter
    def anio(self, value):
        if value < 1900 or value > datetime.now().year:
            raise ValueError("El año debe estar entre 1900 y 2026.")
        self._anio = value

    def alquilar(self):
        if not self.alquilado:
            self.alquilado = True
            return "Vehiculo alquilado con éxito."
        return "El vehículo ya está alquilado."
    
    def devolver(self):
        if self.alquilado:
            self.alquilado = False
            return "Vehiculo devuelto con éxito."
        return "El vehículo no estaba alquilado."

