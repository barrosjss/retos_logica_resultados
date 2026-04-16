# Declaramos las variables

# Variables que debe digital el usuario
caudal = 0
longitud = 0

# Variables que se calculan y se almacenan
categoria_caudal = ""
categoria_longitud = ""
importancia_ecologica = ""

# Solicitamos al usuario que ingrese el caudal y la longitud del río
caudal = int(input("Ingrese el caudal del río (en m3/s): "))
longitud = int(input("Ingrese la longitud del río (en km): "))

# Determinamos la categoría del caudal
if caudal < 10:
    categoria_caudal = "Arroyo"
elif 10 <= caudal < 100:
    categoria_caudal = "Río pequeño"
elif 100 <= caudal < 1000:
    categoria_caudal = "Río mediano"
else:
    categoria_caudal = "Río grande"

# Determinamos la categoría de la longitud
if longitud < 50:
    categoria_longitud = "Corto"
elif 50 <= longitud < 500:
    categoria_longitud = "Mediano"
else:
    categoria_longitud = "Largo"

# Determinamos la importancia ecológica del río
if categoria_caudal == "Río grande" and categoria_longitud == "Largo":
    importancia_ecologica = "Ecosistema Crítico 🔴"
elif categoria_caudal == "Río grande" and categoria_longitud == "Mediano":
    importancia_ecologica = "Alta importancia 🟠"
elif categoria_caudal == "Río mediano" and categoria_longitud == "Largo":
    importancia_ecologica = "Alta importancia 🟠"
elif categoria_caudal == "Río grande" or categoria_caudal == "Río mediano":
    importancia_ecologica = "Importancia media 🟡"
else:
    importancia_ecologica = "Importancia baja 🟢"

# Imprimimos los resultados
print("\n----------------------------------")
print("Resultados:")
print(f"Categoría del caudal: {categoria_caudal}")
print(f"Categoría de la longitud: {categoria_longitud}")
print(f"Importancia ecológica: {importancia_ecologica}")