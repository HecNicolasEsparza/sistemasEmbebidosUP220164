import paho.mqtt.client as mqtt
import json
import time
import random

#broker = "localhost"
broker = "192.168.1.170"
port = 1883
#topic = "Casa/Cocina/Temp"
topic = "mensaje"
intervalo = 2

def on_connect(Client, userdata, flags, rc):
    if rc == 0:
        print("Conectado con el mosquito")
    else:
        print("Fallo en la conexion, codigo de error: ", rc)

client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker, port, 60)  #60 segundos para intentar hacer conexión hasta marcar error
client.loop_start()

try: 
    while True:
        datos = {
            "Mensaje": random.choice(["ok", "warning", "report"]),
        }
        mensaje = json.dumps(datos)
        client.publish(topic, mensaje)
        print(f"enviado: {mensaje}")
        time.sleep(2)

except KeyboardInterrupt:
    print("Desconectado")
    client.loop_stop()
    client.disconnect()
    print("Desconectado del broker")

#sudo nano etc/mosquitto/mosquito.conf