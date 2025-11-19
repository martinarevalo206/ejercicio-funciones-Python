def factorial(n):
    """
    Calcula el factorial de un número entero positivo.
    El factorial de n (n!) es el producto de todos los números desde 1 hasta n.
    Ejemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120
    """
    # Caso base: el factorial de 0 y 1 es 1
    if n == 0 or n == 1:
        return 1
    
    # Inicializamos la variable que almacenará el resultado
    resultado = 1
    
    # Multiplicamos todos los números desde 2 hasta n
    for i in range(2, n + 1):
        resultado *= i  # resultado = resultado * i
    
    # Retornamos el resultado final
    return resultado

# Solicitar el número al usuario
numero = int(input("Ingrese un número entero positivo: "))
print(f"El factorial de {numero} es: {factorial(numero)}")