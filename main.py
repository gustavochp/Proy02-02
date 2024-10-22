# _ La idea es generar una calculadora básica.

import os

def clear_console():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')

def display_menu():
    # clear_console()
    print("\n--- Menu Calculadora ---")
    print("\n--- Ingresar 2 valores y luego la operación ---")
    print("1. + Suma")
    print("2. - Resta")
    print("3. * Multiplicación")
    print("4. / División")
    print("0. Salir")

def suma_calc(num1, num2):
    calc=num1 + num2
    print(f"Es una operación de suma, el resultado es: {calc:.2}")

def resta_calc(num1, num2):
    calc=num1 - num2
    print(f"Es una operación de resta, el resultado es: {calc:.2}")
    
def multip_calc(num1, num2):
    calc=num1 * num2
    print(f"Es una operación de multiplicación, el resultado es: {calc:.2}")

def div_calc(num1, num2):
    if num2!=0:
        calc=num1 / num2
        print(f"Es una operación de división, el resultado es: {calc:.2}")
    else: print(f"El divisor es 0 y la división por cero no se puede calcular")

def main():
    #hist_Calc = []
    clear_console()
    while True:
        num01=float(input("Ingrese primer valor: "))
        num02=float(input("Ingrese segundo valor: "))
        display_menu()
        choice = input("Seleccione una opción (1-4 / 0 para salir): ")

        if choice == "1":
            suma_calc(num01, num02)
        elif choice == "2":
            resta_calc(num01, num02)
        elif choice == "3":
            multip_calc(num01, num02)
        elif choice == "4":
            div_calc(num01, num02)
        elif choice == "0":
            print("Salir de la calculadora!")
            break
        else:
            print("No es una opción válida. Tratar de nuevo.")
        

if __name__ == "__main__":
    main()

# _Fin de programa Test 2.0.1
