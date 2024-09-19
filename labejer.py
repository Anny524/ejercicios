#lab1#
1#
# Asumamos que tu nombre es 'Juan'
nombre = 'Juan'
longitud_nombre = len(nombre)
print(f"La longitud de mi nombre es: {longitud_nombre}")

2#
# Asumamos que tu apellido es 'Pérez'
nombre = 'Juan'
apellido = 'Pérez'

longitud_nombre = len(nombre)
longitud_apellido = len(apellido)

if longitud_nombre > longitud_apellido:
    print(f"El nombre es más largo que el apellido.")
elif longitud_nombre < longitud_apellido:
    print(f"El apellido es más largo que el nombre.")
else:
    print(f"El nombre y el apellido tienen la misma longitud.")


3#
# Declarar variables
num_one = 5
num_two = 4

# Sumar
total = num_one + num_two
print(f"La suma es: {total}")

# Restar
diff = num_one - num_two
print(f"La resta es: {diff}")

# Multiplicar
producto = num_one * num_two
print(f"La multiplicación es: {producto}")

# Dividir
división = num_one / num_two
print(f"La división es: {división}")

# División de módulo
resto = num_two % num_one
print(f"El resto de la división es: {resto}")

# Exponenciación
exp = num_one ** num_two
print(f"El resultado de la potencia es: {exp}")

# División de piso
floor_division = num_one // num_two
print(f"La división de piso es: {floor_division}")


4#
import math

# Radio fijo
radio = 30

# Área del círculo
area_of_circle = math.pi * (radio ** 2)
print(f"El área del círculo es: {area_of_circle}")

# Circunferencia del círculo
circum_of_circle = 2 * math.pi * radio
print(f"La circunferencia del círculo es: {circum_of_circle}")

# Tomar radio como entrada del usuario
radio_usuario = float(input("Introduce el radio del círculo en metros: "))

# Calcular el área con el radio ingresado por el usuario
area_usuario = math.pi * (radio_usuario ** 2)
print(f"El área del círculo con radio {radio_usuario} metros es: {area_usuario}")


5#
# Obtener información del usuario
nombre_usuario = input("Introduce tu nombre: ")
apellido_usuario = input("Introduce tu apellido: ")
pais_usuario = input("Introduce tu país: ")
edad_usuario = int(input("Introduce tu edad: "))

print(f"Nombre: {nombre_usuario}")
print(f"Apellido: {apellido_usuario}")
print(f"País: {pais_usuario}")
print(f"Edad: {edad_usuario}")


#lab02#
1#
texto = "python"
longitud = len(texto)
longitud_float = float(longitud)
longitud_str = str(longitud_float)

print("Longitud del texto:", longitud)
print("Longitud como float:", longitud_float)
print("Longitud como string:", longitud_str)

2#
numero = 4  # Cambia este número para probar otros casos

if numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")


3#
division_entera = 7 // 3
valor_convertido = int(2.7)

if division_entera == valor_convertido:
    print("La división entera de 7 entre 3 es igual al valor de 2.7 convertido a entero.")
else:
    print("No son iguales.")


4#
tipo_cadena = type('10')
tipo_entero = type(10)

if tipo_cadena == tipo_entero:
    print("El tipo de '10' es igual al tipo de 10.")
else:
    print("El tipo de '10' no es igual al tipo de 10.")


5#
try:
    valor = int(float('9.8'))
    if valor == 10:
        print("int('9.8') es igual a 10.")
    else:
        print("int('9.8') no es igual a 10.")
except ValueError:
    print("Error: no se puede convertir '9.8' a entero directamente.")


6#
horas = float(input("Introduce las horas trabajadas: "))
tarifa_por_hora = float(input("Introduce la tarifa por hora: "))

salario_semanal = horas * tarifa_por_hora
print(f"Tu salario semanal es {salario_semanal:.2f}")


7#
anos_vividos = int(input("Introduce el número de años que has vivido: "))

# Suponiendo 365 días por año
segundos_por_anio = 365 * 24 * 60 * 60
segundos_vividos = anos_vividos * segundos_por_anio

print(f"Has vivido durante {segundos_vividos} segundos.")

8#
print("Tabla de potencias:")
for i in range(1, 6):
    fila = [str(i ** j) for j in range(1, 6)]
    print(" ".join(fila))


