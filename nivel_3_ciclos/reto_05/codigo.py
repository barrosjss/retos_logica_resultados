# Inicializar Variables
turno = 0
posiciones = []
ganador = None

N = int(input("Ingrese el número de caracoles: "))
L = int(input("Ingrese la distancia a recorrer (cm): "))

velocidades = []
for i in range(N):
    velocidades.append(int(input("Ingrese la velocidad del caracol ")))

while ganador is None:
    for j in range(N):
        if len(posiciones) == N:
            posiciones[j] = posiciones[j] + velocidades[j]
        else:
            posiciones.append(velocidades[j])

    turno = turno + 1

    print("Turno: ", turno)
    print("Posiciones: ", posiciones)

    # Verificacion de meta
    for j in range(N):
        if posiciones[j] >= L:
            ganador = j
            break

    # Turno multiplo de 3?
    if turno % 3 == 0:
        for j in range(N):
            posiciones[j] += 1
        print("------------------------")
        print("| Lluvia")
        print("| Posiciones Nuevas: ", posiciones)
        print("------------------------")

    # Turno multiplo de 5?
    if turno % 5 == 0:
        minVel = min(velocidades)
        posiciones[velocidades.index(minVel)] -= 2
        print("------------------------")
        print("| Barro")
        print("| Posiciones Nuevas: ", posiciones)
        print("------------------------")

    # Turno multiplo de 7?
    if turno % 7 == 0:
        maxPos = max(posiciones)
        posiciones[posiciones.index(maxPos)] += 3
        print("------------------------")
        print("| Viento")
        print("| Posiciones Nuevas: ", posiciones)
        print("------------------------")

    # Turno multiplo de 11?
    if turno % 11 == 0:
        minPos = min(posiciones)
        promedio = int(sum(posiciones) / N)
        posiciones[posiciones.index(minPos)] = promedio
        print("------------------------")
        print("| Trampa")
        print("| Posiciones Nuevas: ", posiciones)
        print("------------------------")


print("🏆 Ganador: ", ganador, "en el turno ", turno)
