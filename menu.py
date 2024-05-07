import operacion

# Función para mostrar el menú
def mostrar_menu():
    print("Bienvenido al programa de operaciones.")
    print("1. Ingresar números")
    print("2. Realizar suma")
    print("3. Salir")

# Función para ingresar números
def ingresar_numeros():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    return a, b

# Función para imprimir operación y resultado
def imprimir_operacion_resultado(a, b, operacion, resultado):
    print(f"Operación: {a} + {b}")
    print(f"Resultado: {resultado}")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            a, b = ingresar_numeros()
        elif opcion == "2":
            resultado = operacion.suma(a, b)
            imprimir_operacion_resultado(a, b, "suma", resultado)
        elif opcion == "3":
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
