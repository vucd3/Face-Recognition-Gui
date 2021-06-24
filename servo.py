import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(11, gpio.OUT)
servo = gpio.PWM(11, 50)

servo.start(0)

try:
    while True:
        angle = float(input('Enter angle between 0 & 180: '))
        servo.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)

finally:
    time.sleep(2)
    servo.stop()
    gpio.cleanup()


