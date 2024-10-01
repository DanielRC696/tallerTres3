# diccionario vacio
productos = {}

# Agregar productos, valor y cantidad
while True:
    producto = input("Ingrese el nombre del producto (o 'imprimir' para terminar): ")
    if producto.lower() == 'imprimir':
        break
    try:
        valor = float(input(f"Ingrese el valor del producto '{producto}': "))
        cantidad = int(input(f"Ingrese la cantidad del producto '{producto}': "))

        # Guardar el valor y la cantidad en el diccionario
        productos[producto] = {'valor': valor, 'cantidad': cantidad}

    except ValueError:
        print("Error: Ingrese un valor numérico válido para el precio y cantidad.")

# Calcular el total de artículos y el total antes de descuento
total_articulos = sum(datos['cantidad'] for datos in productos.values())
total_sin_descuento = sum(datos['valor'] * datos['cantidad'] for datos in productos.values())

# Determina el descuento
if total_articulos >= 5:
    descuento = 0.20
elif total_articulos >= 3:
    descuento = 0.10
else:
    descuento = 0

# Calcular el total despues del descuento
total_con_descuento = total_sin_descuento * (1 - descuento)

# Determina el metodo de pago
if total_articulos < 3:
    metodo_pago = "Efectivo"
else:
    metodo_pago = "Tarjeta"
    total_con_descuento *= 1.02  # Cargo adicional del 2% si es con tarjeta

# Almacena el producto al salir del bucle
lista_productos = list(productos.keys())  # Lista con los nombres de los productos

# Imprimir el resumen de la compra
print("\nResumen de la compra:")
print(f"Número total de artículos: {total_articulos}")
print(f"Total antes del descuento: {total_sin_descuento:.2f} COP")
print(f"Descuento aplicado: {descuento * 100:.0f}%")
print(f"Total después del descuento: {total_con_descuento:.2f} COP")
print(f"Método de pago recomendado: {metodo_pago}")

# Imprimir el diccionario final
print("\nProductos, cantidades y sus valores:")
for producto, datos in productos.items():
    cantidad = datos['cantidad']
    valor = datos['valor']
    print(f"{producto}: {cantidad} unidades a {valor:.2f} COP cada una")

# Imprimir la lista de productos final
print("\nLista de productos:")
print(lista_productos)