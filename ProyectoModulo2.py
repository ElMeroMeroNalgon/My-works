import random

Ganador = False

def dibujarmatriz(visible):
    for fila in visible:
        for elemento in fila:
            print(f"{str(elemento):>2}", end=" ")
        print()

# Matriz oculta (con minas y números)
matriz = [
    [1, 2, 3, 4, 5, 6, 7, 8], 
    [9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48],
    [49, 50, 51, 52, 53, 54, 55, 56],
    [57, 58, 59, 60, 61, 62, 63, 64],
]

# Matriz visible (lo que ve el jugador)
visible = [
    [str(matriz[i][j]) for j in range(8)] for i in range(8)
]

# Generar 8 posiciones únicas para las minas
minas = random.sample(range(1, 65), 8)
print("Minas generadas (para pruebas):", minas)

# Reemplazar los números por minas en la matriz oculta
for mina in minas:
    fila = (mina - 1) // 8
    columna = (mina - 1) % 8
    matriz[fila][columna] = "*"

print("¡Bienvenido al juego de las minas!")
print("""Recuerde: 
Numeros = Posiciones no reveladas 
X = Posiciones descubiertas
O = Posiciones cubiertas por jugador 
""")

while not Ganador:
    dibujarmatriz(visible)
    Accion = int(input("Ingrese la accion que desea realizar: 1. Descubrir una posición\n2. Marcar una posicion\n3. Desmarcar una posicion\n"))
    if Accion == 1:
        fila = int(input("Ingrese el número de la fila que desea descubrir (1-8): "))
        columna = int(input("Ingrese el número de la columna que desea descubrir (1-8): "))
        if matriz[fila-1][columna-1] == "*":
            visible[fila-1][columna-1] = "*"
            dibujarmatriz(visible)
            print("¡Has pisado una mina! Fin del juego.")
            Ganador = True
        else:
            visible[fila-1][columna-1] = "X"
            print("Has descubierto una posición segura.")
            # Contar posiciones seguras descubiertas
            descubiertas = sum(row.count("X") for row in visible)
            if descubiertas == 64 - 8:  # 64 celdas menos 8 minas
                dibujarmatriz(visible)
                print("¡Felicidades! Has descubierto todas las posiciones seguras. ¡Ganaste!")
                Ganador = True
    elif Accion == 2:
        fila = int(input("Ingrese el número de la fila que desea marcar (1-8): "))
        columna = int(input("Ingrese el número de la columna que desea marcar (1-8): "))
        visible[fila-1][columna-1] = "O"
        print("Has marcado una posición.")
    elif Accion == 3:
        fila = int(input("Ingrese el número de la fila que desea desmarcar (1-8): "))
        columna = int(input("Ingrese el número de la columna que desea desmarcar (1-8): "))
        if visible[fila-1][columna-1] == "O":
            visible[fila-1][columna-1] = str((fila-1)*8 + columna)
            print("Has desmarcado una posición.")
        else:
            print("No hay ninguna posición marcada en esa ubicación.")




