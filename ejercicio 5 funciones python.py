def maximo_de_tres(a, b, c):
    """
    Encuentra el número máximo entre tres valores.
    No utiliza la función max() ni listas.
    
    Parámetros:
        a, b, c: tres números a comparar
    
    Retorna:
        el valor máximo de los tres
    """
    # Asumimos inicialmente que 'a' es el máximo
    maximo = a
    
    # Si 'b' es mayor que el máximo actual, actualizamos
    if b > maximo:
        maximo = b
    
    # Si 'c' es mayor que el máximo actual, actualizamos
    if c > maximo:
        maximo = c
    
    # Retornamos el valor máximo encontrado
    return maximo

# Solicitar los tres números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Calcular el máximo y mostrarlo
resultado = maximo_de_tres(num1, num2, num3)
print(f"El número máximo es: {resultado}")