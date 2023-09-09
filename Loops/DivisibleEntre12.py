RangoMe = input("ingrese valor menor del rango a analisar")
RangoMe = (int(RangoMe))
RangoMa = input("ingrese valor mayor del rango a analisar")
RangoMa = (int(RangoMa))

for i in range(RangoMe, RangoMa):
    if (i%12) != 0:
        continue
    print(i)
