import random
import paho.mqtt.client as mqtt
import time

broker = "localhost"
port = 1883
topico = "Casa/Cocina/Temp"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado con el mosquito")
    else:
        print("Error de conexión:", rc)

client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker, port, 60)
client.loop_start() 
try:
    while True:
        temperatura = round(random.uniform(20.0, 30.0), 2)
        client.publish(topico, str(temperatura))
        print(f"Temperatura enviada: {temperatura} °C")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nDesconectando...")
    client.loop_stop()
    client.disconnect()
