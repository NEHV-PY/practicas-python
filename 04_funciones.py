# Modulo 04: Funciones en Python (def y return)

# 1. Funcion simple con parametro
def saludar_censador(nombre, rol):
    print(f"¡Hola {nombre}! Tu rol asignado es: {rol}")

# 2. Funcion que calcula y DEVUELVE un valor (return)
def calcular_avance(registrados, meta_total):
    porcentaje = (registrados / meta_total) * 100
    return porcentaje  # Devuelve el resultado para usarlo afuera

# --- Ejecucion de las funciones ---
print("--- 1. Pruebas de Saludos ---")
saludar_censador("Nestor", "Capitan de Campo")
saludar_censador("Yorman", "Censador de Terreno")

print("\n--- 2. Calculo de Avance ---")
# Guardamos lo que devuelva la funcion en una variable
progreso = calcular_avance(45, 50)
print(f"El porcentaje de avance del operativo es: {progreso}%")