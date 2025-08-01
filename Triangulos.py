def solicitar_lado(nombre):
    """
    Solicita un valor positivo de tipo float para el lado del triángulo.
    :param nombre: Nombre del lado (ej. 'A', 'B', 'C')
    :return: Valor float positivo del lado
    """
    while True:
        entrada = input(f"Ingrese el lado {nombre} del triángulo: ")
        try:
            valor = float(entrada)
            if valor <= 0:
                print("Error: El valor debe ser un número positivo y mayor a 0.")
                continue
            return valor
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número válido.")


def determinar_tipo_triangulo(a, b, c):
    """
    Determina el tipo de triángulo en base a sus lados.
    :param a: Lado A
    :param b: Lado B
    :param c: Lado C
    :return: String con el tipo de triángulo o mensaje de error si no es válido
    """
    # Verifica si los lados forman un triángulo válido
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Los valores ingresados no forman un triángulo válido."

    if a == b == c:
        return "El triángulo es EQUILÁTERO."
    elif a == b or a == c or b == c:
        return "El triángulo es ISÓSCELES."
    else:
        return "El triángulo es ESCALENO."


def main():
    print("=== Verificador de Tipo de Triángulo ===")
    lado_a = solicitar_lado('A')
    lado_b = solicitar_lado('B')
    lado_c = solicitar_lado('C')

    tipo = determinar_tipo_triangulo(lado_a, lado_b, lado_c)
    print(tipo)


if __name__ == "__main__":
    main()
