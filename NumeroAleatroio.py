def generar_aleatorio(minimo, maximo):
  """
  Genera un número aleatorio entre un mínimo y un máximo dados.

  Parámetros:
    minimo (int): El número mínimo del rango.
    maximo (int): El número máximo del rango.

  Retorno:
    int: Un número aleatorio entre el mínimo y el máximo.
  """
  import random
  return random.randint(minimo, maximo)


# Pedir al usuario el mínimo y el máximo
saludo = print("Bienvenido al programa. A continuación, elige los números entre los cuales quieres generar tu número aleatorio")
minimo = int(input("Introduzca el número mínimo: "))
maximo = int(input("Introduzca el número máximo: "))

# Validar que el mínimo sea menor o igual al máximo
while minimo > maximo:
  print("El número mínimo no puede ser mayor que el máximo.")
  minimo = int(input("Introduzca el número mínimo: "))

# Generar el número aleatorio
numero_aleatorio = generar_aleatorio(minimo, maximo)

# Mostrar el resultado
print(f"El número aleatorio es: {numero_aleatorio}")

# Pausar la ejecución para que el usuario pueda ver el resultado
input("Presiona Enter para continuar...")

