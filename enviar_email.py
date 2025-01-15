
import smtplib, ssl

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

from email.mime.base import MIMEBase

from email.utils import formatdate

import email

from email import encoders

from smtplib import SMTP

from email.mime.text import MIMEText

from email.mime.application import MIMEApplication

from email.mime.multipart import MIMEMultipart

import os


def enviar_email_2(assunto, mensagem, destino):

    msg = MIMEMultipart()

    msg['Subject'] = assunto

    msg['From'] = 'expertemcifras@outlook.com'

    msg['To'] = destino

    msg.preamble = 'Multipart massage.\n'
    part = MIMEText(mensagem)
    msg.attach(MIMEText(mensagem))

    smtp = SMTP('smtp.outlook.com', 587)

    smtp.ehlo()

    smtp.starttls()

    smtp.login('expertemcifras@outlook.com', '@#Mmlx1985')

    # Send the email

    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    enviar_email_2('teste', 'Olá Moises sou expert em cifra', 'moises.miss@gmail.com')


