# EJERCICIO 1
def ejercicio_1():
    print("\n--- Ejercicio 1: Mayor de dos números ---")
    numero1 = float(input("Ingresá el primer número: "))
    numero2 = float(input("Ingresá el segundo número: "))

    mayor = numero1 if numero1 > numero2 else numero2
    print("El mayor es:", mayor)


# EJERCICIO 2
def buscar_palabra(palabra_buscada, *palabras):
    mensaje = "La palabra está en la lista." if palabra_buscada in palabras else "La palabra no está en la lista."
    return mensaje


def ejercicio_2():
    print("\n--- Ejercicio 2: Buscar una palabra ---")
    entrada = input("Ingresá palabras separadas por comas: ")
    palabras = [palabra.strip() for palabra in entrada.split(",") if palabra.strip()]

    buscada = input("¿Qué palabra querés buscar?: ").strip()
    resultado = buscar_palabra(buscada, *palabras)
    print(resultado)


# EJERCICIO 3
def ejercicio_3():
    print("\n--- Ejercicio 3: Par o impar ---")
    numero = int(input("Ingresá un número entero: "))

    resultado = "par" if numero % 2 == 0 else "impar"
    print(f"El número {numero} es {resultado}.")


# EJERCICIO 4
def calcular_promedio(*numeros):
    promedio = sum(numeros) / len(numeros) if len(numeros) > 0 else None
    return promedio


def ejercicio_4():
    print("\n--- Ejercicio 4: Promedio de números ---")
    entrada = input("Ingresá números separados por comas: ")

    try:
        numeros = [float(numero.strip()) for numero in entrada.split(",") if numero.strip()]
    except ValueError:
        print("Error: ingresá solamente números separados por comas.")
        return

    promedio = calcular_promedio(*numeros)
    mensaje = f"El promedio es: {promedio}" if promedio is not None else "Error: tenés que ingresar al menos un número."
    print(mensaje)


# EJERCICIO 5
def mostrar_argumentos_suficientes(*args):
    if len(args) < 2:
        print("Error: se necesitan al menos 2 argumentos.")
    else:
        print("Argumentos recibidos:", args)


def ejercicio_5():
    print("\n--- Ejercicio 5: Validar cantidad de argumentos ---")
    entrada = input("Ingresá dos o más valores separados por comas: ")
    argumentos = [valor.strip() for valor in entrada.split(",") if valor.strip()]
    mostrar_argumentos_suficientes(*argumentos)


def main():
    print("PRÁCTICA CLASE 4 - OPERADORES TERNARIOS")
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()
    ejercicio_5()
    print("\nPráctica finalizada.")


if __name__ == "__main__":
    main()
