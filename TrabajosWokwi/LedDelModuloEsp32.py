#Link: https://wokwi.com/projects/375402504301493249

from machine import Pin
from utime import sleep_ms

ON_BOARD_PIN = 2
led_pin = Pin(ON_BOARD_PIN, Pin.OUT)

while True:
    led_pin.value(not led_pin.value())
    sleep_ms(500)
