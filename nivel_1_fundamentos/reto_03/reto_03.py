
# Iniciamos las variables
precio_producto = 0
pago_cliente = 0
cambio = 0
cantidad = 0

precio_producto = int(input("Ingrese el precio del producto: "))
pago_cliente = int(input("Ingrese el pago del cliente: "))

# Calculamos el cambio
cambio = pago_cliente - precio_producto

if cambio == 0:
    print("No hay cambio")
elif cambio > 0:
    print("Cambio total: ", cambio)

    # Las denominaciones disponibles son (en pesos): 500, 200, 100, 50, 20, 10, 5, 1.

    # Calculamos la cantidad de billetes de 500
    cantidad = int(cambio / 500)
    if cantidad > 0:
        print("Billetes de 500: ", cantidad)
        cambio = cambio - (cantidad * 500)

    # Calculamos la cantidad de billetes de 200
    cantidad = int(cambio / 200)
    if cantidad > 0:
        print("Billetes de 200: ", cantidad)
        cambio = cambio - (cantidad * 200)

    # Calculamos la cantidad de billetes de 100
    cantidad = int(cambio / 100)
    if cantidad > 0:
        print("Billetes de 100: ", cantidad)
        cambio = cambio - (cantidad * 100)

    # Calculamos la cantidad de billetes de 50
    cantidad = int(cambio / 50)
    if cantidad > 0:
        print("Billetes de 50: ", cantidad)
        cambio = cambio - (cantidad * 50)

    # Calculamos la cantidad de billetes de 20
    cantidad = int(cambio / 20)
    if cantidad > 0:
        print("Billetes de 20: ", cantidad)
        cambio = cambio - (cantidad * 20)

    # Calculamos la cantidad de monedas de 10
    cantidad = cambio / 10
    if cantidad > 0:
        print("Monedas de 10: ", cantidad)
        cambio = cambio - (cantidad * 10)

    # Calculamos la cantidad de monedas de 5
    cantidad = int(cambio / 5)
    if cantidad > 0:
        print("Monedas de 5: ", cantidad)
        cambio = cambio - (cantidad * 5)

    # Calculamos la cantidad de monedas de 1
    cantidad = int(cambio / 1)
    if cantidad > 0:
        print("Monedas de 1: ", cantidad)
        cambio = cambio - (cantidad * 1)
    
    
    