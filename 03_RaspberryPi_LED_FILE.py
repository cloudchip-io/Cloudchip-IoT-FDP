import RPi.GPIO as GPIO
import time
from datetime import datetime
LED_PIN=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)

while True:
    
    #create file and keep the ON time & OFF time {"LED_ON":"14:36:00","LED_OFF":"14:36:20"}
    
    f=open('led.config') 
    fc=eval(f.read())
    print(fc)
    t=datetime.now().strftime("%X")
    print(t)
    if(t==fc['LED_ON']):
        print("LED ON")
        GPIO.output(LED_PIN,GPIO.HIGH)
    if(t==fc['LED_OFF']):
        print("LED OFF")
        GPIO.output(LED_PIN,GPIO.LOW)
    time.sleep(1)