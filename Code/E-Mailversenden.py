import smtplib
from email.message import EmailMessage



msg = EmailMessage()
msg['Subject'] = 'I NEED FOOOD'
msg['From'] = 'deine.email'
msg['To'] = 'Ziel E-mail'
msg.set_content('ICH HABE HUNGER, GIB MIR ESSEN')




with smtplib.SMTP_SSL('smtp.domain') as smtp:
    smtp.login('Name', 'passwort')
    smtp.send_message(msg)



print('E-Mail erfolgreich versendet!')

