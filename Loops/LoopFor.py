import time

cadenaString = 'Progamacion Orientada A Objetos'

for letra in cadenaString:
   if letra == 'o':
      continue
   print(letra)
   time.sleep(1)
