"""
Script principal para ejecutar la calculadora desde línea de comandos.
"""

from calculator import Calculator


def main():
    """Función principal que ejecuta la calculadora interactiva."""
    calc = Calculator()
    
    print("=== Calculadora Simple ===")
    print("Demostrando funcionalidades básicas:\n")
    
    # Ejemplos de uso
    print(f"Suma: 10 + 5 = {calc.add(10, 5)}")
    print(f"Resta: 10 - 5 = {calc.subtract(10, 5)}")
    print(f"Multiplicación: 10 * 5 = {calc.multiply(10, 5)}")
    print(f"División: 10 / 5 = {calc.divide(10, 5)}")
    print(f"Potencia: 2 ^ 3 = {calc.power(2, 3)}")
    
    print("\n=== Fin de la demostración ===")


if __name__ == "__main__":
    main()
