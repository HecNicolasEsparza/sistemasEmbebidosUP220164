import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topico = "Casa/Cocina/Temp"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado con el mosquito")
        client.subscribe(topico)
        print(f"suscrito al topic: {topico}")

    else:
        print("Fallo en la conexion, codigo de error: ", rc)
        print("qué triste, no se pudo")

def on_message(client, userdata, msg):
    Mensajito = msg.payload.decode()
    print(f"Mensaje: {Mensajito}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, 30)  #30 segundos para intentar hacer conexión hasta marcar error
client.loop_forever()

