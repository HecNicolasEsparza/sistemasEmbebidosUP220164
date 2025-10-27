import paho.mqtt.client as mqtt
import time
import random

broker = "localhost"
port = 1883
topic = "Casa/Cocina/Temp"
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
        temperatura = round(random.uniform(20.0, 30.0), 2)
        client.publish(topic, str(temperatura))
        time.sleep(2)

except KeyboardInterrupt:
    print("Desconectado")
    client.loop_stop()
    client.disconnect()
    print("Desconectado del broker")