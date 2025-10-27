import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topico = "Casa/Cocina/Temp"

def on_connect(client, userdata, flags, rc):
    
    temperatura = 22.5
    client.publish(topico, str(temperatura))
    print("Conectado con el mosquito")


client = mqtt.Client()

client.on_connect = on_connect

client.connect(broker, port, 60)

client.loop_forever()

