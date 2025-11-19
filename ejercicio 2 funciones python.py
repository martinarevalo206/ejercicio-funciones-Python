def sumar(a, b):
    """Retorna la suma de dos números"""
    return a + b

def restar(a, b):
    """Retorna la resta de dos números (a - b)"""
    return a - b

def multiplicar(a, b):
    """Retorna la multiplicación de dos números"""
    return a * b

def dividir(a, b):
    """
    Retorna la división de dos números (a / b).
    Verifica que el divisor no sea cero para evitar errores.
    """
    if b == 0:
        return "Error: División por cero"
    return a / b

def calculadora():
    """
    Función principal que interactúa con el usuario.
    Solicita dos números y una operación, luego llama a la función correspondiente.
    """
    print("=== Calculadora ===")
    
    # Solicitamos los dos números al usuario
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    # Solicitamos la operación deseada
    operacion = input("Ingrese la operación (+, -, *, /): ")
    
    # Según la operación elegida, llamamos a la función correspondiente
    if operacion == '+':
        resultado = sumar(num1, num2)
    elif operacion == '-':
        resultado = restar(num1, num2)
    elif operacion == '*':
        resultado = multiplicar(num1, num2)
    elif operacion == '/':
        resultado = dividir(num1, num2)
    else:
        resultado = "Operación no válida"
    
    # Mostramos el resultado
    print(f"Resultado: {resultado}")

# Ejecutar la calculadora
calculadora()