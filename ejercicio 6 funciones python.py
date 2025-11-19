def contar_digitos(n):
    """
    Cuenta cuántos dígitos tiene un número entero.
    Funciona con números positivos y negativos.
    
    Parámetros:
        n: número entero
    
    Retorna:
        cantidad de dígitos
    """
    # Caso especial: el número 0 tiene 1 dígito
    if n == 0:
        return 1
    
    # Trabajamos con el valor absoluto para manejar números negativos
    n = abs(n)
    
    # Contador de dígitos
    contador = 0
    
    # Dividimos el número entre 10 hasta que sea 0
    # Cada división representa un dígito
    while n > 0:
        contador += 1
        n //= 10  # División entera: elimina el último dígito
    
    return contador

# Solicitar el número al usuario
numero = int(input("Ingrese un número entero: "))

# Contar los dígitos y mostrar el resultado
cantidad = contar_digitos(numero)
print(f"El número {numero} tiene {cantidad} dígitos")