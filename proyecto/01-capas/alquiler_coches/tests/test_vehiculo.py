import unittest
from domain.vehiculo import Vehiculo


class TestVehiculo(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada test para crear un vehículo de prueba."""
        self.vehiculo = Vehiculo("A1", "Toyota", "Corolla", 2020, 4)
    
    def test_creacion_vehiculo(self):
        """Test para verificar que se crea un vehículo correctamente."""
        self.assertEqual(self.vehiculo.matricula, "A1")
        self.assertEqual(self.vehiculo.marca, "Toyota")
        self.assertEqual(self.vehiculo.modelo, "Corolla")
        self.assertEqual(self.vehiculo.anio, 2020)
        self.assertEqual(self.vehiculo.puertas, 4)
        self.assertFalse(self.vehiculo.alquilado)
    
    def test_alquilar_vehiculo(self):
        """Test para verificar que se puede alquilar un vehículo."""
        resultado = self.vehiculo.alquilar()
        self.assertTrue(self.vehiculo.alquilado)
        self.assertEqual(resultado, "Vehiculo alquilado con éxito.")
    
    def test_alquilar_vehiculo_ya_alquilado(self):
        """Test para verificar que no se puede alquilar un vehículo ya alquilado."""
        self.vehiculo.alquilar()
        resultado = self.vehiculo.alquilar()
        self.assertEqual(resultado, "El vehículo ya está alquilado.")
    
    def test_devolver_vehiculo(self):
        """Test para verificar que se puede devolver un vehículo alquilado."""
        self.vehiculo.alquilar()
        resultado = self.vehiculo.devolver()
        self.assertFalse(self.vehiculo.alquilado)
        self.assertEqual(resultado, "Vehiculo devuelto con éxito.")
    
    def test_devolver_vehiculo_no_alquilado(self):
        """Test para verificar que no se puede devolver un vehículo no alquilado."""
        resultado = self.vehiculo.devolver()
        self.assertEqual(resultado, "El vehículo no estaba alquilado.")
    
    def test_anio_invalido_menor(self):
        """Test para verificar que no se acepta un año menor a 1900."""
        with self.assertRaises(ValueError):
            Vehiculo("A1", "Toyota", "Corolla", 1899, 4)
    
    def test_anio_invalido_mayor(self):
        """Test para verificar que no se acepta un año mayor al actual."""
        with self.assertRaises(ValueError):
            Vehiculo("A1", "Toyota", "Corolla", 2027, 4)


if __name__ == '__main__':
    unittest.main()
