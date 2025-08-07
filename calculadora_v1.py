def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def mostrar_menu():
    print("\n===CALCULADORA V1===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    print("="*20)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona la opcion: ")
        if opcion == '3':
            print("¡Hasta luego!")
            break
        try:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
        except ValueError:
            print("Entrada invalida. Intenta de nuevo.")
            continue
        if opcion == '1':
            print(f"Resultado: {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"Resultado: {restar(num1, num2)}")
        else:
            print("Opcion invalida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
