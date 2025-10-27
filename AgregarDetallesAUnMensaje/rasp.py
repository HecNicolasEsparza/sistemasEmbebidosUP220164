import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime

broker = "192.168.1.12"
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
    emisor = datos["Emisor"]
    contenido = datos["Mensaje"]
 
    #print(f"temperatura: {temperatura} humedad: {humedad} luz: {luz}")
   
    hora_actual = datetime.now().strftime("%H:%M:%S")
    mensaje = json.dumps( {"emisor": str(emisor), "mensaje": str(contenido), "hora": str(hora_actual)} )
    client.publish(topicAvisos, mensaje)
    print(f"mensaje enviado {mensaje}")
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
