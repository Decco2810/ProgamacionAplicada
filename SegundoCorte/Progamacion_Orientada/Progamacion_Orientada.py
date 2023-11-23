#--------------CIRCULO----------------
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creando un círculo con un diámetro de {d}".format(d=diameter))
        self.radio = diameter / 2

    def circunferencia(self):
        return 2 * self.pi * self.radio

    def area(self):
        return self.pi * self.radio**2

    def perimetro(self):
        return 2 * self.pi * self.radio

Pizza_Mediana = Circle(12)
Mesa_De_Enseñanza = Circle(36)
Sala_Redonda = Circle(11460)

print("Circunferencia pizza mediana:\n", Pizza_Mediana.circunferencia())
print("Área de la pizza mediana: \n", Pizza_Mediana.area())
print("Perímetro pizza mediana:\n", Pizza_Mediana.perimetro())

print("Circunferencia de la mesa de enseñanza:\n", Mesa_De_Enseñanza.circunferencia())
print("Área de la mesa de enseñanza:\n", Mesa_De_Enseñanza.area())
print("Perímetro de la mesa de enseñanza:\n", Mesa_De_Enseñanza.perimetro())

print("Circunferencia de la sala redonda:\n", Sala_redonda.circunferencia())
print("Área de la sala redonda:\n", Sala_Redonda.area())
print("Perímetro de la sala redonda:\n", Sala_Redonda.perimetro())

#*-------------- TRIANGULO RECTANGULO-----------------------------------------------
class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return area

    def calcular_perimetro(self):
        hipotenusa = (self.base ** 2 + self.altura ** 2) ** 0.5
        perimetro = self.base + self.altura + hipotenusa
        return perimetro

base = float(input("Ingresa la longitud de la base del triángulo: "))
altura = float(input("Ingresa la longitud de la altura del triángulo: "))

triangulo = TrianguloRectangulo(base, altura)

area = triangulo.calcular_area()
perimetro = triangulo.calcular_perimetro()

print("Área del triángulo rectángulo:", area)
print("Perímetro del triángulo rectángulo:", perimetro)

#-----------------RECTANGULO--------------------------------------
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area

    def calcular_perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        return perimetro

base = float(input("INGRESE LA LONGITU DE LA BASE: "))
altura = float(input("INGRESE LA ALTURA DEL TRIANGULO: "))

rectangulo = Rectangulo(base, altura)

area = rectangulo.calcular_area()
perimetro = rectangulo.calcular_perimetro()

print("Área Rectangular:", area,"cm cuadrados")
print("Perímetro del rectángulo:", perimetro,"cm")

#------------------CUADRADO-------------------------
class Cuadrado:
    def __init__(self, Base):
        self.Base = Base

    def calcular_area(self):
        Area = self.Base * self.Base
        return Area

    def calcular_perimetro(self):
        perimetro = 2 * (self.Base + self.Base)
        return perimetro

Base = float(input("Ingresa la longitud de una de las aristas del Cuadrado: "))

Cuadrado = Cuadrado(Base)

Area = Cuadrado.calcular_area()
perimetro = Cuadrado.calcular_perimetro()

print("Área del Cuadrado:", Area,"cm cuadrados")
print("Perímetro del Cuadrado:", perimetro,"cm")
