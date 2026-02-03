#La ruta para iniciar el proyecto es H:\CodigoVSCode\alquiler_coches_python\proyecto\01-capas>
from alquiler_coches.services.vehiculos_service import VehiculosService
from alquiler_coches.application.vehiculos_repository import VehiculosRepository

def mostrar_menu():
    print("1. Listar vehículos")
    print("2. Buscar por matricula")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Registrar vehiculo")
    print("6. Modificar vehiculo")
    print("7. Eliminar vehiculo")
    print("8. Salir")

def main():
    repository = VehiculosRepository()
    servicio = VehiculosService(repository)
    servicio.agregar_vehiculo("A1", "Toyota", "Corolla", 2023, puertas=4)
    servicio.agregar_vehiculo("B2", "Honda", "Civic", 2022, puertas=4)
    while True:
        mostrar_menu()
        eleccion = input("Seleccione una opción (1-8): ")     
        try:
            if eleccion == '1':
                servicio.listar_vehiculos()
            elif eleccion == '2':
                matricula = input("Ingrese la matrícula del vehículo a buscar: ")
                vehiculo = servicio.buscar_vehiculo(matricula.upper())
                if not vehiculo:
                    print(f"Matrícula: {vehiculo.matricula}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.anio}, Puertas: {vehiculo.puertas}, Alquilado: {vehiculo.alquilado}")
                else:
                    print("Vehículo no encontrado.")
            elif eleccion == '3':
                print("Has seleccionado la Opción 3")
            elif eleccion == '4':
                print("Has seleccionado la Opción 4")
            elif eleccion == '5':
                print("Has entrado en la opcion Registro de vehiculo")
                matricula = input("Ingrese la matrícula del vehículo: ")
                marca = input("Ingrese la marca del vehículo: ")
                modelo = input("Ingrese el modelo del vehículo: ")
                anio = int(input("Ingrese el año del vehículo: "))
                puertas = int(input("Ingrese el número de puertas del vehículo: "))
                servicio.agregar_vehiculo(matricula.upper(), marca, modelo, anio, puertas)
            elif eleccion == '6':
                print("Has seleccionado la Opción 6")
            elif eleccion == '7':
                matricula = input("Ingrese la matrícula del vehículo a eliminar: ")
                servicio.eliminar_vehiculo(matricula.upper())
            elif eleccion == '8':
                print("Saliendo del menú. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        except ValueError as e:
                print("X " + str(e))

if __name__ == "__main__":
    main()