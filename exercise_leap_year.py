def leap_year():
    """
    Ejercicio 11 (Desafío) - Año Bisiesto

    Leer un año mediante input(). Determinar si es un año bisiesto e imprimir el resultado.
    Un año es bisiesto si:
    - Es divisible por 4, Y
    - NO es divisible por 100, O es divisible por 400

    Ejemplo:
        Para la entrada "2000", la salida esperada es:
        El año 2000 es bisiesto

        Para la entrada "2001", la salida esperada es:
        El año 2001 no es bisiesto

        Para la entrada "1700", la salida esperada es:
        El año 1700 no es bisiesto
    """

    año = int(input())
    divisible_por_4 = año % 4
    divisible_por_400 = año % 400
    divisible_por_100 = año % 100
    if divisible_por_4 == 0:
        if divisible_por_100 != 0 or divisible_por_400 == 0:
            print(f"El año {año} es bisiesto")
        else:
            print(f"El año {año} no es bisiesto")
    else: print(f"El año {año} no es bisiesto")

#leap_year()
