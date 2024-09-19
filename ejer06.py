import random
import string

def generar_contraseña(longitud):
    if longitud < 8:
        raise ValueError("La longitud de la contraseña debe ser al menos 8 caracteres.")

    # Definir los conjuntos de caracteres
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiales = string.punctuation

    # Asegurarse de que la contraseña incluya al menos un carácter de cada tipo
    contraseña = [
        random.choice(letras_mayusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiales)
    ]

    # Rellenar el resto de la contraseña con caracteres aleatorios
    todos_los_caracteres = letras_mayusculas + letras_minusculas + numeros + caracteres_especiales
    contraseña += random.choices(todos_los_caracteres, k=longitud - 4)

    # Mezclar los caracteres de la contraseña
    random.shuffle(contraseña)

    # Convertir la lista de caracteres a una cadena
    return ''.join(contraseña)

# Ejemplo de uso
longitud = int(input("Ingrese la longitud deseada para la contraseña (mínimo 8): "))
try:
    contraseña_generada = generar_contraseña(longitud)
    print("Contraseña generada:", contraseña_generada)
except ValueError as e:
    print(e)
