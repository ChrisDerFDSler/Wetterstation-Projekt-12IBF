# Dies ist ein Schulprojekt der FDS-Limburg der Klasse 12IBF


Hardware die wie für die Testumgebung brauchen:

- BME680 Sensor
- Pi 400
- Raspberry Pi

Was am Ende fertig sein sollte
Pi(400):
- MQTT Broker (Mosquitto)
- LAMP-Server (XAMPP auf Linux)
  > Apache/Webserver,
  > MariaDB (Datenbankmanagement),
  > php -> phpMyadmin
- MQTT-Client für Mailverssand (Kunde / Subscriber)
- MQTT-Client für Datenbankanbindung
- MQTT-Client für direkte Dartstellung (Digital)
- Mailempfang + Datenbankanbindung



Pico W2040:

-> Sensor auslesen und an MQTT-Broker senden (Publisher) 

-> also Mail mit Messdaten versenden


Konfigurieren einer Datei mit WLAN-Daten, E-Mail, IP des MQTT Brokers, Mailaccount des SMTP-Servers


