#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

import requests
import smtplib
import argparse
import ssl


description="Mandar correos electronicos"
parser = argparse.ArgumentParser(description="Practica 8", epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-usr', type=str , help='Correo remitente.')
parser.add_argument('-rec', type=str , help='Correo que receptor.')
parser.add_argument('-pw', type=str , help='Contraseña del usuario.')
parser.add_argument('-msj', type=str, help='Mensaje a enviar.',default = "Buenas olvide poner un mensaje")
parser.add_argument('-asunto', type=str, help='Titulo del correo', default="Hola!")
  
params = parser.parse_args()

usr = (params.usr)
rec = (params.rec)
pw = (params.pw)
msj = (params.msj)
asunto = (params.asunto)
url = (params.url)

email_msg = MIMEMultipart("alternative")
email_msg["From"] = usr
email_msg["To"] = rec
email_msg["Subject"] = asunto

email_msg.attach(MIMEText(msj, "plain"))

#Web-scraping
pag = requests.get(url)
soup = bs(pagina.content,"html.parser")

archivo = "archivo:).txt"
arch = open(archivo, "a")
contenido = soup.find_all("p")[:3]
for p in contenido:
    contenido = p.get_text()
    arch.write(contenido)
arch.close()


filename = archivo   
with open(filename, "rb") as attachment:
    
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
 
encoders.encode_base64(part)


part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)


email_msg.attach(part)


context = ssl.create_default_context()
with smtplib.SMTP("smtp.office365.com", 587) as server:
    server.ehlo()
    server.starttls(context=context)
    server.login(usr, pw)
    server.sendmail(
        usr, rec, email_msg.as_string()
    )
print("successfully sent email to: %s" % (rec))


