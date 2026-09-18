stock = 0

if stock > 0:
    print("Producto disponible")
else:
    print("Sin inventario")


# Variables del sistema
stock = 15
usuario_activo = True
es_admin = False

# 1. Evaluacion con AND (Ambas deben ser verdaderas)
if stock > 0 and usuario_activo:
    print("Venta autorizada: Hay stock y el usuario esta activo.")
else:
    print("Venta rechazada.")

# 2. Evaluacion con OR (Al menos una debe ser verdadera)
if usuario_activo or es_admin:
    print("Acceso al sistema concedido.")

# 3. Evaluacion con NOT (Invierte el valor)
if not es_admin:
    print("El usuario no tiene permisos de administrador.")

    