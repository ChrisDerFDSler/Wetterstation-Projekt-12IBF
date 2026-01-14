import time
from machine import Pin, I2C
from bme680 import BME680_I2C # Stelle sicher, dass diese Bibliothek auf deinem Pico W installiert ist
# --- KONFIGURATION (Nur I2C) ---
# I2C-Pins für den BME680
# GP4/SDA, GP5/SCL (Typische Pins für I2C 0 auf dem Pico)
I2C_SDA_PIN = 4
I2C_SCL_PIN = 5
# --- INITIALISIERUNG ---
# I2C-Bus 0 initialisieren
try:
    i2c = I2C(0, sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=100000)
    
    # Prüfen, ob der BME680 am I2C-Bus gefunden wird (Adresse 0x76 oder 0x77)
    devices = i2c.scan()
    if not devices:
        print("❌ FEHLER: Keine I2C-Geräte gefunden. Prüfe die Verkabelung.")
    elif 118 not in devices and 119 not in devices: # Dezimal 118=0x76, 119=0x77
        print("❌ FEHLER: BME680 nicht gefunden (erwartet 0x76/0x77). Gefunden:", [hex(d) for d in devices])
    else:
        print("✅ I2C-Verbindung erfolgreich. Gefundene Geräte:", [hex(d) for d in devices])
    
    # BME680-Sensor initialisieren
    sensor = BME680_I2C(i2c)
    print("✅ BME680-Sensor initialisiert.")
except Exception as e:
    print(f"❌ Initialisierungsfehler: {e}")
    # Endlosschleife, falls die Initialisierung fehlschlägt
    while True:
        time.sleep(10)
# --- HAUPT-LOOP ZUM LESEN ---
print("\nStarte Messwert-Ausgabe. Warte 3 Sekunden auf die erste Messung...")
while True:
    try:
        # Werte über die Properties abrufen
        temp = sensor.temperature
        hum = sensor.humidity
        pres = sensor.pressure
        gas = sensor.gas
        # Werte auf der Konsole ausgeben
        print("-----------------------------")
        print("📊 Sensorwerte BME680:")
        print("🌡 Temperatur: {:.2f} °C".format(temp))
        print("💧 Feuchtigkeit: {:.2f} %".format(hum))
        print("⚙️ Druck: {:.2f} hPa".format(pres))
        print("💨 Gaswiderstand: {} Ohm".format(gas))
        
        
    except Exception as e:
        print(f"❌ Fehler beim Lesen der Sensorwerte: {e}")
    # Wartezeit vor der nächsten Messung
    time.sleep(1) # Lese alle 10 Sekunden