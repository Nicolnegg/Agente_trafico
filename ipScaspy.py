from scapy.all import *
from scapy.layers.http import HTTPRequest
__author__ = "Richard Porter (@packetalien)"
__copyright__ = "Copyright 2019, Palo Alto Networks"
__version__ = "0.1"
__license__ = "MIT"
__status__ = "Development"

import paramiko, logging, warnings, random, argparse
from logging.handlers import RotatingFileHandler
warnings.filterwarnings(action='ignore',module='.*paramiko.*')
logging.getLogger("paramiko").setLevel(logging.INFO)

# Setting up with ArgParse

parser = argparse.ArgumentParser(description='SSH Traffic generater settings.')
parser.add_argument("-s", "--server", help="IP address of the SSH Server to generate traffic, default is SE Tools (192.168.35.138)", default="192.168.35.138")
parser.add_argument("-u", "--username", help="SSH Traffic user, default for SE Tools is 'panse'", default="panse")
parser.add_argument("-p", "--password", help="SSH Traffic Password, default for SE Tools is 'paloalto'", default="paloalto")
parser.add_argument("-c", "--command", help="SSH Command to run for SSH traffic type.", default="uname -r")
args = parser.parse_args()

sshServer = args.server
sshUser = args.username
sshPassword = args.password
sshCMD = args.command
sshportlist = [22,80,443,636,3389]

# Setting up logging
logger = logging.getLogger(__name__)
logLevel = 'DEBUG'
maxSize = 10000000
numFiles = 10
handler = RotatingFileHandler('actor.log',maxBytes=maxSize,backupCount=numFiles)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel("DEBUG")

# Setting up Paramiko Log
paramiko.util.log_to_file("paramiko.log")
print('*' * 80 + '\n')
print("Did you know we can decrypt SSH?")
print('*' * 80 + '\n') 

def ssh_traffic(port):
    '''
    This function is a simple SSH connector. The purpose is to generate a live traffic
    connection with a SSH resource. It has four attributes:
    erver: The SSH resource function connects to.
    username: SSH user.
    password: SSH users password.
    sshcmd: SSH command to run for traffic generation.
    port: Port to run command on.
    '''
    try:
        print('*' * 80)
        print("Generating App-ID Traffic for SSH on port: %s" % str(port))
        print('*' * 80 + '\n')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(sshServer,username=sshUser,password=sshPassword,port=port)
        stdin_, stdout_, stderr_ = ssh.exec_command(sshCMD)
        print('*' * 80)
        print("SUCCESS, command sent: %s" % sshCMD)
        print('*' * 80 + '\n')
        out = stdout_.readlines()
        out = str(out)
        print('*' * 80)
        print("Command returned: \n")
        print(out)
        print('*' * 80 + '\n')
        ssh.close()
        logger.debug("Ran the command %s" % sshCMD)
    except:
        print("Soemthing went wrong with the run_ssh_connect() function.")
        print("Please check the actor.log for details.")
        #logger.error("There was an error sending the commend, here is the output %s", err)

if __name__ == "__main__":
    for each in sshportlist:
        ssh_traffic(each)