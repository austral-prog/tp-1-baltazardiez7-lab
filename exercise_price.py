def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100
    impuesto = precio_base/100 *21
    print (impuesto)
    subtotal1= precio_base+impuesto
    print (subtotal1)
    propina = subtotal1/100 *10
    print (propina)
    print (subtotal1+propina)
