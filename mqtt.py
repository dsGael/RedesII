import paho.mqtt.client as mqtt
import time
import json
import random


# Definir los parámetros del broker MQTT
broker_address = "52.206.108.141"
port = 8080
topic = "Invernader"

# Definir la función de callback para cuando se publique un mensaje
def on_publish(client, userdata, result):
    print("Mensaje publicado con éxito!")

# Configurar el cliente MQTT
client = mqtt.Client()
client.on_publish = on_publish

# Conectar al broker MQTT
client.connect(broker_address, port)

# Loop principal
while True:
    # Obtener el mensaje a publicar
    #mensaje = input("Ingrese el mensaje a publicar: ")
    
    humedad = random.randint(0, 100)
    Intensidad = random.randint(0,200)
    Temperatura = random.randint(0,10)
    mensaje = {"Humedad":humedad, "Intensidad":Intensidad, "Temperatura":Temperatura}
    
    mensaje_json = json.dumps(mensaje)
    
    
    # Publicar el mensaje en el tema especificado
    client.publish(topic, mensaje_json)

    # Esperar un segundo antes de la siguiente iteración
    time.sleep(10)