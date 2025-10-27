import paho.mqtt.client as mqtt

broker = "192.168.1.12"
port = 1883
topic = "avisos"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado con el mosquito")
        client.subscribe(topic)
        print(f"suscrito al topic: {topic}")

    else:
        print("Fallo en la conexion, codigo de error: ", rc)

def on_message(client, userdata, msg):
    Mensaje = msg.payload.decode()
    print(f"Mensaje: {Mensaje}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, 60)  #60 segundos para intentar hacer conexión hasta marcar error
client.loop_forever()



