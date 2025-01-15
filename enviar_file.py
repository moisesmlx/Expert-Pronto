import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox
from smtplib import SMTP
from tkinter import *
import os

def enviar_file(email_usuario, senha, destinatario, endereco_file, assunto):
    try:
      # cria o servidor SMTP
      context = ssl.create_default_context()
      server = smtplib.SMTP('smtp.outlook.com', 587)
      server.ehlo()
      server.starttls(context=context)
      server.ehlo()

      # dados do remetente
      sender_email = email_usuario
      password = senha

      # dados do destinatário
      receivers = [f'{destinatario}']

      # dados do e-mail
      body = assunto
      message = MIMEMultipart()
      message['Subject'] = assunto
      message['From'] = sender_email
      message['To'] = ','.join(receivers)
      message.attach(
        MIMEText(
          f'{assunto}',
          'plain'
        )
      )

      # define os atributos do anexo
      filename = f'minhas_cifras/{endereco_file}.pdf'
      attachment = MIMEBase('application', 'octet-stream')

      with open(filename, 'rb') as f:
        attachment.set_payload(f.read())

      encoders.encode_base64(attachment)

      attachment.add_header(
        'Content-Disposition',
        f'attachment; filename={filename}',
      )

      # anexa o arquivo no e-mail
      message.attach(attachment)

      # realiza login no servidor
      server.login(sender_email, password)

      # envia o email
      server.sendmail(sender_email, receivers, message.as_string())
      messagebox.showinfo(message=f'Email enviado com sucesso')

    except Exception as e:
      messagebox.showerror(message=f'Erro: {e}')
    finally:
      # fecha o servidor
      server.quit()

class Email():
    def __init__(self):
        janela = Tk()

        inf = Label(janela,text='''
        Para enviar cifra por email, é necessário uma conta no outlook;
        Se ainda não tem, crie uma conta lá.
        '''
        , bg='#DDA0DD')
        inf.pack()

        Button(janela, text='Ver lista de cifras', command= lambda:os.startfile('minhas_cifras'), bg='yellow', bd=4).pack(anchor=W)

        
        def enviar():
            enviar_file(email_usuario.get(), senha.get(), destinatario.get(), file.get(), assunto.get())
                                                  
        f = Frame(janela, bd=2, bg='#9370DB')
        Label(f, text='Digite seu email:',bg='#DDA0DD').grid(row=0, column=0, padx=3, pady=3)
        email_usuario = Entry(f, bd=4)
        email_usuario.grid(row=0, column=1, padx=3, pady=3)

        Label(f, text='Digite sua senha:',bg='#DDA0DD').grid(row=1, column=0, padx=3, pady=3)
        senha = Entry(f, bd=4, show='*')
        senha.grid(row=1, column=1, padx=3, pady=3)

        Label(f, text='email do destinátario:',bg='#DDA0DD').grid(row=2, column=0, padx=3, pady=3)
        destinatario = Entry(f, bd=4)
        destinatario.grid(row=2, column=1, padx=3, pady=3)

        Label(f, text='Nome da cifra:',bg='#DDA0DD').grid(row=3, column=0, padx=3, pady=3)
        file = Entry(f, bd=4)
        file.grid(row=3, column=1, padx=3, pady=3)

        Label(f, text='Assunto:',bg='#DDA0DD').grid(row=4, column=0, padx=3, pady=3)
        assunto = Entry(f, bd=4)
        assunto.grid(row=4, column=1, padx=3, pady=3)

        email_usuario.focus()

        f.pack(anchor=W)
        Button(janela, text='enviar', command=enviar, bg='lime', bd=4).pack()

        janela.title('Expert em Cifras')
        janela.config(bg='#DDA0DD')


        janela.mainloop()


if __name__ == '__main__':
    Email()