9#
cadena = input("Introduce una cadena: ")
cadena_invertida = cadena[::-1]

print("La cadena invertida es:", cadena_invertida)


10#
cadena = input("Introduce una cadena: ")
vocales = "aeiouAEIOU"
contador_vocales = sum(1 for caracter in cadena if caracter in vocales)

print("Número de vocales en la cadena:", contador_vocales)

11#
cadena = input("Introduce una cadena: ")
cadena_limpia = cadena.replace(" ", "").lower()
es_palindromo = cadena_limpia == cadena_limpia[::-1]

if es_palindromo:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")


12#
cadena = input("Introduce una cadena: ")
cadena_reemplazada = cadena.replace(" ", "_")

print("Cadena con espacios reemplazados:", cadena_reemplazada)


13#
cadena = input("Introduce una cadena: ")
numero_palabras = len(cadena.split())

print("Número de palabras en la cadena:", numero_palabras)


5

15#
cadena = input("Introduce una cadena: ")
cadena_limpia = cadena.strip()

print("Cadena sin espacios al principio y al final:", cadena_limpia)


16#
cadena = input("Introduce una cadena: ")
inicio = int(input("Introduce el índice de inicio: "))
fin = int(input("Introduce el índice de fin: "))

subcadena = cadena[inicio:fin]
print("Subcadena extraída:", subcadena)


17#
cadena = input("Introduce una cadena: ")
prefijo = input("Introduce el prefijo: ")
sufijo = input("Introduce el sufijo: ")

empieza_con_prefijo = cadena.startswith(prefijo)
termina_con_sufijo = cadena.endswith(sufijo)

print(f"La cadena comienza con '{prefijo}':", empieza_con_prefijo)
print(f"La cadena termina con '{sufijo}':", termina_con_sufijo)




#lab03#
1#
# Solicitar al usuario dos palabras
palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

# Comparar las palabras alfabéticamente
if palabra1 < palabra2:
    print(f"La palabra '{palabra1}' va antes que '{palabra2}' en orden alfabético.")
elif palabra1 > palabra2:
    print(f"La palabra '{palabra2}' va antes que '{palabra1}' en orden alfabético.")
else:
    print(f"Las palabras '{palabra1}' y '{palabra2}' son iguales.")


2#
# Solicitar al usuario las longitudes de los lados del triángulo
lado1 = float(input("Introduce la longitud del primer lado: "))
lado2 = float(input("Introduce la longitud del segundo lado: "))
lado3 = float(input("Introduce la longitud del tercer lado: "))

# Clasificar el triángulo
if lado1 == lado2 == lado3:
    print("El triángulo es equilátero.")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")


3#
# Solicitar al usuario las notas
notas = []
n = int(input("¿Cuántas notas quieres ingresar? "))

for _ in range(n):
    nota = float(input("Introduce una nota: "))
    notas.append(nota)

# Calcular el promedio
promedio = sum(notas) / len(notas)
print(f"El promedio de las notas es: {promedio}")


4#
# Solicitar al usuario dos números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Solicitar al usuario la operación deseada
operacion = input("Introduce la operación deseada (suma, resta, multiplicación, división): ").strip().lower()

# Realizar la operación correspondiente
if operacion == "suma":
    resultado = num1 + num2
elif operacion == "resta":
    resultado = num1 - num2
elif operacion == "multiplicación":
    resultado = num1 * num2
elif operacion == "división":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: División por cero"
else:
    resultado = "Operación no válida"

print(f"El resultado de la operación es: {resultado}")


5#
# Solicitar al usuario un número entero
numero = int(input("Introduce un número entero: "))

# Determinar si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

6#
# Solicitar al usuario tres números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Determinar el mayor de los tres números
if num1 >= num2 and num1 >= num3:
    print(f"El número mayor es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número mayor es: {num2}")
else:
    print(f"El número mayor es: {num3}")


7#
# Solicitar al usuario el precio original y la categoría del descuento
precio_original = float(input("Introduce el precio original del producto: "))
categoria = input("Introduce la categoría del descuento (estudiante, jubilado, empleado, otro): ").strip().lower()

# Aplicar el descuento correspondiente
if categoria == "estudiante":
    descuento = 0.10
elif categoria == "jubilado":
    descuento = 0.15
elif categoria == "empleado":
    descuento = 0.05
