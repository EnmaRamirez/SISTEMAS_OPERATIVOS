def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "ERROR: Division entre cero"
    return a / b

def raiz(a):
    if a < 0:
        return "ERROR: Raiz de numero negativo"
    return a ** 0.5

def mostrar_menu():
    print("\n===CALCULADORA V4===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raiz cuadrada")
    print("6. Salir")
    print("="*20)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona la opcion: ")
        if opcion == '6':
            print("¡Hasta luego!")
            break
        if opcion == '5':
            try:
                num1 = float(input("Ingrese el numero: "))
            except ValueError:
                print("Entrada invalida. Intenta de nuevo.")
                continue
            print(f"Resultado: {raiz(num1)}")
        elif opcion in ['1', '2', '3', '4']:
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

