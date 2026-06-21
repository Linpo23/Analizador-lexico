variables = []

while True:
    print("\n1. Declarar variable")
    print("2. Usar variable")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la variable: ")

        if nombre in variables:
            print("Error semántico: la variable ya fue declarada.")
        else:
            variables.append(nombre)
            print("Variable declarada correctamente.")

    elif opcion == "2":
        nombre = input("Nombre de la variable: ")

        if nombre in variables:
            print("Variable utilizada correctamente.")
        else:
            print("Error semántico: la variable no ha sido declarada.")

    elif opcion == "3":
        print("Fin del programa.")
        break

    else:
        print("Opción no válida.")