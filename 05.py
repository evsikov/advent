from gpiozero import LED
from gpiozero import Button
from time import sleep

led_18 = LED(18)
led_24 = LED(24)
button_21 = Button(21)

while True:
    led_18.on()
    led_24.off()
    
    # wait for gpio 21
    button_21.wait_for_press()

    sleep(0.2)
    led_18.off()
    led_24.on()
    
    # wait for gpio 21
    button_21.wait_for_press()
    
    sleep(0.2)
