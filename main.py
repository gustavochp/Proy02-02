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
    
# _Fin de archivo    