import math

# Paso 1 : Solicitar al usuario que ingrese el radio del circulo del cual quiere saber el area.
variable_radio = float(input("Por favor, ingresa el radio del circulo del cual se quiere saber el area: "))

# Paso 2: Calcular el area del circulo, utilizado la formula area = π * radio**2

varible_area = math.pi * (variable_radio**2)

# Paso 3: Mostrar al usuario el resultado del area.

print("El area del circulo con radio", variable_radio, "es", varible_area)