import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topics = [
    "Universidad/Edificio/Temperatura", 
    "Universidad/Edificio/Movimiento", 
    "MaquinaExpendedora/Ingreso/Billete", 
    "MaquinaExpendedora/Ingreso/Moneda"
]
values = ["23c", "False", "$20", "$5"]

def on_connect(client, userdata, flags, rc):
    print("Conectado con el mosquito")
    # Publicar todos los topics al conectarse
    for t, v in zip(topics, values):
        client.publish(t, v)
        print(f"Publicado {v} en {t}")

client = mqtt.Client()
client.on_connect = on_connect

client.connect(broker, port, 60)
client.loop_forever()
