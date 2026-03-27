def discount():
    """
    Ejercicio 9 (Integrador) - Sistema de Descuentos

    Crear un sistema de descuentos para una tienda. Leer mediante input():
    1. El precio unitario de un producto (decimal)
    2. La cantidad de unidades a comprar (entero)

    Calcular el total aplicando los siguientes descuentos según la cantidad:
    - Si compra 10 o más unidades: 20% de descuento
    - Si compra entre 5 y 9 unidades: 10% de descuento
    - Si compra menos de 5 unidades: sin descuento

    Imprimir:
    1. El subtotal (precio × cantidad)
    2. El porcentaje de descuento aplicado
    3. El monto del descuento
    4. El total final

    Ejemplo:
        Para las entradas "100" y "12", la salida esperada es:
        Subtotal: 1200.0
        Descuento aplicado: 20%
        Monto de descuento: 240.0
        Total final: 960.0
    """
    
    precio = float(input())
    cantidad = int(input())
    subtotal = float(precio * cantidad)

    if cantidad >= 10:
        num_descuento= "20%"
        descuento= subtotal * (20/100)
    elif cantidad >= 5 and cantidad <= 9:
        num_descuento="10%"
        descuento= subtotal * (10/100)
    else: 
        descuento = 0
        num_descuento = "0%"

    total= subtotal - descuento
    print("Subtotal:",subtotal)
    print("Descuento aplicado:",num_descuento)
    print("Monto de descuento:",float(descuento))
    print("Total final:",total)

#discount()
