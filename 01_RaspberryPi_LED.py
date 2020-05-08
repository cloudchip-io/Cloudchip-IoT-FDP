import RPi.GPIO as GPIO
import time

LED_PIN=18
# for GPIO numbering, choose BCM 
GPIO.setmode(GPIO.BCM)

# or, for pin numbering, choose BOARD  
#GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED_PIN,GPIO.OUT)

while True:
     print("LED ON")
     GPIO.output(18,GPIO.HIGH)
     time.sleep(1)
     print("LED OFF")
     GPIO.output(18,GPIO.LOW)
     time.sleep(1)