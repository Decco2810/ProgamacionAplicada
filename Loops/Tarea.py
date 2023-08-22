a = input("Ingrese Numero A: ")
a = int(a)
b = input("Ingrese Numero B: ")
b = float(b)
c = a + b

if a == b:
    print("Los numeros son iguales")
else:
    print("Los numeros son diferentes")

print("A es un numero de tipo: ", type(a))
print("B es un numero de tipo: ", type(b))
print("c = ", c)

if type(a) == type(b):
    print("A y B son del mismo tipo")
else:
    print("A y B son de diferente tipo")