import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)




broker = "192.168.0.170"
port = 1883
topic = "mensaje"
topicAvisos = "mensajeDetallado"

def on_connect(Client, userdata, flags, rc):
    if rc == 0:
        print("conectado con el mosquito")
        client.subscribe(topic)
    else:
        print("Fallo en la conexion")
       
def on_message(client, userdata, msg):
    datos = json.loads(msg.payload.decode())
    #ensaje = msg.payload.decode()
    Color = datos["Color"]
   
 
    #print(f"temperatura: {temperatura} humedad: {humedad} luz: {luz}")
   
   
    #ensaje = json.dumps( {"color": str(Color)} )
    #client.publish(topicAvisos, mensaje)
   
   
    if Color == 'azul':
        print("Junue")
        GPIO.output(21, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(21,GPIO.HIGH)
       
   
    if Color == 'rojo':
        print("Edith")
        GPIO.output(21, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20,GPIO.HIGH)
       
       
    if Color == 'verde':
        print("Mau")
        GPIO.output(21, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(16,GPIO.HIGH)
       
   
    if Color == 'blanco':
        print("Nico")
        GPIO.output(21, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(21,GPIO.HIGH)
        GPIO.output(20,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
       
       
   
    print(datos)
   
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, 60)
client.loop_forever()
       
client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker, port, 60)
client.loop_start()