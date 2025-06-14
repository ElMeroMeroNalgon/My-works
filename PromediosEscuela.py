Continuar=True
diccionario = {}
numeroestudiantes=0
porencimadelpromedio=0
pordebajodelpromedio=0
porcentajefinalencima=0
porcentajefinaldebajo=0
while Continuar:
    Continuar = int(input("Ingrese 1 para agregar otro estudiante o 0 para salir: "))
    if Continuar == 0:
        break
    if Continuar == 1:
        numeroestudiantes += 1
        nombre=input("Ingrese su nombre: ")
        puntajefinal=int(input("Ingrese su puntaje final: "))
        diccionario[nombre] = puntajefinal

if numeroestudiantes > 0:
    promedio = sum(diccionario.values()) / numeroestudiantes

for puntaje in diccionario.values():
    if puntaje > promedio:
        porencimadelpromedio += 1
    elif puntaje < promedio:
        pordebajodelpromedio += 1

porcentajefinalencima = (porencimadelpromedio / numeroestudiantes) * 100
porcentajefinaldebajo = (pordebajodelpromedio / numeroestudiantes) * 100
NombreMasAlto = max(diccionario, key=diccionario.get)
NombreMasBajo = min(diccionario, key=diccionario.get)
ValorMaximo = diccionario[NombreMasAlto]
ValorMinimo = diccionario[NombreMasBajo]

print("Diccionario de estudiantes y sus puntajes:", diccionario)
print("El estudiante con el puntaje más alto es:", NombreMasAlto, "con un puntaje de:", ValorMaximo)
print("El estudiante con el puntaje más bajo es:", NombreMasBajo, "con un puntaje de:", ValorMinimo)
print("El puntaje promedio de los estudiantes es:", promedio)
print("Total de estudiantes:", numeroestudiantes)
print("Porcentaje de estudiantes por encima del promedio:", porcentajefinalencima)
print("Porcentaje de estudiantes por debajo del promedio:", porcentajefinaldebajo)
print("Gracias por participar en la encuesta.")
