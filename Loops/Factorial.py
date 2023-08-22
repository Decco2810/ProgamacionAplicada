while True:

    value = int(input("Introduzca un valor entero positivo: "))
    print("Valor: ", value)
    a = isinstance(value, int)
    if a == True and value > 0:
        fact = 1
        for i in range (1, value + 1):
            fact = fact*i            
        print(f'Un factorial De {value} es: ', fact)
    else:
        print("El numero que ingreso no es entero o no es positivo")
