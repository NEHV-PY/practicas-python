# Ejemplo de bucle for con range() y listas

# 1. Iterar un rango de numeros (del 1 al 5)
print("--- Conteo con range ---")
for i in range(1, 6):
    print(f"Numero de iteracion: {i}")

# 2. Recorrer una lista de modulos
print("\n--- Procesando lista de modulos ---")
modulos = ["Condicionales", "Bucles", "Funciones", "Clases"]

for modulo in modulos:
    print(f"Modulo de Python completado: {modulo}")


    # Suma acumulada de numeros del 1 al 5
suma_total = 0

for numero in range(1, 6):
    suma_total += numero  # Suma el numero actual al acumulado
    print(f"Sumando {numero} | Total parcial: {suma_total}")

print(f"\nSuma final completada: {suma_total}")