import paho.mqtt.client as mqtt
import json
import time
import random

broker = "192.168.1.12"
port = 1883
topic = "datos"
topicAvisos = "avisos"

def on_connect(Client, userdata, flags, rc):
    if rc == 0:
        print("conectado con el mosquito")
        client.subscribe(topic)
    else:
        print("Fallo en la conexion")
       
def on_message(client, userdata, msg):
    datos = json.loads(msg.payload.decode())
    #ensaje = msg.payload.decode()
    temperatura = datos["temperatura"]
    humedad = datos["humedad"]
    luz = datos["luz"]
    #print(f"temperatura: {temperatura} humedad: {humedad} luz: {luz}")
   
    if luz == "OFF":
        mensaje = json.dumps( {"aviso": "Se ha encendido la luz"} )
        client.publish(topicAvisos, mensaje)
        print("aviso de luz")
   
    if humedad > 55:
        mensaje = json.dumps( {"aviso": "Se ha encendido la secadora"} )
        client.publish(topicAvisos, mensaje)
        print("aviso de humedad")
   
    if temperatura > 25:
        mensaje = json.dumps( {"aviso": "Se ha encendido el ventilador"} )
        client.publish(topicAvisos, mensaje)
        print("aviso de temperatura")
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