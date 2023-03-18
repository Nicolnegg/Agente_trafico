import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.1.112", username="user",
            key_filename=os.path.join(os.path.expanduser('~'), ".ssh", "id_ed25519"))
stdin, stdout, stderr = ssh.exec_command('ls -l')
print(stdout.read().decode())
ssh.close()
