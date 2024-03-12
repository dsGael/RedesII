import paho.mqtt.client as mqtt
import time
import json
import random


# Definir los parámetros del broker MQTT
broker_address = "10.10.222.150"
port = 1883
topic = "Invernadero"

# Definir la función de callback para cuando se publique un mensaje
def on_publish(client, userdata, result): 
    print("Mensaje publicado con éxito!")

# Configurar el cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1 , "elpapu25")
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
    
    #mensaje = {"Humedad":humedad, "Intensidad":Intensidad, "Temperatura":Temperatura}
    list=["Humedad","Intensidad","Temperatura"]
    sensor=random.choice(list)
    mensaje = {"Sensor":"Humedad","Valor":humedad}
    mensaje2={"Sensor":"Temperatura","Valor":Temperatura}
    msg3={"Sensor":"Instensidad","Valor":Intensidad}
    mensajes={"Mensaje1":mensaje,"Mensaje2":mensaje2,"Mensaje3":msg3}
    for mensaje in mensajes:
        k=
    mensaje_json = json.dumps(mensaje)
    
    # Publicar el mensaje en el tema especificado
    client.publish(topic, mensaje_json) 

    # Esperar n segundos antes de la siguiente iteración
    time.sleep(10)