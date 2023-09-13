#Link: https://wokwi.com/projects/375404115405034497

from machine import Pin, PWM, ADC
import time

pinPot = ADC(Pin(26))

pinLed = PWM(Pin(22))

while True:
    BRILLO = pinPot.read()

    BRILLO = int(BRILLO / 16.2)
    print("brillo:",BRILLO)

    pinLed.duty(BRILLO)

    time.sleep(1)
