import streamlit as st
import smtplib
from socket import gaierror
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Função para enviar o e-mail
def send_email(subject, body, recipient):
    # Configurações do servidor de e-mail
    email_address = "seu_email@example.com"
    password = "sua_senha"
    smtp_server = "smtp.example.com"
    smtp_port = 587

    # Criar uma mensagem de e-mail
    msg = MIMEMultipart()
    msg["From"] = email_address
    msg["To"] = recipient
    msg["Subject"] = subject

    # Adicionar o corpo do e-mail
    msg.attach(MIMEText(body, "plain"))

    # Enviar o e-mail utilizando o servidor SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_address, password)
        server.send_message(msg)

# Interface do Streamlit
st.title("Enviar E-mail")
subject = st.text_input("Assunto")
body = st.text_area("Corpo do E-mail")
recipient = st.text_input("Destinatário")

# Botão para enviar o e-mail
if st.button("Enviar"):
    try:
        send_email(subject, body, recipient)
        st.write('Sent')
    except (gaierror, ConnectionRefusedError):
        st.write("Failed to connect to the server. Bad connection settings?")
    except smtplib.SMTPServerDisconnected:
        st.write("Failed to connect to the server. Wrong user/password?")
    except smtplib.SMTPException as e:
        st.write("SMTP error occurred: " + str(e))
