from faker import Faker
import requests
import paramiko
import smtplib
from email.mime.text import MIMEText
from ftplib import FTP

fake = Faker()

# Generar tráfico HTTP/HTTPS al azar funciona
url = fake.url()
response = requests.get(url)
print(f'Response code for {url}: {response.status_code}')

# Generar tráfico SSH al azar
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(fake.hostname(), username=fake.user_name(), password=fake.password())
# stdin, stdout, stderr = ssh.exec_command('ls')
# print(f'Response for SSH command "ls": {stdout.read().decode()}')
# ssh.close()
