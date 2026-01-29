def mostrar_menu():
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Opción 5")
    print("6. Opción 6")
    print("7. Opción 7")
    print("8. Salir")

def main():
    while True:
        mostrar_menu()
        eleccion = input("Seleccione una opción (1-8): ")
        try:
            if eleccion == '1':
                print("Has entrado en la opcion Registro de vehiculo")
            elif eleccion == '2':
                print("Has seleccionado la Opción 2")
            elif eleccion == '3':
                print("Has seleccionado la Opción 3")
            elif eleccion == '4':
                print("Has seleccionado la Opción 4")
            elif eleccion == '5':
                print("Has seleccionado la Opción 5")
            elif eleccion == '6':
                print("Has seleccionado la Opción 6")
            elif eleccion == '7':
                print("Has seleccionado la Opción 7")
            elif eleccion == '8':
                print("Saliendo del menú. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        except ValueError as e:
                print("X " + str(e))

if __name__ == "__main__":
    main()