else:
    descuento = 0.00

precio_final = precio_original * (1 - descuento)
print(f"El precio final después del descuento es: {precio_final}")


8#
# Solicitar al usuario un número
numero = float(input("Introduce un número: "))

# Determinar si el número es positivo, negativo o cero
if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print(f"El número es cero.")


9#
# Solicitar al usuario un año
año = int(input("Introduce un año: "))

# Determinar si el año es bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")


10#
# Solicitar al usuario una longitud en metros y la unidad deseada
metros = float(input("Introduce una longitud en metros: "))
unidad = input("Introduce la unidad a la que deseas convertir (pies, pulgadas, yardas): ").strip().lower()

# Realizar la conversión
if unidad == "pies":
    conversion = metros * 3.28084
elif unidad == "pulgadas":
    conversion = metros * 39.3701
elif unidad == "yardas":
    conversion = metros * 1.09361
else:
    conversion = "Unidad no válida"

print(f"Longitud en {unidad}: {conversion}")


11#
# Solicitar al usuario su peso y altura
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Determinar la categoría del IMC
if imc < 18.5:
    categoria = "bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "normal"
elif 25 <= imc < 29.9:
    categoria = "sobrepeso"
else:
    categoria = "obesidad"

print(f"Tu IMC es {imc:.2f} y tu categoría es: {categoria}")


12#
# Solicitar al usuario un número del 1 al 7
numero = int(input("Introduce un número del 1 al 7: "))

# Determinar el día de la semana correspondiente
if numero == 1:
    dia = "Lunes"
elif numero == 2:
    dia = "Martes"
elif numero == 3:
    dia = "Miércoles"
elif numero == 4:
    dia = "Jueves"
elif numero == 5:
    dia = "Viernes"
elif numero == 6:
    dia = "Sábado"
elif numero == 7:
    dia = "Domingo"
else:
    dia = "Número no válido"

print(f"El día de la semana correspondiente es: {dia}")


13#
# Solicitar al usuario su edad
edad = int(input("Introduce tu edad: "))

# Determinar si es mayor de edad
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

14#
import random

98# Solicitar al usuario su elección
eleccion_usuario = input("Elige 'piedra', 'papel' o 'tijera': ").strip().lower()

# Generar una elección aleatoria para la computadora
elecciones = ["piedra", "papel", "tijera"]
eleccion_computadora = random.choice(elecciones)

print(f"La computadora eligió: {eleccion_computadora}")

# Determinar el ganador
if eleccion_usuario == eleccion_computadora:
    resultado = "Empate"
elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
     (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
     (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
    resultado = "Ganaste"
else:
    resultado = "Perdiste"

print(f"Resultado: {resultado}")


15#
# Solicitar al usuario un número de teléfono de 10 dígitos
numero = input("Introduce un número de teléfono de 10 dígitos: ")

# Dar formato al número
if len(numero) == 10 and numero.isdigit():
    formato = f"({numero[:3]}) {numero[3:6]}-{numero[6:]}"
    print(f"El número de teléfono con formato es: {formato}")
else:
    print("Número de teléfono no válido. Debe tener 10 dígitos.")


#lab04#

1#
# Solicitar al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Inicializar la suma
suma = 0
i = 2

# Calcular la suma de números pares desde 2 hasta 'n' (inclusive)
while i <= n:
    suma += i
    i += 2

print("La suma de todos los números pares desde 2 hasta", n, "es", suma)


2#
# Solicitar al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Imprimir la secuencia de la conjetura de Collatz
print("Secuencia de Collatz:")
while n != 1:
    print(n, end=' ')
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
print(n)  # Imprime el último número, que será 1


3#
# Solicitar al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Imprimir la tabla de multiplicar del número 'n'
print(f"Tabla de multiplicar de {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


4#
# Solicitar al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Imprimir un triángulo de asteriscos con 'n' filas
for i in range(1, n + 1):
    print('*' * i)


5#
# Solicitar al usuario una frase
frase = input("Introduce una frase: ")

# Inicializar el contador de vocales
vocales = "aeiouAEIOU"
contador = 0

# Contar el número total de vocales en la frase
for caracter in frase:
    if caracter in vocales:
        contador += 1

print("Número total de vocales en la frase:", contador)


6#
# Solicitar al usuario un número entero positivo
numero = int(input("Introduce un número entero positivo: "))

# Inicializar la suma de dígitos
suma_digitos = 0

# Calcular la suma de los dígitos
while numero > 0:
    suma_digitos += numero % 10
    numero //= 10

print("La suma de los dígitos es:", suma_digitos)


7#
# Solicitar al usuario una cadena
cadena = input("Introduce una cadena: ")

# Inicializar la cadena invertida
cadena_invertida = ""

# Invertir la cadena
for caracter in cadena:
    cadena_invertida = caracter + cadena_invertida

print("La cadena invertida es:", cadena_invertida)


8#
# Solicitar al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Inicializar los primeros dos números de Fibonacci
a, b = 0, 1

# Calcular el enésimo número de Fibonacci
for _ in range(n - 1):
    a, b = b, a + b

print(f"El {n}-ésimo número de Fibonacci es:", a)


9#
# Solicitar al usuario una cadena
cadena = input("Introduce una cadena: ")

# Inicializar la variable para verificar si es palíndromo
es_palindromo = True

# Verificar si la cadena es palíndromo
for i in range(len(cadena) // 2):
    if cadena[i] != cadena[-i - 1]:
        es_palindromo = False
        break

if es_palindromo:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")


10#
# Solicitar al usuario una serie de números separados por comas
entrada = input("Introduce una serie de números separados por comas: ")

# Convertir la entrada en una lista de números
numeros = [float(x) for x in entrada.split(',')]

# Calcular el promedio
suma = 0
for numero in numeros:
    suma += numero

promedio = suma / len(numeros)
print("El promedio de los números es:", promedio)


#lab05#

1#
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

edades.sort()  # Ordenar la lista
edad_minima = edades[0]
edad_maxima = edades[-1]

print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)

edades.append(edad_minima)
edades.append(edad_maxima)

print("Lista con edad mínima y máxima añadidas:", edades)


n = len(edades)
if n % 2 == 1:
    edad_mediana = edades[n // 2]
else:
    edad_mediana = (edades[n // 2 - 1] + edades[n // 2]) / 2

print("Edad mediana:", edad_mediana)


rango = edad_maxima - edad_minima
print("Rango de edades:", rango)


edades_set = set(edades)
print("Conjunto de edades:", edades_set)


promedio = sum(edades) / len(edades)

# Comparar (mínimo - promedio) y (máximo - promedio)
comparacion_min = abs(edad_minima - promedio)
comparacion_max = abs(edad_maxima - promedio)

print("Comparación mínimo - promedio:", comparacion_min)
print("Comparación máximo - promedio:", comparacion_max)


2#
frase = "Soy profesor y me encanta inspirar y enseñar a la gente"

# Convertir la frase en un conjunto de palabras únicas
palabras = set(frase.split())

print("Número de palabras únicas:", len(palabras))


3#
lista1 = list(range(1, 11))
lista2 = list(range(5, 16))
lista3 = list(range(10, 21))


conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)

interseccion = conjunto1 & conjunto2 & conjunto3
print("Números presentes en las tres listas:", interseccion)


union = conjunto1 | conjunto2 | conjunto3
print("Números presentes en al menos una lista:", union)


diferencia = conjunto1 - conjunto3
print("Números presentes en la primera lista pero no en la última:", diferencia)


conjunto1_tupla = tuple(conjunto1)
conjunto3_tupla = tuple(conjunto3)

# Asegurarse de que las tuplas no estén vacías
if conjunto1_tupla:
    suma1 = conjunto1_tupla[0] + conjunto1_tupla[-1]
    print("Suma del primer y último elemento de la primera lista:", suma1)

if conjunto3_tupla:
    suma3 = conjunto3_tupla[0] + conjunto3_tupla[-1]
    print("Suma del primer y último elemento de la última lista:", suma3)


4#
l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)]
l2 = [("one", 1), ("two", 2), ("six", 6)]


s1 = set(l1)
s2 = set(l2)

print("Conjunto s1:", s1)
print("Conjunto s2:", s2)

s3 = s1 & s2
print("Elementos comunes a s1 y s2:", s3)


s4 = s1 ^ s2
print("Elementos únicos para s1 y s2:", s4)


l3 = sorted(s3.union(s4), key=lambda x: x[1])
print("Lista l3 ordenada por el número entero de cada tupla:", l3)
