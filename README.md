Dies ist ein Schulprojekt der FDS-Limburg aus 2025/26 der Klasse 12IBF

Was am Ende fertig sein sollte
Pi(400):
- MQTT Broker (Mosquitto)
- LAMP-Server (XAMPP auf Linux)
  > Apache/Webserver
  > MariaDB (Datenbankmanagement)
  > php -> phpMyadmin
- MQTT-Client für Mailverssand (Kunde / Subscriber)
- MQTT-Client für Datenbankanbindung
- MQTT-Client für direkte Dartstellung (Digital)
- Mailempfang + Datenbankanbindung


Pico:
-Sensor auslesen und an MQTT-Broker senden (Publisher) 
-> also Mail mit Messdaten versenden
Konfigurieren einer Datei mit WLAN-Daten, E-Mail, IP des MQTT Brokers, Mailaccout des SMTP-Servers
