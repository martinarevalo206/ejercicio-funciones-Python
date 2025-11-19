def celsius_fahrenheit(c):
    """
    Convierte grados Celsius a Fahrenheit.
    Fórmula: F = (C × 9/5) + 32
    
    Parámetros:
        c: temperatura en grados Celsius
    
    Retorna:
        temperatura en grados Fahrenheit
    """
    # Aplicamos la fórmula de conversión
    fahrenheit = (c * 9/5) + 32
    return fahrenheit

# Solicitar la temperatura en Celsius al usuario
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir y mostrar el resultado
fahrenheit = celsius_fahrenheit(celsius)
print(f"{celsius}°C equivale a {fahrenheit}°F")