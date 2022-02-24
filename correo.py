# Importando la librería smptlib para usar servidores SMTP
import smtplib

# Importando de la librería email, el package mime, el package multipart, la clase MIMEMultipart
from email.mime.multipart import MIMEMultipart

# Importando de la librería email, el package mime, el package text, la clase MIMEText
from email.mime.text import MIMEText

correo_desde = 'Paolo Bejarano <paolo.bejarano@gmail.com>'
correo_para = 'Paolo Bejarano <paolo@kurios.la>'

mensaje = MIMEMultipart()
mensaje['From'] = correo_desde
mensaje['To'] = correo_para
mensaje['Subject'] = 'Hola mundo'
cuerpo_del_correo = """
Este es el cuerpo del correo
"""
mensaje.attach(MIMEText(cuerpo_del_correo))

#Conectando al servidior SMTP
server = smtplib.SMTP_SSL('smtp.sendgrid.net', 465)
server.ehlo()

# Logearse al servidor de Sendgrid
server.login('apikey', 'reemplazar-con-tu-api-key-aqui')

#Enviar el correo
server.sendmail(correo_desde, correo_para, mensaje.as_string())

# Cerrando la conexión al servidor smtp
server.close()
print("mail sent")
