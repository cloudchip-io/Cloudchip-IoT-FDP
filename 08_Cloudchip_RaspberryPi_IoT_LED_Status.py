import paho.mqtt.client as mqtt
import json
import RPi.GPIO as GPIO
import time

HOST = 'www.cloudchip.io'
TOKEN='*****************'
LED_PIN=2
BUTTON_PIN=3

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(BUTTON_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)

client=mqtt.Client()
client.username_pw_set(TOKEN)
client.connect(HOST,1883,60)
client.loop_start()

Led_status=0
GPIO.output(LED_PIN,GPIO.LOW)
data={"value":0,"test":95}#
while True:
    button=GPIO.input(BUTTON_PIN)
    if button==0 and Led_status==0:
        GPIO.output(LED_PIN,GPIO.HIGH)
        Led_status=1
    elif button==0 and Led_status==1:
        GPIO.output(LED_PIN,GPIO.LOW)
        Led_status=0
    if(Led_status == 0):
        data['value']=0
        print("LED OFF")
        client.publish('v1/devices/me/telemetry',json.dumps(data),0)
    if(Led_status == 1):
        data['value']=1
        print("LED ON")
        client.publish('v1/devices/me/telemetry',json.dumps(data),1)
        GPIO.output(LED_PIN,Led_status)
    time.sleep(0.2)
    
