def invertir(cadena):
    """
    Invierte una cadena de texto usando recursión.
    (Misma función del ejercicio anterior)
    """
    if len(cadena) <= 1:
        return cadena
    return invertir(cadena[1:]) + cadena[0]

def es_palindromo(cadena):
    """
    Determina si una cadena es un palíndromo.
    Un palíndromo se lee igual de izquierda a derecha que de derecha a izquierda.
    
    Proceso:
        1. Convertimos a minúsculas para ignorar mayúsculas/minúsculas
        2. Eliminamos espacios
        3. Comparamos la cadena original con su versión invertida
    
    Ejemplos de palíndromos: "oso", "anita lava la tina", "reconocer"
    """
    # Normalizamos la cadena: convertimos a minúsculas y quitamos espacios
    cadena = cadena.lower().replace(" ", "")
    
    # Comparamos la cadena con su versión invertida
    return cadena == invertir(cadena)

# Solicitar la cadena al usuario
texto = input("Ingrese una palabra o frase: ")

# Verificar si es palíndromo y mostrar el resultado
if es_palindromo(texto):
    print(f"'{texto}' ES un palíndromo")
else:
    print(f"'{texto}' NO es un palíndromo")