def mcd(a, b):
    """
    Calcula el Máximo Común Divisor de dos números.
    Utiliza el algoritmo de Euclides:
        - El MCD de a y b es igual al MCD de b y (a mod b)
        - Se repite hasta que b sea 0
        - Cuando b = 0, el MCD es a
    
    Ejemplo: mcd(12, 18)
        12 mod 18 = 12
        18 mod 12 = 6
        12 mod 6 = 0
        MCD = 6
    """
    # Trabajamos con valores absolutos para manejar números negativos
    a = abs(a)
    b = abs(b)
    
    # Algoritmo de Euclides
    while b != 0:
        temporal = b           # Guardamos el valor de b
        b = a % b              # b toma el residuo de a/b
        a = temporal           # a toma el valor anterior de b
    
    # Cuando b llega a 0, a contiene el MCD
    return a

def mcm(a, b):
    """
    Calcula el Mínimo Común Múltiplo de dos números.
    Utiliza la fórmula: MCM(a,b) = |a × b| / MCD(a,b)
    
    El MCM es el menor número que es múltiplo de ambos números.
    
    Ejemplo: mcm(12, 18)
        MCD(12, 18) = 6
        MCM = (12 × 18) / 6 = 216 / 6 = 36
    """
    # Caso especial: si alguno es 0, el MCM es 0
    if a == 0 or b == 0:
        return 0
    
    # Aplicamos la fórmula: MCM = |a × b| / MCD(a,b)
    # Usamos // para obtener división entera
    return abs(a * b) // mcd(a, b)

# Solicitar los dos números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calcular MCD y MCM
resultado_mcd = mcd(num1, num2)
resultado_mcm = mcm(num1, num2)

# Mostrar los resultados
print(f"\nResultados para {num1} y {num2}:")
print(f"MCD (Máximo Común Divisor): {resultado_mcd}")
print(f"MCM (Mínimo Común Múltiplo): {resultado_mcm}")