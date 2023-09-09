import time
inicio = time.time()

for i in range(0,31):
    contador = 0
    for n in range(1, i+1):
        residuo = i%n
        if residuo == 0:
            contador = contador + 1
              
    if contador == 2:
        print(f'{i} es un primo')
        
fin = time.time()
print("tImepo = ", (fin - inicio)*1000)
