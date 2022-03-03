# Envío de correos con Python

## Librerías

El primer paso es importar las librerías para el envío de correos.
```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
```

## Mensaje del correo

```python
mensaje = MIMEMultipart()
mensaje['From'] = "paolo@kurios.la"
mensaje['To'] = "paolo.bejarano@gmail.com"
mensaje['Subject'] = "Hola mundo"
cuerpo_del_correo = """
Este es el cuerpo del correo
mensaje.attach(MIMEText(cuerpo_del_correo))
```

## Conexión a servidor SMTP de Sendgrid

```python
server = smtplib.SMTP_SSL('smtp.sendgrid.net', 465)
server.ehlo()
server.login('apikey', 'reemplazar-con-tu-api-key-aqui')
```

### Conexión a servidor SMTP de gmail

Si tienes problemas con Sendgrid, puedes optar por usar el servidor SMTP de Gmail. Solo tienes que tener tu correo y contraseña de Gmail a la mano.

```python
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("tudirecciondecorreo@gmail.com", "tu-contraseña-de-gmail-va-aqui"). # Reemplaza tu dirección de correo y contraseña aquí
```

## Envío de correo

```python
server.sendmail(correo_desde, correo_para, mensaje.as_string())
```






