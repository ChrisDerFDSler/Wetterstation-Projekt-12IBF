import time
from machine import Pin, I2C
from bme680 import BME680_I2C
from umqtt.simple import MQTTClient
import network
import ntptime

BROKER = "IP_DEINES_BROKERS"
TOPIC  = b"sensor/bme680/station1"

# WLAN verbinden und NTP-Zeit holen (damit Timestamp UTC stimmt)
# ... WLAN-Code ...
ntptime.settime()

i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=100000)
sensor = BME680_I2C(i2c)

client = MQTTClient("pico-bme680", BROKER)
client.connect()

while True:
    temp = sensor.temperature
    hum  = sensor.humidity
    pres = sensor.pressure
    gas  = sensor.gas  # Rohwert Gaswiderstand
    qualitaet = gas    # hier erst mal direkt Gas als „Qualität“

    ts = time.time()   # UNIX-Timestamp vom Pico (nach NTP)

    payload = "{:.2f};{:.2f};{:.2f};{};{}".format(
        temp, hum, pres, int(qualitaet), int(ts)
    )
    client.publish(TOPIC, payload)
    time.sleep(10)
