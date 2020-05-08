

import paho.mqtt.client as mqtt
import json
import time
import random

HOST = 'www.cloudchip.io'
TOKEN='XXXXXXX'

client=mqtt.Client()
client.username_pw_set(TOKEN)
client.connect(HOST,1883,60)
client.loop_start()
data={"LED":"ON"}

while True:
  
    if data['LED'] == 'ON':
        data['LED'] = 'OFF'
    elif data['LED'] == 'OFF':
        data['LED'] = 'ON'
    
   
    client.publish('v1/devices/me/telemetry',json.dumps(data),0)
    print(data);
    time.sleep(1)
    
