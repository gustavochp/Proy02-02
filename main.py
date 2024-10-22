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
    print("\n--- Menu Calculadora. Indicar la Operación: ---")
    #print("\n--- Ingresar 2 valores y luego la operación ---")
    print("+ . Suma")
    print("- . Resta")
    print("* . Multiplicación")
    print("/ . División")
    print("0. Salir")

def suma_calc(num1, num2):
    calc=num1 + num2
    print (f"{num1:0.1f} + {num2:0.1f} = {calc:0.1f}")

def resta_calc(num1, num2):
    calc=num1 - num2
    print (f"{num1:0.1f} - {num2:0.1f} = {calc:0.1f}")
    
def multip_calc(num1, num2):
    calc=num1 * num2
    print (f"{num1:0.1f} * {num2:0.1f} = {calc:0.1f}")

def div_calc(num1, num2):
    if num2!=0:
        calc=num1 / num2
        print (f"{num1:0.1f} / {num2:0.1f} = {calc:0.1f}")
    else: print(f"El divisor es 0 y la división por cero no se puede calcular")

def main():
    hist_Calc = []
    clear_console()
    while True:
        print("\n--- Ingresar 2 valores y luego la operación ---")
        num01=float(input("Ingrese primer valor: "))
        num02=float(input("Ingrese segundo valor: "))
        display_menu()
        choice = input("Seleccione una operación (0 para salir): ")
        print("")
        if choice == "+":
            suma_calc(num01, num02)
        elif choice == "-":
            resta_calc(num01, num02)
        elif choice == "*":
            multip_calc(num01, num02)
        elif choice == "/":
            div_calc(num01, num02)
        elif choice == "0":
            print("Salir de la calculadora!")
            break
        else:
            print("No es una opción válida. Tratar de nuevo.")
        
        print("")

if __name__ == "__main__":
    main()

# _Fin de programa
