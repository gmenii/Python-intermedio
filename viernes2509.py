##Ejercicio 1
"""
def dividir (a, b):
    return a / b

resultado = 0

    
try:
    resultado = dividir(10, 0)
    
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

print(f"El resultado de la división es: {resultado}") 
"""

##Ejercicio 2
"""
def sumar(a, b):
    return a + b

resultado = 0

try:
    resultado = sumar(5, "hola amigos")

except TypeError:
    print("Error: No se puede sumar un número y una cadena de texto.")

print(f"El resultado de la suma es: {resultado}")
"""

###Ejercicio 3
"""
diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

try:
    print(diccionario["apellido"])

except KeyError:
    print("Error: La clave 'apellido' no existe en el diccionario.")

else: 
    print(f"La clave 'apellido' es: {diccionario['apellido']}.")
"""

###Ejercicio 4
"""
try:
    archivo = open("archivo.txt", "r")
    print("El archivo se abrió correctamente.")

except FileNotFoundError:
    print("Error: El archivo no existe.")
    archivo = open("archivo.txt", "w")

print("El archivo fue creado correctamente.")

"""

##Ejercicio 5
"""
def dividir(a, b):
    return a / b

try:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    resultado = dividir(numero1, numero2)

except ValueError:
    print("Error: Debe ingresar números válidos.")

except ZeroDivisionError:
    print("Error: No se puede dividir por 0.")

else:
    print(f"El resultado de la división es: {resultado}")

finally:
    print("Fin del programa")

"""