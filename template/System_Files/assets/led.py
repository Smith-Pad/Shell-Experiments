## Import the Library
from gpiozero import LED

## SPECIFY THE LED PORT

led = LED(17)


## If it is true, then turn on the LED
## and generate a log file telling that
## it is working

while True: 
        led.on()                ## Turn the LED ON
