import paho.mqtt.client as mqtt 

import mysql.connector 

from datetime import datetime 

  

# MQTT 

broker_address = "localhost" 

topic = "test" 

  

# MySQL Zugangsdaten muss nur gemacht werden wenn keine DB vorhanden ist 

db_config = { 

    "host": "localhost", 

    "user": "root",          # muss angepasst werden 

    "password": "",          # muss angepasst werden 

    "database": "mqtt_db"    # "" 

} 

  

# MySQL Verbindung 

conn = mysql.connector.connect(**db_config) 

cursor = conn.cursor() 

  

def on_connect(client, userdata, flags, rc): 

    if rc == 0: 

        print("Verbunden zum Broker!") 

        client.subscribe(topic) 

        print(f"Abonniere Topic: {topic}") 

    else: 

        print(f"Verbindung fehlgeschlagen mit Code {rc}") 

  

def on_message(client, userdata, message): 

    msg_text = message.payload.decode() 

    topic_name = message.topic 

    timestamp = datetime.now() 

  

    print(f"Nachricht erhalten: {msg_text} auf Topic {topic_name} um {timestamp}") 

  

    # Nachricht in MySQL speichern 

    cursor.execute( 

        "INSERT INTO messages (topic, message, timestamp) VALUES (%s, %s, %s)", 

        (topic_name, msg_text, timestamp) 

    ) 

    conn.commit() 

  

# MQTT Client 

client = mqtt.Client() 

client.on_connect = on_connect 

client.on_message = on_message 

  

client.connect(broker_address, 1883) 

  

try: 

    client.loop_forever() 

except KeyboardInterrupt: 

    print("Beende Programm...") 

finally: 

    cursor.close() 

    conn.close() 

 