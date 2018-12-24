from gpiozero import LED
from time import sleep

led_18 = LED(18)
led_24 = LED(24)

while True:
    led_18.on()
    led_24.off()
    sleep(0.5)
    led_18.off()
    led_24.on()
    sleep(0.5)
