def invertir(cadena):
    """
    Invierte una cadena de texto usando recursión.
    No utiliza slicing [::-1] ni estructuras avanzadas.
    
    Lógica:
        - Caso base: si la cadena tiene 0 o 1 caracteres, se retorna tal cual
        - Caso recursivo: invertimos la subcadena sin el primer carácter
          y le agregamos el primer carácter al final
    
    Ejemplo: invertir("ABC")
        = invertir("BC") + "A"
        = (invertir("C") + "B") + "A"
        = ("C" + "B") + "A"
        = "CBA"
    """
    # Caso base: cadena vacía o de un solo carácter
    if len(cadena) <= 1:
        return cadena
    
    # Caso recursivo:
    # - cadena[1:] es la cadena sin el primer carácter
    # - cadena[0] es el primer carácter
    # Invertimos el resto y agregamos el primer carácter al final
    return invertir(cadena[1:]) + cadena[0]

# Solicitar la cadena al usuario
texto = input("Ingrese una palabra o frase: ")

# Invertir y mostrar el resultado
texto_invertido = invertir(texto)
print(f"Texto original: {texto}")
print(f"Texto invertido: {texto_invertido}")