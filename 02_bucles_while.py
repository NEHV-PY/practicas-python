# Control de inventario con bucle while
stock = 5

while stock > 0:
    print(f"Procesando venta... Unidades restantes en stock: {stock}")
    stock -= 1  # Resta 1 al stock en cada vuelta para evitar un bucle infinito

print("¡Atención! El stock se ha agotado por completo.")