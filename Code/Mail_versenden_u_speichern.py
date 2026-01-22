import time
import paho.mqtt.client as mqtt
import smtplib
from email.message import EmailMessage

broker_address = "localhost"
topic = "sensor/bme680/station1"

SMTP_HOST = "smtp.fds-limburg.schule"
SMTP_USER = "c.froehlich"
SMTP_PASS = "GEHEIM"
TO_ADDR   = "ZIEL@fds-limburg.schule"

letzter_payload = "Noch kein Wert"

def send_mail(payload):
    global letzter_payload
    letzter_payload = payload
    try:
        temp_s, hum_s, pres_s, qual_s, ts_s = payload.split(";")
        text = (
            f"Messung:\n"
            f"Temperatur: {temp_s} °C\n"
            f"Feuchte: {hum_s} %\n"
            f"Druck: {pres_s} hPa\n"
            f"Qualität: {qual_s}\n"
            f"Timestamp: {ts_s}\n"
        )
    except:
        text = f"Rohdaten: {payload}"

    msg = EmailMessage()
    msg['Subject'] = 'BME680 Messwerte'
    msg['From'] = f"{SMTP_USER}@fds-limburg.schule"
    msg['To'] = TO_ADDR
    msg.set_content(text)

    with smtplib.SMTP_SSL(SMTP_HOST) as smtp:
        smtp.login(SMTP_USER, SMTP_PASS)
        smtp.send_message(msg)
    print("E-Mail gesendet")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Verbunden, abonniere:", topic)
        client.subscribe(topic)

def on_message(client, userdata, message):
    global letzter_payload
    letzter_payload = message.payload.decode()
    print("MQTT:", letzter_payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, 1883)
client.loop_start()

try:
    while True:
        send_mail(letzter_payload)
        time.sleep(600)  # alle 10 Minuten
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
