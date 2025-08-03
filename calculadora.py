def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return " X ERROR: Division entre cero"
    return a/b

def mostrar_menu():
    print("\n" + "="*30)
    print("\n ===CALCULADORA BASICA===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("="*30)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona la opcion: ")

        if opcion == '5':
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
        elif opcion == '3':
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcion == '4':
            print(f"Resultado: {dividir(num1, num2)}")
        else:
            print("Opcion invalida. Intenta de nuevo.")

if __name__ == "__main__":
    main()