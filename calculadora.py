def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def potencia(a, b):
    return a ** b

def raiz(a):
    if a < 0:
        return "ERROR: Raiz de numero negativo"
    return a ** 0.5
def dividir(a, b):
    if b == 0:
        return "ERROR: Division entre cero"
    return a/b

def mostrar_menu():
    print("\n===CALCULADORA BASICA===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Salir")
    print("="*30)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona la opcion: ")

        if opcion == '7':
            print("¡Hasta luego!")
            break
        try:
            if opcion == '6':
                num1 = float(input("Ingrese el numero: "))
            else:
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
        elif opcion == '5':
            print(f"Resultado: {potencia(num1, num2)}")
        elif opcion == '6':
            print(f"Resultado: {raiz(num1)}")
        else:
            print("Opcion invalida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
                













