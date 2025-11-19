def potencia(base, exponente):
    """
    Calcula la potencia de un número sin usar el operador **.
    Utiliza multiplicaciones repetidas.
    
    Casos:
        - Exponente 0: cualquier número elevado a 0 es 1
        - Exponente negativo: usamos 1/base^(-exponente)
        - Exponente positivo: multiplicamos la base 'exponente' veces
    
    Ejemplos:
        potencia(2, 3) = 2 × 2 × 2 = 8
        potencia(5, 0) = 1
        potencia(2, -2) = 1/(2²) = 0.25
    """
    # Caso especial: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    
    # Caso de exponente negativo: aplicamos 1/base^(-exponente)
    if exponente < 0:
        return 1 / potencia(base, -exponente)
    
    # Caso de exponente positivo: multiplicamos la base repetidamente
    resultado = 1
    for i in range(exponente):
        resultado *= base  # Multiplicamos la base 'exponente' veces
    
    return resultado

# Solicitar la base y el exponente al usuario
base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

# Calcular la potencia y mostrar el resultado
resultado = potencia(base, exponente)
print(f"{base} elevado a {exponente} es: {resultado}")