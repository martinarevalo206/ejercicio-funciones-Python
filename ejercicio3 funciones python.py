def es_primo(n):
    """
    Determina si un número es primo.
    Un número primo solo es divisible por 1 y por sí mismo.
    Retorna True si es primo, False si no lo es.
    """
    # Los números menores o iguales a 1 no son primos
    if n <= 1:
        return False
    
    # El 2 es el único número primo par
    if n == 2:
        return True
    
    # Descartamos todos los números pares (excepto el 2)
    if n % 2 == 0:
        return False
    
    # Verificamos divisibilidad solo con números impares
    # desde 3 hasta la raíz cuadrada de n
    i = 3
    while i * i <= n:  # Equivalente a: i <= sqrt(n)
        if n % i == 0:  # Si n es divisible por i, no es primo
            return False
        i += 2  # Avanzamos de 2 en 2 (solo números impares)
    
    # Si no encontramos divisores, el número es primo
    return True

# Solicitar el número al usuario
numero = int(input("Ingrese un número entero: "))

# Verificar si es primo y mostrar el resultado
if es_primo(numero):
    print(f"{numero} es un número primo")
else:
    print(f"{numero} NO es un número primo")