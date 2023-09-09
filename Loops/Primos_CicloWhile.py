a = 1
value = input('Ingrese El Valor A Analizar')
value = int(value)

while a == 1:
    for i in range(1,value+1):
        conta = 0
        for n in range(1, i+1):
            residue = i%n
            if residue == 0:
                conta = conta + 1
    if conta == 2:
       print(f'{i} Pertenece A Los Primos')
       print("\n")
    else:
       print(f'{i} No Es Un Primo')
       print("\n")

    print('Para Insertar Otro Valor Ingrese 1')
    a = input()
    a = int(a)

    if a != 1:
        print("A salido De La Operacion")
        break

    value = input('Ingrese un valor')
    value = int(value)
