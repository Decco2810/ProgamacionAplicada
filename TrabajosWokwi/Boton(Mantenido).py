#Link: https://wokwi.com/projects/375804409906128897
import time
import machine
from machine import Pin

led = Pin(21,Pin.OUT)
button = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if button.value() == 0 :
       led.value(1)
    else :
        led.value(0)
