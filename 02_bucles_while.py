# Uso de break y continue en un bucle while
contador = 0

while contador < 5:
    contador += 1

    if contador == 3:
        print("Saltando la iteracion numero 3 con 'continue'...")
        continue  # Omite el print final para el 3 y salta al siguiente paso

    if contador == 5:
        print("Interrumpiendo el bucle por completo con 'break'.")
        break  # Detiene el bucle inmediatamente

    print(f"Ejecutando vuelta numero: {contador}")