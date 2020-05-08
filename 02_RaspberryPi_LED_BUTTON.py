import RPi.GPIO as GPIO
import time

LED_PIN=2
BUTTON_PIN=3

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(BUTTON_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
Led_status=0
GPIO.output(LED_PIN,GPIO.LOW)

while True:
    button=GPIO.input(BUTTON_PIN)
    if button==0 and Led_status==0:
        GPIO.output(LED_PIN,GPIO.HIGH)
        Led_status=1
    elif button==0 and Led_status==1:
        GPIO.output(LED_PIN,GPIO.LOW)
        Led_status=0
    if(Led_status == 0):
        print("LED OFF")
    if(Led_status == 1):
        print("LED ON")
        GPIO.output(LED_PIN,Led_status)
    time.sleep(0.2)
    
