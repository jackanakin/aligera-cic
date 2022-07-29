from paramiko import SSHClient, AutoAddPolicy

class SshClient:
    def __init__(self, host, user, passwd, port):
        print("open ssh")
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        self.ssh.connect(hostname=host,username=user,password=passwd,port=port)

    def executeAndClose(self, cmd):
        try:
            stdin,stdout,stderr = self.ssh.exec_command(cmd)            
            stdout = stdout.readlines()
        finally:
            return stdout

    def close(self):
        print("close ssh")
        self.ssh.close()