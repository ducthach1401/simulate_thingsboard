import paho.mqtt.client as mqtt
import random
import time
import json
import sys

#define thingsboard
host = "localhost"
port = 1883
token = sys.argv[1]
sensor_data = {'temperature': 0, 'humidity': 0}
sleep_time = 1

#setup mqtt
client = mqtt.Client()
client.username_pw_set(token)
client.connect(host, port, keepalive = 60)
client.loop_start()

#send data
try:
    while True:
        sensor_data['temperature'] = random.randint(20,35)
        sensor_data['humidity'] = random.randint(50,100)
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
        time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()