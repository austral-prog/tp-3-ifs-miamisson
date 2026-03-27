def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    
    contraseña = input()
    if len(contraseña) >= 8:
        cantidad_caracteres = True
    else:
        cantidad_caracteres = False

    
    if "0" in contraseña or "1" in contraseña or "2" in contraseña or "3" in contraseña or "4" in contraseña or "5" in contraseña or "6" in contraseña or "7" in contraseña or "8" in contraseña or "9" in contraseña:
        hay_numero = True
    else:
        hay_numero = False

    if cantidad_caracteres == True and hay_numero == True:
        print("Contraseña valida")
    elif cantidad_caracteres == False and hay_numero == True:
        print("Contraseña muy corta")
    elif cantidad_caracteres == True and hay_numero == False:
        print("Debe contener un numero")
    else: 
        print("Contraseña muy corta")
        print("Debe contener un numero")


#password()
