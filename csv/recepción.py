import paho.mqtt.client as mqtt
import csv
from datetime import datetime

broker = "192.168.0.141"
port = 1883
topic = "Clase/Salon09A/Temperatura"
archivo_csv = "datos_temperatura.csv"

with open(archivo_csv, mode='w') as file:
    writer =  csv.writer(file)
    writer.writerow(["Fecha", "Topic", "Mensaje"])

def on_Message(client, userdata, msg):
    mensaje = msg.payload.decode()
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Mensaje recibido en {fecha_hora}: {mensaje} de parte de: {broker}")

    with open(archivo_csv, mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([fecha_hora, msg.topic, mensaje, broker])

client = mqtt.Client()
client.connect(broker, port, 60)
client.suscribe(topic)
client.on_message = on_Message
print("guardado en el excel")
client.loop_forever()