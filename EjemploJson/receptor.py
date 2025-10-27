import paho.mqtt.client as mqtt
import json

#broker = "localhost"
port = 1883
#topic = "Casa/Cocina/Temp"
broker = "10.73.180.24"
topic = "Clase/Salon09A/Hector_Esparza"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado con el mosquito")
        client.subscribe(topic)
        print(f"suscrito al topic: {topic}")

    else:
        print("Fallo en la conexion, codigo de error: ", rc)

def on_message(client, userdata, msg):
    #datos = json.loads(msg.payload.decode())
    datos = msg.payload.decode()
    saludo= datos["saludo"]
    persona = datos["persona"]
    print(f"saludo: {saludo}  persona: {persona}")
    print(datos)
   
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, 60)  #60 segundos para intentar hacer conexión hasta marcar error
client.loop_forever()

