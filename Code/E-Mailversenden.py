import smtplib
from email.message import EmailMessage



msg = EmailMessage()
msg['Subject'] = 'I NEED FOOOD'
msg['From'] = 'c.froehlich@fds-limburg.schule'
msg['To'] = 'nikita.puidenko@fds-limburg.schule'
msg.set_content('ICH HABE HUNGER, GIB MIR ESSEN')




with smtplib.SMTP_SSL('smtp.fds-limburg.schule') as smtp:
    smtp.login('c.froehlich', 'dc.rWj#=^Dz4!;#')
    smtp.send_message(msg)



print('E-Mail erfolgreich versendet!')
